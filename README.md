# S&P 500 Analysis Project

## Project Overview

This project provides a comprehensive analysis of the S&P 500, focusing on key metrics such market capitalization, trading volume and performance trends from 2010 - 2024. Also includes data cleaning, processing and visualization using Python and Tableau.

## Technical Stack

- **VS Code**: Used for data cleaning and processing.
- **Python**: Employed for data manipulation and processing using Pandas.
- **Tableau**: Utilized for creating interactive dashboards and visualizations.

## Data Sources

- **S&P 500 Historical Data**: Includes stock prices, market capitalization, and other financial metrics.
- **Sector and Industry Data**: Information about sectors and industries within the S&P 500.
- **Kaggle**: The datasets were retrieved from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks)

## Project Structure

- `data_load.py`: Script used to load and process the datasets.
- `data_processing.py`: Script used for further data processing, including cleaning and preparation for analysis.
- `cleaned_stocks.csv`: The cleaned dataset used for analysis and visualization.<br>
  **Note**: The full `cleaned_stocks.csv` dataset was used in the project but is not included in the repository due to file size constraints.
- `cleaned_stocks_2022.csv`: A subset of the cleaned dataset used for analysis and visualization.
- `cleaned_companies.xlsx`: Processed data about S&P 500 companies, used for sector and industry analysis.
- `cleaned_index.xlsx`: Index data relevant to the S&P 500, used for trend analysis.
- **Tableau Dashboards**: Three comprehensive dashboards created to visualize different aspects of the S&P 500 data.

## Dashboards

1. **S&P 500 Leaders: Volume, Value and Performance Overview**
   - Showcases the leading companies by their yearly average closing prices, trading volume and total trade value.
  
2. **S&P 500: Sector Analysis**
   - Provides a detailed examination of market capitalization across sectors, highlights workforce distribution by industry and identifies the leading companies based on market capitalization.
  
3. **Comprehensive Analysis of S&P 500 Index Trends**
   - Displays an in-depth look at historical index performance, including rolling averages, monthly trends and the distribution of data points over time for clarity.
  
## How to Run the Project

1. **Clone the Repository**:
   - To get a copy of Stock Project, use the following command:
     ```bash
     git clone https://github.com/colemcnabb/StockProject.git
     cd StockProject

2. **Install Dependencies**:
   - Ensure you have Python and the necessary libraries installed. Run the following command:
     ```bash
     pip install pandas numpy

3. **Run the Scripts**:
   - Execute the Python scripts to load and process the data:
     ```bash
     python data_load.py
     python data_processing.py

4. **Review Processed Data**:
   - After running the scripts, you can review the processed data files (`cleaned_stocks_2022.csv`, `cleaned_companies.xlsx`, `cleaned_index.xlsx`) in the `data/` directory.

## Interactive Visualizations

The interactive dashboards created for this project can be accessed via Tableau Public:

   - [S&P 500 Leaders: Volume, Value and Performance Overview](https://public.tableau.com/views/StockProjectLeadersOverview/SP500LeadersVolumeValueandPerformanceOverview?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
   - [S&P 500: Sector Analysis](https://public.tableau.com/shared/26Q2SZCQX?:display_count=n&:origin=viz_share_link)
   - [Comprehensive Analysis of S&P 500 Index Trends](https://public.tableau.com/views/StockProjectIndexTrends/ComprehensiveAnalysisofSP500IndexTrends?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
  
## Results and Insights

**Top Performing Companies**: The analysis identified the top 10 companies based on their average closing prices, with **NVR, Inc. (NVR)** consistently leading since 2016.  This indicates the company has sustained a high market valuation and strong performance over the years.

**Sector Dominance**: The Technology sector dominates the S&P 500, accounting for over **$13 trillion** in market capitalization, making it the largest sector by a significant margin.  The next closest sector, Communication Services, has a market capitalization that is over 50% smaller, highlighting the overwhelming influence of the Technology sector in the index.

**Volume vs Value**: A strong correlation was observed between trading volume and total traded value.  High-volume stocks such as **Tesla (TSLA)** and **Apple(AAPL)** command significant total traded values, reflecting both investor confidence alongside market impact. Conversely, stocks like **Ford (F)** show that high trading volume does not always equate to high traded value, particularly when the stock prices are lower.

**Index Performance Trends**: The S&P 500 has shown a steady upward trend over the last decade, with a large increase observed from 2020-2021. This reflects a period of rapid recovery and growth, driven by the post-pandemic market dynamics and the performance of leading technology companies.

**Employment by Industry**: An overview of the full-time employees by industry show that **Discount Stores** and **Internet Retail** are some of the largest employers within the S&P 500.  This highlights the labour-intensive nature of these industries, which require a large workforce to sustain operations.

**Revenue Growth and EBITDA**: The **Technology** and **Healthcare** sectors exhibit the highest EBITDA values, indicating that strong revenue growth within these industries is often tied to significant profitability.  This suggests that companies within these sectors are efficiently converting their revenue growth into earnings, cementing themselves as dominant players within the S&P 500.


## Future Projects

Future projects of mine will gradually become more advanced and provide an in-depth look at a variety of topics that interest me.  

These projects will include the following:

- **Expanded Analysis**: Additional analysis that includes more advanced statistical methods or machine learning models to uncover deeper insights from the data.
- **Additional Visualizations**: Creation of more interactive and detailed visualizations that enhance the clarity and impact of the data being presented.
- **Exploration of New Data Sources**: Integration of diverse data sources to analyze different industries, financial markets, or emerging trends, providing a broader perspective.
- **Automation and Efficiency Improvements**: Development of scripts and tools to automate repetitive tasks, streamline data processing, and improve the overall efficiency of data analysis workflows.

## Conclusion

This project serves as a demonstration of my ability to handle, process and visualize data effectively using industry-standard tools and techniques. This foundational project is intended to showcase essential skills required for an Entry Level Data Analyst role.
