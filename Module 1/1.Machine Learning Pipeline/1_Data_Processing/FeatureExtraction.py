# ==========================================
# FEATURE EXTRACTION COMPLETE PIPELINE
# ==========================================

import pandas as pd
import numpy as np

# Sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

# -------------------------------
# 1. Load Dataset
# -------------------------------

df = pd.read_csv("C:/Users/Hariom/Desktop/Python/Module 1/1.Machine Learning Pipeline/1_Data_Processing/data.csv")


print("🔹 Original Data:")
print(df.head())

# -------------------------------
# 2. Basic Cleaning (minimal)
# -------------------------------

# Fill numeric
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical
cat_cols = df.select_dtypes(include=['object', 'string']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -------------------------------
# 3. Separate Features & Target
# -------------------------------

# Change 'Purchased' if needed
X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# -------------------------------
# 4. One-Hot Encoding (Categorical)
# -------------------------------

X = pd.get_dummies(X, drop_first=True)

# -------------------------------
# 5. Feature Scaling
# -------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------
# 6. Polynomial Features (New Features)
# -------------------------------

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X_scaled)

print("\n🔹 Shape after Polynomial Features:", X_poly.shape)

# -------------------------------
# 7. PCA (Dimensionality Reduction)
# -------------------------------

pca = PCA(n_components=2)   # reduce to 2 features
X_pca = pca.fit_transform(X_poly)

print("🔹 Shape after PCA:", X_pca.shape)

# -------------------------------
# 8. TEXT FEATURE EXTRACTION (Optional)
# -------------------------------

# Example text column (create dummy if not present)
df['Text'] = [
    "good product", "bad quality", "average item",
    "excellent", "poor", "nice", "bad", "great",
    "ok", "good", "fine"
]

tfidf = TfidfVectorizer()
X_text = tfidf.fit_transform(df['Text'])

print("🔹 TF-IDF Shape:", X_text.shape)

# -------------------------------
# 9. Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.2, random_state=42
)

# -------------------------------
# 10. Save Extracted Features
# -------------------------------

# Convert PCA output to DataFrame
X_pca_df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])

X_pca_df.to_csv("extracted_features.csv", index=False)

print("\n✅ Feature Extraction Completed!")
print("📁 File saved: extracted_features.csv")