# 🧸 Toylytics

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/sujalbundheliya/Toylytics.git)

## 📌 Description

**Toylytics** scrapes sponsored "soft toys" listings from Amazon.in, cleans the data, and analyzes it to reveal brand performance, pricing trends, and customer insights. It outputs clear visualizations to help understand product popularity and market dynamics.

---

## ✨ Features

- ✅ Scrapes sponsored product listings for "soft toys" from Amazon.in
- ✅ Extracts product info: Title, Brand, Reviews, Rating, Price, Image URL, Product URL
- ✅ Cleans and standardizes raw data (handles ₹, commas, missing values, etc.)
- ✅ Analyzes brand frequency, price-rating patterns, and reviews
- ✅ Generates clear and insightful visualizations

---

## 🚀 Quick Setup Guide

Follow these steps to set up and run **Toylytics** locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sujalbundheliya/Toylytics.git
cd Toylytics
```

### 2️⃣ Set Up Virtual Environment (Recommended)

- **For Windows:**
```powershell
python -m venv env
.\env\Scripts\activate
```
- **For macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧹 Run the Scraper

The scraper uses **Playwright** to extract sponsored product data from Amazon.in.

### Step 1: Install Playwright (if not already installed)
```bash
playwright install
```

### Step 2: Run the Scraper
```bash
python scraper.py
```

- Data will be saved to: `data/raw_data.csv`

---

## 🧼 Clean & Prepare Data

Run the cleaning script to format and prepare the data for analysis:

```bash
python scripts/clean_prepare.py
```

- Output: `data/cleaned_data.csv`

---

## 📊 Run the Analysis

Launch the Jupyter Notebook to analyze the cleaned data and generate visualizations:

```bash
jupyter notebook notebooks/analysis.ipynb
```

Analyses performed:
- ✅ Top Brands by Frequency and Average Rating
- ✅ Price vs Rating Distribution & Outliers
- ✅ Top 5 Most Reviewed and Highest Rated Products

---

## 📂 Project Structure

```
Toylytics-/
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── notebooks/
│   └── analysis.ipynb
├── scripts/
│   └── clean_prepare.py
├── scraper.py
├── requirements.txt
├── README.md
```

---

## 📦 Dependencies

- `playwright`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `jupyter`

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Troubleshooting

- **Playwright errors?** Run `playwright install` again to ensure drivers are installed.
- **Amazon blocking?** Avoid scraping too fast or use headless=False for easier debugging.
- **Data mismatch?** Ensure sponsored products exist on the page before scraping.

---

## 👨‍💻 Author

- [Sujal Bundheliya](https://github.com/sujalbundheliya)

---

⭐ If you find this project useful, don’t forget to **star the repository**!

