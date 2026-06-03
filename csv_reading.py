import pandas as pd

# df = pd.read_csv("student_data.csv")
# print(df)

df = pd.read_csv("student.csv")

# print("Complete Dataset")
# print(df)

# print(f"First Rows\n{df.head()}")

# print(f"last rows\n{df.tail()}")
# print(f"(Rows,Colums)\n{df.shape}")
# print(f"Colums{df.columns}")
print(df.info() ,"\n",df.describe() )