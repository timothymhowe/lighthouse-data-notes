import pandas as pd
import sys
from supporting_files.data_loader import load_excel

df = pd.read_excel('supporting_files/SaleData.xlsx')

"""
Write a Pandas program to find the total sale amount (Sale_amt) region and manager wise. 
Order the dataframe by Sale_amt, starting with the highest.
Output should be DataFrame with 3 columns (order is important):
    - Region
    - Manager
    - Sale_amt
and numeric index starting with 0 (after sorting).
"""

print(df)


def compute_total_sale(df):
    # new_df = pd.DataFrame(df['Region', 'Manager', 'Sale_amt'])
    new_df = df.groupby(['Region', 'Manager']).on(['Region', 'Manager', 'Sale_amt'])
    new_df.sort_values(by=['Sale_amt'], ascending=False, ignore_index=True)
    return new_df
# %%
