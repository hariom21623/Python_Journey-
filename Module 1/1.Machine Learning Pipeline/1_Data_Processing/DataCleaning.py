# ================================
# DATA CLEANING COMPLETE PIPELINE
# ================================

import pandas as pd
import numpy as np

# 1. Load Dataset
df = pd.read_csv("C:/Users/Hariom/Desktop/Python/Module 1/1.Machine Learning Pipeline/1_Data_Processing/data.csv")
print(df.head())

print("🔹 Original Data:")
print(df.head())
print("\nShape:", df.shape)

# -------------------------------
# 2. Handle Missing Values
# -------------------------------

print("\n🔹 Missing Values Before:")
print(df.isnull().sum())

# Fill numerical columns with mean
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\n🔹 Missing Values After:")
print(df.isnull().sum())

# -------------------------------
# 3. Remove Duplicates
# -------------------------------

print("\n🔹 Duplicate Rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# -------------------------------
# 4. Fix Text Data
# -------------------------------

for col in cat_cols:
    df[col] = df[col].str.lower().str.strip()

# -------------------------------
# 5. Convert Data Types
# -------------------------------

# Example: ensure Age is integer
if 'Age' in df.columns:
    df['Age'] = df['Age'].astype(int)

# -------------------------------
# 6. Handle Outliers (IQR Method)
# -------------------------------

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

# -------------------------------
# 7. Final Output
# -------------------------------

print("\n🔹 Cleaned Data:")
print(df.head())
print("\nShape after cleaning:", df.shape)

# -------------------------------
# 8. Save Cleaned Data
# -------------------------------

df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Data Cleaning Completed & Saved as cleaned_data.csv")