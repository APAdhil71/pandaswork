import pandas as pd
data=[56,54,64,65,87,90,87,65,45,63]
series=pd.Series(data)
print(series)
# head()bottom 5 records
print(series.head())
# tail last 5 records
print(series.tail())
# shape
print(series.shape)