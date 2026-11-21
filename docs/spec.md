
# Web Scraper and Price Tracker

## 1. Project Overview
This project is a Python-based web scraping application that collects book information and tracks book prices over time.

## 2. Target Website
https://books.toscrape.com/

This website is used for learning and practicing web scraping.

## 3. Data to Collect
For each book, the application will collect:
- Book title
- Price
- Rating
- Availability
- Category
- Product URL

## 4. Database Design
We will use MySQL with two tables:

### Products
- id
- title
- url
- category
- rating

### Price History
- id
- product_id
- price
- availability
- scraped_at

## 5. Price Alert
Users can set a target price for a book.

If the latest price becomes equal to or lower than the target price, the application will generate an alert.

## 6. Dashboard
The Streamlit dashboard will display:
- All collected books
- Current prices
- Price history charts
- Product search and category filters
- Watchlist and price alerts
- Last scraping time

## 7. Technologies
- Python
- Requests
- BeautifulSoup
- Pandas
- MySQL
- Streamlit
- Schedule
- SMTP
- Pytest

## 8. Project Goal
The goal is to build a working application that automatically collects book data, stores price history, tracks target prices, and displays information through an interactive dashboard.
