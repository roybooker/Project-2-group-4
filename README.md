# PROJECT 4 TITLE

## Objective
To analyse the S&P 500 trading data for the past 20 years using various machine learning models and provide a visual comparison and evaluation on how each model performs.

The most efficient model can then be used by the Amazon Lex based RoboAdvisor to advise users on how much returns they can expect on their initial investment.  

*RoboAdvisor is not part of this project due to the time constraints*.

The project was analysed in July 2022 by :
-   Padma Ram
-   Roy Booker
-   Jigar Lotia

The project uses various Notebooks to perform the analysis with high level process flow depicted as below:

## High Level Process Flow

*Process Flow Image to be added here*


Each of the notebook and the corresponding process that happens is described as below:

## Notebook 1 - Data Preparation

This [notebook](src/Data_Processing.ipynb) uses the historical price of S&P 500 Index for past 20 years.  This data is sourced from [Investing.com](https://au.investing.com/indices/us-spx-500) and is stored as [S&P500_Data.csv](data/SP500_Data.csv).

The notebook performs the following pre-processing using the `Pandas DataFrame` :
- Parse Dates in the data file with `parse_dates` attribute
- Calculate daily percentage change using the `pct_change` function
- Dropping nulls using `dropna` function

In addition, this notebook also performs the following step to prepare the data that can be used by various machine learning models: 

- Calculate the Simple Moving Average (SMA) for perod of 4 days and 50 days which are used as short window and long window
- Buy / Sell signal calculation based on whether the short window of SMA crosses the long window which is interpreted as **Buy** signal otherwise as the **Sell** signal. 
