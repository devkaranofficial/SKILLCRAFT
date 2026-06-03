import numpy as np
from sklearn.linear_model import LinearRegression

hours = np.array([1,2,3,4,5,6,7,8])
marks =np.array([20,30,40,50,60,70,80,90])

x = hours.reshape(-1,1)
y = marks

model = LinearRegression()
model.fit(x,y)

new_hour = np.array([[9]])
prediction = model.predict(new_hour)

print(f"Marks Obtained By Student Who Studied {new_hour[0]} is {prediction[0]}")