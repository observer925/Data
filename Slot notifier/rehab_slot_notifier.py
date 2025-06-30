#!/usr/bin/env python3
"""
rehab_slot_notifier.py

Monitor rehab‐slot availability on:
https://ipr.esveikata.lt/available-registrations?organizationId=1000097880&serviceId=434

Requirements:
  pip install selenium webdriver-manager
  Set these environment variables before running:
    EMAIL_ADDRESS    – your SMTP login (e.g. Gmail address)
    EMAIL_PASSWORD   – your SMTP password or app-specific password
    NOTIFY_EMAIL     – the email to receive alerts
"""

import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPAuthenticationError
import re

# —— CONFIGURATION —— #
URL = "https://ipr.esveikata.lt/available-registrations?organizationId=1000097880&serviceId=434&leftBound=1747728000000"
CHECK_INTERVAL = 5  # seconds between full scans
TARGET_NAME = "TIK PSICHIKOS IR ELGESIO"  # change this to the slot name you’re hunting

# Email settings (via environment variables)
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
NOTIFY_EMAIL = os.getenv("NOTIFY_EMAIL")

if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, NOTIFY_EMAIL]):
    raise RuntimeError(
        "Please set EMAIL_ADDRESS, EMAIL_PASSWORD, and NOTIFY_EMAIL env vars."
    )


def notify_user(message: str):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["Subject"] = f"[Rehab Notifier] Slot on {message.split('→')[0].strip()}"
    msg["From"] = f"Rehab Notifier <{EMAIL_ADDRESS}>"
    msg["To"] = NOTIFY_EMAIL
    msg["Reply-To"] = EMAIL_ADDRESS

    # Build a simple plain-text body
    body = (
        f"Hello,\n\n"
        f"A matching rehab slot was found:\n\n"
        f"  {message}\n\n"
        f"Please visit the registration page to book it:\n"
        f"{URL}\n\n"
        f"Best,\n"
        f"Rehab Notifier Bot\n"
    )
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_ADDRESS, NOTIFY_EMAIL, msg.as_string())
        print(f"[Alert sent] {message}")
    except SMTPAuthenticationError as e:
        print(f"[Email error] Authentication failed: {e}")


def create_driver():
    chrome_opts = Options()
    chrome_opts.binary_location = (
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    )
    chrome_opts.add_argument("--headless")
    chrome_opts.add_argument("--disable-gpu")

    # Download the matching driver for Brave v136.0.7103.93
    driver_path = ChromeDriverManager(driver_version="136.0.7103.93").install()
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_opts)

    # try loading the page up to 3 times
    for attempt in range(1, 4):
        try:
            driver.get(URL)
            return driver
        except Exception as e:
            print(f"[create_driver] load attempt {attempt} failed: {e}")
            if attempt < 3:
                time.sleep(2)
            else:
                driver.quit()
                raise

    # should never reach here
    return driver


def check_slots(driver) -> None:
    """
    1) Reset page and wait for inline calendar to appear
    2) Month-by-month: click each enabled day → wait for the slot list to settle → alert on TARGET_NAME
    3) Advance to next month and repeat until no enabled days remain
    """
    # 1) load/reset the page and wait for the calendar’s “Next month” arrow
    driver.get(URL)
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mat-calendar-next-button"))
        )
    except TimeoutException:
        print("[Scan] ⚠️ calendar never appeared, skipping this round.")
        return

    next_btn = driver.find_element(By.CSS_SELECTOR, "button.mat-calendar-next-button")

    # 2) loop until no enabled days remain
    while True:
        days = driver.find_elements(
            By.CSS_SELECTOR,
            "button.mat-calendar-body-cell:not(.mat-calendar-body-disabled)"
        )
        if not days:
            print("[Scan] no enabled days left, stopping.")
            return

        for day in days:
            date_str = day.get_attribute("aria-label") or day.text
            day.click()

            # Poll until the slot list stabilizes (up to 3s)
            max_wait, interval = 3.0, 0.1
            deadline = time.time() + max_wait
            prev_count, stable = -1, 0
            while time.time() < deadline:
                elems = driver.find_elements(By.ID, "commentText")
                cnt = len(elems)
                if cnt == prev_count:
                    stable += 1
                else:
                    stable = 0
                if stable >= 2:
                    break
                prev_count = cnt
                time.sleep(interval)

            # snapshot & alert
            slot_texts = []
            for el in elems:
                try:
                    text = el.text.strip()
                    if text:
                        slot_texts.append(text)
                except StaleElementReferenceException:
                    continue

            print(f"Scanned {date_str}: found {len(slot_texts)} slot(s)")
            for t in slot_texts:
                if TARGET_NAME.lower() in t.lower():
                    notify_user(f"{date_str} → {t}")

        # 3) advance to next month
        next_btn.click()
        time.sleep(0.5)


def main():
    driver = create_driver()
    try:
        while True:
            check_slots(driver)
            print(
                f"[{datetime.datetime.now().isoformat()}] Scan complete. Next check in {CHECK_INTERVAL} seconds."
            )
            time.sleep(CHECK_INTERVAL)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
