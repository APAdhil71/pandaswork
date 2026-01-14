import pandas as pd
employee={"emp1":1,"emp2":2,"emp3":3,"emp4":4,"emp5":6}
series=pd.Series(employee)
print(series["emp3"])