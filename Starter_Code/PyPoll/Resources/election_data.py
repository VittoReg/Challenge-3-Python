# Import Dependencies
import os
import pandas as pd
from pathlib import Path

# Store filepaths into variable
election_data = Path("Resources/election_data.csv")

election_data_df = pd.read_csv("election_data.csv")
election_data_df

num_rows = election_data_df.shape[0]
ccs_count = election_data_df["Candidate"].value_counts()["Charles Casper Stockham"]
dg_count = election_data_df["Candidate"].value_counts()["Diana DeGette"]
rad_count = election_data_df["Candidate"].value_counts()["Raymon Anthony Doane"]

ccspercent = (ccs_count)/(num_rows)*(100)
dgpercent = (dg_count)/(num_rows)*(100)
radpercent = (rad_count)/(num_rows)*(100)

ccspercent = f"{ccspercent:.3f}"
dgpercent = f'{dgpercent:.3f}'
radpercent = f'{radpercent:.3f}'

print("Election results")
print("--------------------------------------")
print(f"Total Votes: {num_rows}")
print(f"Charles Casper Stockham: {ccspercent}% ({ccs_count})")
print(f"Diana DeGette: {dgpercent}% ({dg_count})")
print(f"Raymond Anthony Doane: {radpercent}% ({rad_count})")
print("--------------------------------------")
print("Winner: Diana DeGette")

txtfile = "election_results2.txt"
with open(txtfile, "w") as file:
    file.write('Election Results\n')
    file.write('-----------------\n')
    file.write(f'The total number of votes is: {num_rows}\n')
    file.write('-----------------\n')
    file.write(f"Charles Casper Stockham: {ccspercent}% ({ccs_count})\n")
    file.write(f"Diana DeGette: {dgpercent}% ({dg_count})\n")
    file.write(f"Raymond Anthony Doane: {radpercent}% ({rad_count})\n")
    file.write('-----------------\n')
    file.write("Winner: Diana DeGette")
    
print("""Election analysis has been saved in "election_results2.txt" """)