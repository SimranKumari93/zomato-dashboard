#  Zomato Analytics Dashboard – Power BI Project

## Overview

This Power BI project is an end-to-end data analysis and dashboard solution built using real-world restaurant data from India.
The dashboard uncovers key insights into customer preferences, restaurant popularity, rating patterns, and geographic trends, 
enabling data-driven decision-making for businesses in the food and hospitality industry.

---

## 🏁 Objectives

- Analyze restaurant performance based on votes, ratings, cost, and location.
- Identify top-performing restaurants by votes and ratings.
- Visualize rating distribution across different price ranges.
- Explore geographic spread of restaurant activity via interactive maps.
- Simplify complex data for non-technical users via user-friendly visuals.

---

## 🗃️ Dataset

The dataset includes two main files:

1. **`cleaned_data.csv`**  
   Contains restaurant-level data such as:
   - Restaurant name
   - City and locality
   - Average cost for two
   - Online delivery availability
   - Aggregate rating and rating text
   - Number of votes
   - Price range
   - Cuisine types

2. **`country-code.csv`**  
   Provides mapping between `country_code` and full country names.

---

## 🛠️ Tools Used

- **Power BI Desktop**
- **DAX** for calculated columns and measures
- **Python** (for data cleaning, handling duplicates, data types, missing data)
- **Map Visualizations** for geographic insights(through latitudes and longitudes)

---

## 📊 Features and Visuals

### ✅ Key Dashboards

- **Top 10 Restaurants by Votes**  
  Displays the most popular restaurants.

- **Rating Distribution by Price Range**  
  Uses a stacked column chart to show how ratings vary with price level.

- **Restaurant Count by Rating Text**  
  Highlights sentiment distribution (e.g., "Excellent", "Good", "Poor").

- **Map of Total Votes by Country**  
  Interactive map showing voting intensity by country.

- **Pie Chart of Online Delivery Availability**  
  Compares restaurants offering delivery vs. those that don’t.

---

## 🧮 Sample DAX Measures

```dax
Total Votes = SUM(cleaned_data[votes])
Average Rating = AVERAGE(cleaned_data[Aggregate rating])
Total Restaurants = DISTINCTCOUNT(cleaned_data[Restaurant ID])
Online Delivery % = 
DIVIDE(
    CALCULATE(COUNTROWS(cleaned_data), cleaned_data[has_online_delivery] = 1),
    COUNTROWS(cleaned_data)
)
Top 10 Votes = [Total Votes]  -- Use the "Total Votes" measure from earlier used filters to find top 10 palces by votes
---
- ** Data Model***
A relationship is created between the tables:

cleaned_data[country_code] → country-code[Country Code] (Many-to-One)

This allows for seamless analysis by country name instead of code.


