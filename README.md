# E-commerce Analytics Pipeline (Spark & Databricks)
## Overview

This project demonstrates a foundational-to-intermediate data engineering and analytics pipeline using Apache Spark (PySpark) and Databricks.
The focus was on learning how Spark and Databricks work in practice and applying them to derive basic business insights from e-commerce data

### What I Learned

How to use Databricks workspaces, notebooks, and Unity Catalog volumes

- Spark DataFrame API, schema enforcement, and joins

- Delta Lake for reliable storage (Silver & Gold layers)

- Fact and dimension modeling (star schema basics)

- Broadcast joins and basic performance awareness

- Creating analytics-ready datasets and visualizations

## Architecture 
CSV → Databricks (Raw) → PySpark → Delta Lake (Gold) → Analytics

## Dataset

- Synthetic e-commerce data (~1M rows, ~80 MB)

- Orders, customers, products, payments, cities

## Analytics & KPIs

- Revenue by City – identifies high-performing regions

- Revenue Leakage (Cancellations) – measures lost revenue

- Discount Effectiveness – evaluates impact of discounts

- Payment Method Analysis – compares order value and volume

## 📊 Visualizations & Insights

## 📊 Visualizations & Insights

### Top Cities by Revenue
![Top Cities by Revenue](visualizations/top_cities_by_revenue.png)

### Payment Method Economics
![Payment Method Economics](visualizations/payment_method_economics.png)

### Discount Effectiveness
![Discount Effectiveness](visualizations/discount_effectiveness.png)

