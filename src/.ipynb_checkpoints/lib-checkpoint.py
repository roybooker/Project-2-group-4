# Import
import pandas as pd
import numpy as np

def performance_metrics(df, strategy_name):
    metrics = [
    'Annualized Return',
    'Cumulative Returns',
    'Annual Volatility',
    'Sharpe Ratio',
    'Sortino Ratio',
    'Max Actual Return',
    'Max Strategy Return',
    'SS Lag',
    'Max SReturn Lag'   
    ]
    
    columns = [strategy_name]
        
    # Initialize the DataFrame with index set to evaluation metrics and columns 
    portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)
    
    portfolio_evaluation_df.loc['Annualized Return'] = (df['strategy_returns'].mean() * 252)
    
    portfolio_evaluation_df.loc['Cumulative Returns'] = df['cumulative_Returns'][-1]
    
    # Calculate the Annual volatility metric
    portfolio_evaluation_df.loc['Annual Volatility'] = (df['cumulative_Returns'].std() * np.sqrt(252)    )
     
    
    # Calculate the Sharpe ratio
    sharpe_ratio = (
        df['strategy_returns'].mean() * 252) / (
        df['strategy_returns'].std() * np.sqrt(252)
    )
    
    portfolio_evaluation_df.loc['Sharpe Ratio'] = sharpe_ratio
    
    # Calculate the Sortino ratio
    # Start by calculating the downside return values

    # Create a DataFrame that contains the Portfolio Daily Returns column
    sortino_ratio_df = df[['strategy_returns']].copy()

    # Create a column to hold downside return values
    sortino_ratio_df.loc[:,'Downside Returns'] = 0

    # Find Portfolio Daily Returns values less than 0, 
    # square those values, and add them to the Downside Returns column
    sortino_ratio_df.loc[sortino_ratio_df['strategy_returns'] < 0, 
                         'Downside Returns'] = sortino_ratio_df['strategy_returns']**2

    # Calculate the annualized return value
    annualized_return = sortino_ratio_df['strategy_returns'].mean() * 252

    # Calculate the annualized downside standard deviation value
    downside_standard_deviation = np.sqrt(sortino_ratio_df['Downside Returns'].mean()) * np.sqrt(252)

    # Divide the annualized return value by the downside standard deviation value
    sortino_ratio = annualized_return/downside_standard_deviation

    # Add the Sortino ratio to the evaluation DataFrame
    portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio
    
    # Add the max_return to the evaluation DataFrame
    pred_cumprod = (1 + df[["actual_returns"]]).cumprod()
    pred_cumprod =pred_cumprod.reset_index()
    list_index = list(pred_cumprod.index)
    list_y = list(pred_cumprod["actual_returns"])
    max_return = integrate(list_index, list_y)
    portfolio_evaluation_df.loc['Max Actual Return'] = max_return
    
    # Add the max_strategy_return to the evaluation DataFrame
    pred_cumprod = (1 + df[["strategy_returns"]]).cumprod()
    pred_cumprod =pred_cumprod.reset_index()
    list_index = list(pred_cumprod.index)
    list_y = list(pred_cumprod["strategy_returns"])
    max_strategy_return = integrate(list_index, list_y)
    portfolio_evaluation_df.loc['Max Strategy Return'] = max_strategy_return
    
    portfolio_evaluation_df.loc['Max Return Lag'] = max_return - max_strategy_return
    portfolio_evaluation_df.loc['SS Lag'] = sharpe_ratio - sortino_ratio
    
    return portfolio_evaluation_df


def integrate(x, y):
    sm = 0
    for i in range(1, len(x)):
        h = x[i] - x[i-1]
        sm += h * (y[i-1] + y[i]) / 2
        
    return sm

