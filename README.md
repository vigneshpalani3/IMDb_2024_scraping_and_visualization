

# 🎬 IMDb 2024: Scraping and Visualization

This project scrapes movie data from IMDb's 2024 listings, processes and cleans it, and provides interactive visualizations using Streamlit. It’s built to help users explore trends across genres, ratings, votes, durations, and more.

---

## 🚀 Features

- ✅ Web scraping using Selenium
- ✅ Genre-wise CSV exports
- ✅ SQL database integration
- ✅ Streamlit app with interactive filters
- ✅ Visual insights: bar charts, heatmaps, scatter plots

---

## 📂 Project Structure

```
IMDb_2024_scraping_and_visualization/
├── csv files/              # Cleaned CSVs per genre
├── sql/                    # SQL dump or table creation scripts
├── pages/                  # Additional Streamlit app pages
├── utils/                  # Data processing helper scripts
├── Home.py                 # Main Streamlit app
├── IMDB_scrapping.ipynb    # Jupyter notebook for scraping
└── README.md               # Project documentation
```

---

## ⚙️ Getting Started

> All you need is **Python 3.7+** installed.

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

(If `requirements.txt` isn’t ready, install manually:)

```bash
pip install pandas selenium streamlit matplotlib seaborn sqlalchemy
```

### 2. Run the App

```bash
streamlit run Home.py
```

---

## 💾 SQL Setup (Optional)

To use the SQL features:

- Import the `.sql` file from the `/sql` folder into your MySQL/PostgreSQL server.
- Connect using SQLAlchemy in your code.

---

## 📊 Data Source

- Data scraped from [IMDb](https://www.imdb.com/) – 2024 movies.

---

## 📌 Use Cases

- Explore highest-rated movies
- Compare ratings and vote counts by genre
- Analyze duration extremes
- Use filters to customize results interactively

---

## 🙌 Author

**Vignesh Palani**  
📫 [GitHub](https://github.com/vigneshpalani3)
