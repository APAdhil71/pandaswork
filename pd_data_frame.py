import pandas as pd
students={
    "name":["adhnan","adhil","arshiya","abshan","aahil"],
    "age":[21,21,18,25,24],
    "course":["ds","ds","ds","dj","dj"]

}
df=pd.DataFrame(students)
# print(df)
# print(df[1:2])
print(df[["name","age","course"]])