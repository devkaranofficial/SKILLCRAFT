import numpy as np
from sklearn.linear_model import LinearRegression

house_size = np.array([1000 , 1200 , 1400 , 1600 , 1800 , 2000])
house_cost = np.array([20 , 25 , 30 , 35 , 40 , 45])

x = house_size.reshape(-1,1)
y = house_cost

model = LinearRegression()

model.fit(x,y)
new_size = np.array([[1500]])
prediction = model.predict(new_size)

print(f"The Cost will be {prediction}Lakhs")