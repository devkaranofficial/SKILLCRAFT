import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

df = pd.read_csv("Practice_models/house_dataset.csv")


x = df[
    ["Area" ,"Bedrooms" , "Bathrooms"]
]
y = df["Price"]



x_train , x_test , y_train , y_test = train_test_split( x , y ,test_size=0.2 , random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

prediction = model.predict(x_test)
print("Prediction results:",prediction)
print("Actual Results:",y_test)

print("MAE:",mean_absolute_error(y_test,prediction))
print("MSE:",mean_squared_error(y_test,prediction))
print("R2 score:",r2_score(y_test,prediction))
print("Model coefficients:",model.coef_)
print("Model Intercept:",model.intercept_)