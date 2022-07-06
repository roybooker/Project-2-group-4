# Import
import pandas as pd
import numpy as np

def performance_metrics(df, strategy_name):
    metrics = [
    'Annualized Return',
    'Cumulative Returns',
    'Annual Volatility',
    'Sharpe Ratio',
    'Sortino Ratio'
    ]
    
    columns = [strategy_name]
        
    # Initialize the DataFrame with index set to evaluation metrics and columns 
    portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)
    
    portfolio_evaluation_df.loc['Annualized Return'] = (df['Portfolio Daily Returns'].mean() * 252)
    
    portfolio_evaluation_df.loc['Cumulative Returns'] = df['Portfolio Cumulative Returns'][-1]
    
    # Calculate the Annual volatility metric
    portfolio_evaluation_df.loc['Annual Volatility'] = (df['Portfolio Daily Returns'].std() * np.sqrt(252)    )
     
    
    # Calculate the Sharpe ratio
    portfolio_evaluation_df.loc['Sharpe Ratio'] = (
        df['Portfolio Daily Returns'].mean() * 252) / (
        df['Portfolio Daily Returns'].std() * np.sqrt(252)
    )
    
    # Calculate the Sortino ratio
    # Start by calculating the downside return values

    # Create a DataFrame that contains the Portfolio Daily Returns column
    sortino_ratio_df = df[['Portfolio Daily Returns']].copy()

    # Create a column to hold downside return values
    sortino_ratio_df.loc[:,'Downside Returns'] = 0

    # Find Portfolio Daily Returns values less than 0, 
    # square those values, and add them to the Downside Returns column
    sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < 0, 
                         'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2

    # Calculate the annualized return value
    annualized_return = sortino_ratio_df['Portfolio Daily Returns'].mean() * 252

    # Calculate the annualized downside standard deviation value
    downside_standard_deviation = np.sqrt(sortino_ratio_df['Downside Returns'].mean()) * np.sqrt(252)

    # Divide the annualized return value by the downside standard deviation value
    sortino_ratio = annualized_return/downside_standard_deviation

    # Add the Sortino ratio to the evaluation DataFrame
    portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio
    
    return portfolio_evaluation_df
