import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

house_data = np.array([
    [1000,2,1],
    [1200,2,2],
    [1500,3,2],
    [1800,3,3],
    [2000,4,3],
    [2200,4,4],
    [2500,5,4]
])
house_price = np.array([
    20,
    25,
    35,
    45,
    55,
    65,
    80
])
x_train , x_test , y_train , y_test = train_test_split(house_data , house_price , test_size=0.2 , random_state=42)

model =LinearRegression()
model.fit(x_train,y_train)

prediction = model.predict(x_test)
print("Predicted Prices:",prediction    )
print("Actual Prices:",y_test)
print(model.score(x_train,y_train))

print("The MAE:",mean_absolute_error(y_test,prediction))
print("The MSE:",mean_squared_error(y_test,prediction))