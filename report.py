import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv('Sales Data.csv')
print(df)

#generate a report
profile=ProfileReport(df)
profile.to_file(output_file="report.html")