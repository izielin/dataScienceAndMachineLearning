import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('../pandas/sources/csv_example.csv', index_col=0)
print(df, '\n')
df.to_csv('../pandas/output/csv_output.csv', index=False)

df_2 = pd.read_excel('../pandas/sources/excel_example.xlsx', sheet_name='Sheet1', index_col=0)
print(df_2, '\n')
df_2.to_excel('../pandas/output/excel_output.xlsx', sheet_name='NewSheet', index=False)

# df_3 = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
# print(type(df_3))
# print(df_3[0].head())

engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine)
sql_df = pd.read_sql('my_table', con=engine)
print(sql_df)