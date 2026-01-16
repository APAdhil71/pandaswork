import pandas as pd
df=pd.read_csv("ipl_case_study\ipl_data.csv")
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
# matchid
df["match_id"].fillna(549,inplace=True)
print(df.isnull().sum())
# season
df["season"].fillna(df["season"].mode()[0],inplace=True)
print(df.isnull().sum())
# city
df["city"].fillna(df["city"].mode()[0],inplace=True)
print(df.isnull().sum())
# team 1
df["team1"].fillna("unknown", inplace=True)
print(df.isnull().sum())
# team2
df["team2"].fillna("unknown",inplace=True)
print(df.isnull().sum())
# winning team
df["winning_team"].fillna("unknown",inplace=True)
print(df.isnull().sum())
# player of the match
df["player_of_match"].fillna("unknown",inplace=True)
print(df.isnull().sum())
# venue
df["venue"].fillna(df["venue"].mode()[0],inplace=True)
print(df.isnull().sum())
# wickets
df["wickets"].fillna(df["wickets"].median(),inplace=True)
print(df.isnull().sum())
# run scored
run_round=round(df["runs_scored"].mean())
df["runs_scored"].fillna(run_round,inplace=True)
print(df.isnull().sum())
# analysis
# matches per season
print("matches per season",df["season"].value_counts)
# top match count season
print("top match count season",df["season"].value_counts().idxmax())
# total match won by each team
print(df["winning_team"].value_counts())
# per season avg run
print(df.groupby("season")["runs_scored"].mean())
# venue wise match count
print(df["venue"].value_counts())
# venue wise avg run
print(df.groupby('venue')['runs_scored'].mean())
# city wise
print(df["city"].value_counts())
# avg city wise
print(df.groupby("city")["runs_scored"].mean())
# who scored most runs winning team  
print(df.groupby("winning_team")["runs_scored"].mean().idxmax())
# top 3 venue
print(df["venue"].value_counts().head(3))