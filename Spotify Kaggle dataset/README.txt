# Spotify Top 50 (2020) — Exploratory Analysis

This notebook walks through a quick, end-to-end look at **Spotify’s Top 50 tracks of 2020**.  
The goals are to answer the product-manager’s checklist and to surface a few business-ready insights:

1. **Audio-profile** – show typical values and spread of key numeric features (danceability, loudness, acousticness, etc.) so we know what the 2020 chart *sounds* like.  
2. **Hit concentration** – see whether a handful of artists/albums dominate or success is more evenly spread.  
3. **Genre comparison** – compare Pop, Hip-Hop/Rap, Dance/Electronic and Alternative/Indie on danceability, loudness and acousticness.  

Along the way the notebook covers data loading, basic cleaning (missing-value, duplicate and outlier checks) and a small correlation study.

---

## Quick findings

| Theme | Insight (2020 Top-50) |
|-------|-----------------------|
| **Danceability** | 64 % of tracks score ≥ 0 .70; high-groove songs largely rule the chart. |
| **Loudness vs Energy** | r ≈ 0 .79 — louder mixes register as more energetic. Nearly 40 % of hits sit above –5 dB. |
| **Artist/Album spread** | 7 artists and 4 albums supply **34 %** and **18 %** of the list, yet 40 acts and 45 albums appear overall — room for new names. |
| **Genre leaders** | Hip-Hop/Rap & Dance/Electronic top danceability; Alternative/Indie is most acoustic; Pop sits in the middle but with widest range. |
| **Long-tail genres** | 10 niche genres place exactly one song each — best promoted in targeted, genre-specific playlists. |

---

## Notebook outline

| Section | What happens |
|---------|--------------|
| **0 – Project Aim** | States the three business-oriented goals. |
| **1 – Download** | Pulls the CSV from Kaggle with `kagglehub`. |
| **2 – Load** | Reads the file into a pandas DataFrame. |
| **3 – Data Cleaning** | Checks missing values, duplicates, outliers (IQR rule) and explains decisions. |
| **4 – EDA** | Answers 20+ PM questions: counts, top artists, genre mix, most/least danceable & loud, correlations, etc. |
| **5, 6, 7 – Genre deep-dives** | Compares danceability, loudness, acousticness across four headline genres. |
| **Conclusion** | One-paragraph business summary: push proven stars, feature high-groove loud tracks in workout/party lists, use genre playlists to surface quieter or acoustic cuts. |
