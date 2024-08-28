# S&P 500 Analysis Project

## Project Overview

This project provides a comprehensive analysis of the S&P 500, focusing on key metrics such market capitalization, trading volume and performance trends throughout the years. Also includes data cleaning, processing and visualization using Python and Tableau.

## Technical Stack

- **VS Code**: For data cleaning and processing
- **Python**: Used for data maniplulation and processing (Pandas, NumPy)
- **Tableau**: For creating interactive dashboards and visualization

## Data Sources

- **S&P 500 Historical Data**: Includes stock prices, market caps, and other financial metrics
- **Sector and Industry Data**: Information about sectors and industries within the S&P 500
- **Kaggle**: the datasets were retrieved from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks)

## Project Structure

- 'data_load.py': Script used to load and process the datasets
- 'data_processing.py': Script used for further data processing, including cleaning and preparation for analysis
- 'cleaned_stocks.csv': The cleaned dataset used for analaysis and visualization
- 'cleaned_companies.xlsx': Processed data about S&P 500 companies, used for sector and industry analysis
- 'cleaned_index.xlsx': Index data relevant to the S&P 500, used for trend analysis
- **Tableau Dashboards**: Three comprehensive dashboards created to visualize different aspects of the S&P 500 data

## Dashboards

1. **S&P 500 Leaders: Volume, Value and Performance Overview**
   - Visualizes top companies by yearly average close, trading volume, and total traded value.
  
2. **S&P 500: Sector Analysis**
   - Analyzes market cap by sector, full-time employees by industry and top 10 companies by market cap.
  
3. **Comprehensive Analysis of S&P 500 Index Trends**
   - Covers historical index performance, rolling average, monthly averages and data point counts.
  
## How to Run the Project

1. **Clone the Repository**:
   - To get a copy of Stock Project, use the following command:
     ```bash
     git clone https://github.com/colemcnabb/StockProject.git
     cd StockProject

2. **Install Dependencies**:
   - Ensure you have Python and the necessary libraries installed. Run the folloiwng command:
     ```bash
     pip install pandas numpy

3. **Run the Scripts**:
   - Execute the Python scripts to load and process the data:
     ```bash
     python data_load.py
     python data_processing.py

4. **View Dashboards**:
   - Open the Tableau files in Tableau to view the interactive dashboards.
  
## Results and Insights

The project reveals key insights regarding the S&P 500 Index, including trends in market capitalization, the relationship between trading volume and total traded value and sector performance

## Future Projects

Future projects of mine will be considerately more advanced and provide a more in-depth look at a variety of topics that interest me.  

These projects will include the following: 

- **Expanded Analysis**: Additional analysis that includes more advanced statistical methods or machine learning models to uncover deeper insights from the data
- **Additional Visualizations**: Creation of more interactive and detailed visualizations that enhance the clarity and impact of the data being presented
- **Exploration of New Data Sources**: Integration of diverse data sources to analyze different industries, financial markets, or emerging trends, providing a broader perspective
- **Automation and Efficiency Improvements**: Development of scripts and tools to automate repetitive tasks, streamline data processing, and improve the overall efficiency of data analysis workflows

## Conclusion

This project serves as a demonstration of my ability to handle, process and visualize data effectively using industry-standard tools and techniques. It is a foundational project intended to showcase essential skills for an Entry Level Data Analyst Role
