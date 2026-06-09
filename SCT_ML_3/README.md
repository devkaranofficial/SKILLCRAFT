# 🐱🐶 Cats vs Dogs Image Classification using SVM

## SkillCraft Technology - Machine Learning Internship Task 03

### Project Overview

This project was completed as part of the **SkillCraft Technology Machine Learning Internship Program**.

The objective of this task is to build an image classification model capable of distinguishing between **cats and dogs** using traditional Machine Learning techniques. The project utilizes **OpenCV** for image preprocessing and **Support Vector Machine (SVM)** for classification.

Instead of using deep learning, images are converted into numerical feature vectors and classified using a supervised machine learning algorithm.

---

## Objectives

* Understand image preprocessing techniques
* Learn how images are represented as numerical data
* Build a machine learning dataset from image files
* Train an SVM classifier
* Evaluate classification performance using multiple metrics
* Gain practical experience with computer vision and machine learning

---

## Technologies Used

* Python
* OpenCV
* NumPy
* Scikit-learn

---

## Concepts Learned

* Image Reading using `cv2.imread()`
* Image Resizing
* Grayscale Conversion
* Pixel Values
* Feature Extraction
* Flattening Images
* Feature Vectors
* Labels and Target Variables
* Dataset Creation
* Folder Traversal using `os.listdir()`
* Train-Test Split
* Support Vector Machine (SVM)
* Model Training
* Predictions
* Accuracy Score
* Confusion Matrix
* Classification Report

---

## Dataset Information

Dataset: Cats vs Dogs Dataset

Total Images: **25,000**

* Cats: 12,500
* Dogs: 12,500

Image Size After Processing:

```text
64 × 64 pixels
```

Feature Vector Size:

```text
4096 features per image
```

---

## Project Workflow

### 1. Image Preprocessing

Each image undergoes the following preprocessing steps:

* Read image using OpenCV
* Resize image to 64 × 64 pixels
* Convert image to grayscale
* Flatten image into a one-dimensional feature vector

Example:

```text
64 × 64
↓
Grayscale
↓
Flatten
↓
4096 Features
```

---

### 2. Dataset Creation

Features (X):

* Flattened pixel values from processed images

Labels (Y):

* Cat = 0
* Dog = 1

---

### 3. Train-Test Split

The dataset is divided into training and testing sets:

* Training Data: 80%
* Testing Data: 20%

Parameters:

```python
test_size = 0.2
random_state = 43
```

Dataset Shapes:

```text
X Shape: (25000, 4096)
Y Shape: (25000,)

X_train Shape: (20000, 4096)
X_test Shape: (5000, 4096)
```

---

### 4. Model Training

A Support Vector Machine (SVM) classifier is used for training.

```python
from sklearn.svm import SVC

model = SVC()
model.fit(X_train, Y_train)
```

---

### 5. Model Evaluation

The model performance is evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## Results

### Accuracy Score

```text
65.96%
```

### Confusion Matrix

```text
[[1631  918]
 [ 784 1667]]
```

### Classification Report

```text
              precision    recall  f1-score   support

       0         0.68      0.64      0.66      2549
       1         0.64      0.68      0.66      2451

accuracy                             0.66      5000
macro avg      0.66      0.66      0.66      5000
weighted avg   0.66      0.66      0.66      5000
```

---

## Sample Predictions

```text
Prediction: Dog | Actual: Cat
Prediction: Cat | Actual: Cat
Prediction: Cat | Actual: Cat
Prediction: Cat | Actual: Cat
Prediction: Cat | Actual: Cat
```

---

## Key Learnings

Through this project, I learned:

* How image data is represented numerically
* How image preprocessing impacts model performance
* How feature vectors are created from images
* How Support Vector Machines classify data
* How to evaluate classification models using multiple metrics
* The importance of train-test splitting
* Practical implementation of computer vision concepts

---

## Future Improvements

* Normalize pixel values
* Increase image preprocessing techniques
* Use Histogram of Oriented Gradients (HOG) features
* Experiment with different SVM kernels
* Apply Hyperparameter Tuning
* Implement Convolutional Neural Networks (CNNs)
* Improve classification accuracy using Deep Learning

---
## Dataset

The Cats vs Dogs dataset was used for this project.

Due to GitHub storage limitations, the dataset is not included in this repository.

Dataset Source:
https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset


## Repository Structure

```text
Task 03/
│
├── Support_Vector_Machine.py
├── README.md
└── Output Screenshot
```

---

## Conclusion

This project demonstrates the complete machine learning workflow for image classification using traditional computer vision techniques and Support Vector Machines. It provides hands-on experience with image preprocessing, feature engineering, model training, and performance evaluation.

---

## Author

**Dev Karan Singh**

Machine Learning Intern – SkillCraft Technology

GitHub: https://github.com/devkaranofficial
