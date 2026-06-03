import numpy as np
from sklearn.linear_model import LinearRegression

house_data = np.array([[1000,2,1] , [1200,2,2] , [1500,3,2]])
house_price = np.array([ 20,25, 35])

x = house_data
y = house_price
# print(x.shape)

model = LinearRegression()
model.fit(x,y)

new_house_data = np.array([[1700, 3, 2]])
prediction = model.predict(new_house_data)
# print(f"The price of new house would be {prediction[0]:.3f}")



#model 2
cottage_data = np.array([
    [1000,2,1],
    [1200,2,2],
    [1500,3,2],
    [1800,3,3],
    [2000,4,3],
    [2200,4,4],
    [2500,5,4]
])#(area,bedrooms,bathrooms)
cottage_price = np.array([
    20,
    25,
    35,
    45,
    55,
    65,
    80])

x = cottage_data
y = cottage_price

model = LinearRegression()
model.fit(x,y)

new_cottage_data = np.array([[1700, 3, 2]])
prediction = model.predict(new_cottage_data)

print("The model Coefficient:",model.coef_)
print("The modelIntercepts:",model.intercept_)

print(f"The price of New Cottage Would be:{prediction[0]:.3f}Lakhs")

print("Model Score:",model.score(x,y))