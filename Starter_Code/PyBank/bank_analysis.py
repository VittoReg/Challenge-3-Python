# Import Dependencies
import os
import pandas as pd
from pathlib import Path

# Store filepaths into variable
budget_data = Path("Resources/budget_data.csv")

budget_data_df = pd.read_csv("budget_data.csv")
pd.set_option("display.max.rows", 90)
budget_data_df

num_rows = budget_data_df.shape[0]
column_sum = budget_data_df["Profit/Losses"].sum()

max_profit_row = budget_data_df.loc[budget_data_df['Profit/Losses'].idxmax()]
max_profit_value = max_profit_row['Profit/Losses']
max_profit_date = max_profit_row['Date']

min_profit_row = budget_data_df.loc[budget_data_df['Profit/Losses'].idxmin()]
min_profit_value = min_profit_row['Profit/Losses']
min_profit_date = min_profit_row['Date']

diff = budget_data_df["Profit/Losses"].diff()

avg_change = diff.mean()
avg_change = f"{avg_change:.2f}"

print(f"Total Months: ${num_rows}")
print(f"Total: ${column_sum}")
print(f"Greatest Increase in Profits: {max_profit_date} ${max_profit_value}")
print(f"Greatest Decrease in Profits: {min_profit_date}, ${min_profit_value}")
print(f"Average change: ${avg_change}")


output_file = 'analysis_results2.txt'
with open(output_file, 'w') as file:
    file.write('The budget data csv file has been analysed and produced the following results:\n')
    file.write(f'Total number of months in the dataset: ${num_rows}\n')
    file.write(f'The net total amount of Profit/Losses is: ${column_sum}\n')
    file.write(f'Greatest Increase in Profits: {max_profit_date}, ${max_profit_value}\n')
    file.write(f'Greatest Decrease in Profits: {min_profit_date}, ${min_profit_value}\n')
    file.write(f'The changes in profit/losses over the entire period is: ${avg_change}\n')

print(f'Results have been saved to {output_file}')