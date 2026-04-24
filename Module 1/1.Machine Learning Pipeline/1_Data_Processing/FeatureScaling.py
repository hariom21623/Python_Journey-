# ==========================================
# COMPLETE FEATURE SCALING PIPELINE
# ==========================================

import pandas as pd
import numpy as np

# Sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# -------------------------------
# 1. Load Dataset
# -------------------------------

df = pd.read_csv("C:/Users/Hariom/Desktop/Python/Module 1/1.Machine Learning Pipeline/1_Data_Processing/data.csv")

print("🔹 Original Data:")
print(df.head())

# -------------------------------
# 2. Handle Missing Values
# -------------------------------

# Numerical columns
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Categorical columns
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -------------------------------
# 3. Encode Categorical Data
# -------------------------------

df = pd.get_dummies(df, drop_first=True)

print("\n🔹 Data After Encoding:")
print(df.head())

# -------------------------------
# 4. Split Features & Target
# -------------------------------

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# -------------------------------
# 5. Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 6. Feature Scaling (Standardization)
# -------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)  # fit + transform
X_test_scaled = scaler.transform(X_test)        # only transform

print("\n🔹 Scaled Training Data (StandardScaler):")
print(X_train_scaled[:5])

# -------------------------------
# 7. Feature Scaling (Min-Max)
# -------------------------------

minmax = MinMaxScaler()

X_train_minmax = minmax.fit_transform(X_train)
X_test_minmax = minmax.transform(X_test)

print("\n🔹 Scaled Training Data (MinMaxScaler):")
print(X_train_minmax[:5])

# -------------------------------
# 8. Convert Back to DataFrame (Optional)
# -------------------------------

X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X.columns)
X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X.columns)

# -------------------------------
# 9. Save Output Files
# -------------------------------

X_train_scaled_df.to_csv("X_train_scaled.csv", index=False)
X_test_scaled_df.to_csv("X_test_scaled.csv", index=False)

print("\n✅ Feature Scaling Completed Successfully!")
print("📁 Files saved: X_train_scaled.csv, X_test_scaled.csv")