import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
IMG_SIZE = 64
#Creating a function which will process the image into required size and format
def image_processor(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    resized_image = cv2.resize(image ,(IMG_SIZE,IMG_SIZE))
    gray_image = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
    flattened_image = gray_image.flatten()
    return flattened_image #These features of the image would be used to classify

#Accesing images stores in the folder
folder_name = "training_data"
files = os.listdir(folder_name)

#Creating Lists to store features and Attributes
x = []#Features
y = []#Attributes

#Loop to access each file in the folder
for file in files:
    if 'cat' in file.lower():
        path = folder_name + '/' + file
        features = image_processor(path)
        if features is not None:
            x.append(features)
            y.append(0)
    elif 'dog' in file.lower():
        path = folder_name + '/' + file
        features = image_processor(path)
        if features is not None:
            x.append(features)
            y.append(1)
#Converting the Lists into Numpy Array
X = np.array(x)
Y = np.array(y)


#Splitting The Data into Training and Testing
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size=0.2 , random_state=43)

#Dataset
print(f"Total Images: {len(X)}")
print(f"Cats: {np.sum(Y == 0)}")
print(f"Dogs: {np.sum(Y == 1)}")

print(f"X Shape: {X.shape}")
print(f"Y Shape: {Y.shape}")

print(f"X_train Shape: {X_train.shape}")
print(f"X_test Shape: {X_test.shape}")


#model training
model = SVC()
model.fit(X_train,Y_train)

#Making Predictions
model_predictions = model.predict(X_test)

#Printing first 5 Output and comparing them
for i in range (5):
    
    if 0 == model_predictions[i]:
        predict = "Cat"
    elif 1 == model_predictions[i]:
        predict = "Dog"
    if 0 == Y_test[i]:
        actual = "Cat"
    elif 1 == Y_test[i]:
        actual = "Dog"
    print(f"Prediction:{predict} | Actual:{actual}")

#Printing Model efficiency
print(f"Accuracy Score:{accuracy_score(Y_test,model_predictions)}") 
print("Confusion Matrix:\n",confusion_matrix(Y_test,model_predictions))
print("Classification report:",classification_report(Y_test,model_predictions))