COURSE: Coursera Dataset EDA

OVERVIEW
This project runs exploratory analysis on Coursera’s course dataset.
Data cleaning: drop IDs, standardize headers, convert enrollment strings to numbers.
QA checks: missing values, duplicates, outlier detection (retained, visualized on log scale).
EDA: distributions by rating, enrollment, difficulty, certificate type, providers.

PREREQUISITES

Python 3.8+
pandas, numpy, matplotlib, seaborn

SETUP
Clone this repo.
Copy coursera_data.csv to project root.

Install deps:
pip install pandas numpy matplotlib seaborn

USAGE
Open coursera.ipynb.
Run cells sequentially.
Review charts and summary outputs.

NOTEBOOK SECTIONS
Data Cleaning
Exploratory Data Analysis

Conclusions and Next Steps

KEY TAKEAWAYS
Ratings cluster tightly (4.6–4.9) across types.
Mixed-difficulty & Professional certificates show highest median enrollment.
No meaningful correlation between rating and enrollment (r ≈ 0.07).
Retained outliers to preserve real signals; use log scale for skew.

FILES

coursera.ipynb: notebook

coursera_data.csv: raw data

readme.txt: this file

