import pandas as pd
df=df = pd.read_csv("malayalam case study\\malayalam_actors_actresses.csv")
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
# ANALYSIS
print(df[df["age"] > 25])
print(df[(df["age"] > 25) & (df["gender"] == "Male")])
# avg age using gender
print(df.groupby("gender")["age"].mean())
# sort age
print(df.sort_values(["age"]))
# Basic value count
print(df["gender"].value_counts())
# active status count
print(df['active_status'].value_counts())
# who done top 3 most no of films
print(df.sort_values("no_of_films", ascending=False).head(3))
# avg of number of films
print(df["no_of_films"].mean())
# avg of no of awards
print(df["no_of_awards"].mean())
# avg of debut year
print(df["debut_year"].mean())