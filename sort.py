import pandas as pd

df = pd.read_csv("e:\\reactJS\\project-api\\users.csv")

sorted_df = df.sort_values(by=["Name"], ascending=True)

sorted_df.to_csv('usersSorted.csv', index=False)