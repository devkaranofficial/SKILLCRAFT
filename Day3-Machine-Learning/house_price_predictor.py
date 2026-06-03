import numpy as np
from sklearn.linear_model import LinearRegression

house_area = np.array([1000, 1200, 1400, 1600, 1800, 2000])
house_price = np.array([20, 25, 30, 35, 40, 45])

x = house_area.reshape(-1,1)
y = house_price

model = LinearRegression()
model.fit(x,y)

new_house_area = np.array([[1500]])
prediction = model.predict(new_house_area)

print(f"The New House Price is {prediction[0]}Lakhs")