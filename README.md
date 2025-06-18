# S&P 500 Analysis (2010 - 2024)

## Project Overview

This project provides a comprehensive analysis of the S&P 500, focusing on key metrics such market capitalization, trading volume and performance trends from 2010 - 2024.

---

## Technical Stack

| Stage          | Tool                                   |
|----------------|----------------------------------------|
| Data cleaning  | Python in VS Code                      |
| Dashboards     | Tableau Public                         |

---

## Data Sources

- **S&P 500 Historical Data**: Includes stock prices, market capitalization, and other financial metrics.
- **Sector and Industry Data**: Information about sectors and industries within the S&P 500.
- **Kaggle**: The datasets were retrieved from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks)

---

## Tableau Dashboards

1. **S&P 500 Leaders: Volume, Value and Performance Overview**
   - Showcases the leading companies by their yearly average closing prices, trading volume and total trade value.
  
2. **S&P 500: Sector Analysis**
   - Provides a detailed examination of market capitalization across sectors, highlights workforce distribution by industry and identifies the leading companies based on market capitalization.
  
3. **Comprehensive Analysis of S&P 500 Index Trends**
   - Displays an in-depth look at historical index performance, including rolling averages, monthly trends and the distribution of data points over time for clarity.

---
  
## Interactive Visualizations

The interactive dashboards created for this project can be accessed via Tableau Public:

   - [S&P 500 Leaders: Volume, Value and Performance Overview](https://public.tableau.com/views/StockProjectLeadersOverview/SP500LeadersVolumeValueandPerformanceOverview?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
   - [S&P 500: Sector Analysis](https://public.tableau.com/shared/26Q2SZCQX?:display_count=n&:origin=viz_share_link)
   - [Comprehensive Analysis of S&P 500 Index Trends](https://public.tableau.com/views/StockProjectIndexTrends/ComprehensiveAnalysisofSP500IndexTrends?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
  
## Results and Insights

**Top Performing Companies**: The analysis identified the top 10 companies based on their average closing prices, with **NVR, Inc. (NVR)** consistently leading since 2016.  This indicates the company has sustained a high market valuation and strong performance over the years.

**Sector Dominance**: The Technology sector dominates the S&P 500, accounting for over **$13 trillion** in market capitalization, making it the largest sector by a significant margin.  The next closest sector, Communication Services, has a market capitalization that is over 50% smaller, highlighting the overwhelming influence of the Technology sector in the index.

**Volume vs Value**: A strong correlation was observed between trading volume and total traded value.  High-volume stocks such as **Tesla (TSLA)** and **Apple (AAPL)** command significant total traded values, reflecting both investor confidence alongside market impact. Conversely, stocks like **Ford (F)** show that high trading volume does not always equate to high traded value, particularly when the stock prices are lower.

**Index Performance Trends**: The S&P 500 has shown a steady upward trend over the last decade, with a large increase observed from 2020-2021. This reflects a period of rapid recovery and growth, driven by the post-pandemic market dynamics and the performance of leading technology companies.

**Employment by Industry**: An overview of the full-time employees by industry show that **Discount Stores** and **Internet Retail** are some of the largest employers within the S&P 500.  This highlights the labour-intensive nature of these industries, which require a large workforce to sustain operations.

**Revenue Growth and EBITDA**: The **Technology** and **Healthcare** sectors exhibit the highest EBITDA values, indicating that strong revenue growth within these industries is often tied to significant profitability.  This suggests that companies within these sectors are efficiently converting their revenue growth into earnings, cementing themselves as dominant players within the S&P 500.

---

## Repository Structure

data/     -> Raw and cleaned CSV/XLSX
scripts/  -> data_load.py and data_processing.py
img/      -> Dashboard preview PNGs
README.md -> Project overview (this file)


