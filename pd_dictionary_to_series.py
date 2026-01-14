import pandas as pd
student_total={"s1":450,"s2":475,"s3":450,"s4":500}
series=pd.Series(student_total)
# print(series["s3"])
# agg function
# max()
# min()
# mean()
# sum()
print("total",series.sum())
print("max",series.max())
print("mean",series.mean())