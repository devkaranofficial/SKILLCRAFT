# Task 02 - Customer Segmentation using K-Means Clustering

## Overview

This project is part of my Machine Learning Internship at SkillCraft Technology.

The objective of this task is to perform Customer Segmentation using the K-Means Clustering algorithm. Customer segmentation helps businesses group customers based on similar purchasing behavior, enabling targeted marketing strategies and better customer engagement.

## Dataset

Dataset: Mall Customer Segmentation Data

The dataset contains customer information collected through membership cards, including:

* Customer ID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1-100)

For this project, Annual Income and Spending Score were used as features for clustering.

## Problem Statement

A supermarket mall wants to understand its customers better and identify distinct customer groups based on spending behavior and income. These insights can help the marketing team design personalized campaigns and improve business decisions.

## Concepts Learned

* Unsupervised Learning
* Customer Segmentation
* K-Means Clustering
* WCSS (Within Cluster Sum of Squares)
* Elbow Method
* Cluster Centroids
* Data Visualization
* Model Interpretation

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

## Project Workflow

### 1. Data Loading

The customer dataset was loaded using Pandas and relevant features were selected.

### 2. Feature Selection

The following features were used:

* Annual Income (k$)
* Spending Score (1-100)

### 3. Elbow Method

The Elbow Method was used to determine the optimal number of clusters by calculating WCSS values for different cluster counts.

### 4. K-Means Clustering

A K-Means model was trained using the optimal number of clusters identified from the Elbow Method.

### 5. Visualization

Customer groups and cluster centroids were visualized using scatter plots for better interpretation.

## Results

* Optimal Number of Clusters: 5
* Successfully segmented customers into 5 distinct groups.
* Visualized customer clusters and cluster centers.
* Identified customer segments based on income and spending behavior.

## Output Visualizations

### Elbow Method Graph

The Elbow Method graph was used to determine the optimal value of K.

File:

* elbow_method.png

### Customer Segmentation Graph

Visual representation of customer clusters and their centroids.

File:

* customer_clusters.png

## Key Learning Outcomes

Through this project, I gained hands-on experience with:

* Applying unsupervised machine learning algorithms
* Understanding customer segmentation techniques
* Using the Elbow Method for cluster selection
* Interpreting cluster centroids
* Visualizing machine learning results

## Author

Dev Karan Singh

GitHub: https://github.com/devkaranofficial

SkillCraft Technology - Machine Learning Internship
