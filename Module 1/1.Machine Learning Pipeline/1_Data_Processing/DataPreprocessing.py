# =====================================
# DATA PREPROCESSING COMPLETE PIPELINE
# =====================================

import pandas as pd
import numpy as np

# Sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# -------------------------------
# 1. Load Dataset
# -------------------------------

df = pd.read_csv("data.csv")

print("🔹 Original Data:")
print(df.head())

# -------------------------------
# 2. Handle Missing Values
# -------------------------------

# Fill numerical columns with mean
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -------------------------------
# 3. Encode Categorical Data
# -------------------------------

le = LabelEncoder()

for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# -------------------------------
# 4. Split Features & Target
# -------------------------------

# Change 'Purchased' to your target column if different
X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# -------------------------------
# 5. Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 6. Feature Scaling
# -------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------
# 7. Final Output
# -------------------------------

print("\n🔹 Training Data Shape:", X_train.shape)
print("🔹 Testing Data Shape:", X_test.shape)

print("\n✅ Data Preprocessing Completed Successfully!")