import pandas as pd
import numpy as np

data = {"Name":["Dev Karan Singh" , "Raj Karan Singh" , "Satvinder Singh"] , "Age":[19 , 23 , 50]}
df = pd.DataFrame(data)
print(df)

print(df.columns)
print(df.info())


# Task 1
data = { "Name":["Sam" , "Alex" , "Ryan"] , "Marks":[85 , 90 , 78]}
df = pd.DataFrame(data)
# print(df)
# print(f"Highest marks:{np.max(data["Marks"])} ")
# print(f"Lowest Marks:{np.min(data["Marks"])}")
# print(f"Average marks:{np.mean(data["Marks"])}")
print(df["Marks"])
print(df.shape)
print(df.describe())

#Mini Project
employee_data = {"name":["John" , "Emma" , "Mike" , "Sarah"] , "Salary":[30000 , 45000 , 40000 ,50000]}
df = pd.DataFrame(employee_data)
print(df)
print(f"Highest Salary is {df["Salary"].max()}")
print(f"Lowest Salary is {df["Salary"].min()}")
print(f"Average salary is {df["Salary"].mean()}")
print(df.shape)
print(df.info())