# 🔹 🔄 ML Workflow (Step-by-Step)
#1. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2. Load Dataset
df = pd.read_csv("C:/Users/Hariom/Desktop/Python/Module 1/1.Machine Learning Pipeline/1_Data_Processing/data.csv")
print(df.head())

#3. Basic Data Exploration
print(df.shape)        # rows, columns
print(df.info())       # data types
print(df.describe())   # statistical summary

#4. Handling Missing Values
'''➤ Check missing values'''
print(df.isnull().sum())
'''➤ Fill missing values'''
df['Age'].fillna(df['Age'].mean(), inplace=True)  # numerical
df['City'].fillna(df['City'].mode()[0], inplace=True)  # categorical
'''➤ Drop missing values (if needed)'''
df.dropna(inplace=True)

#5. Encoding Categorical Data
'''➤ Label Encoding'''

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

'''➤ One-Hot Encoding'''
df = pd.get_dummies(df, columns=['City'])

#6. Feature Scaling

'''➤ Standardization (Z-score scaling)'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

'''➤ Normalization (Min-Max scaling)'''
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

#7. Splitting Dataset
from sklearn.model_selection import train_test_split

X = df.drop('Target', axis=1)
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#8. Handling Outliers
# Using IQR method

Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Salary'] >= Q1 - 1.5 * IQR) & (df['Salary'] <= Q3 + 1.5 * IQR)]

#9. Feature Selection
# Correlation heatmap

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True)
plt.show()