import pandas as pd
import numpy as np
import joblib
from sqlalchemy import create_engine

# Load model, preprocessor, dan label encoder (jika pakai)
model = joblib.load('model/random_forest.pkl')
preprocessor = joblib.load('model/preprocessor.pkl')

# Load data input
df_new = pd.read_csv('dataset/data_bersih.csv')
if 'Attrition' in df_new.columns:
    df_new = df_new.drop(columns=['Attrition'])

# Preprocess input
X_new = preprocessor.transform(df_new)

# Prediksi
y_pred = model.predict(X_new)

# Tambahkan hasil ke dataframe
df_new['PredictedAttrition'] = y_pred

# Mapping ke Yes/No
df_new['PredictedAttritionLabel'] = df_new['PredictedAttrition'].map({0: 'Yes', 1: 'No'})

# Daftar kolom yang di-log1p
skewed_cols = [
    'NumCompaniesWorked', 'MonthlyIncome', 'DistanceFromHome',
    'YearsInCurrentRole', 'YearsWithCurrManager', 'YearsAtCompany',
    'TotalWorkingYears', 'PercentSalaryHike', 'YearsSinceLastPromotion',
    'Age', 'JobLevel', 'StockOptionLevel'
]

# Inverse transform
for col in skewed_cols:
    if col in df_new.columns:
        df_new[col] = df_new[col].apply(np.expm1).round(0).astype(int)

# 1. Simpan hasil ke file CSV
df_new.to_csv('dataset/hasil_prediksi.csv', index=False)

print("Hasil prediksi telah disimpan ke 'hasil_prediksi.csv'")

# 2. Koneksi ke Supabase PostgreSQL
engine = create_engine(
    # 'postgresql://postgres:roots12345!kita@db.gxjbqjsfkmssgqedesbk.supabase.co:5432/postgres',
    # postgresql://postgres.gxjbqjsfkmssgqedesbk:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
    'postgresql://postgres.gxjbqjsfkmssgqedesbk:roots12345!kita@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres',
    connect_args={"sslmode": "require"}
)

# Simpan ke tabel
df_new.to_sql('hasil_prediksi', engine, if_exists='replace', index=False)
print("Data berhasil disimpan ke Supabase PostgreSQL.")

# 3. Simpan lokal ke file SQLite bernama hasil_prediksi.db
engine = create_engine('sqlite:///docker/database/hasil_prediksi.db')

df_new.to_sql('hasil_prediksi', engine, if_exists='replace', index=False)
print("Data berhasil disimpan ke file lokal hasil_prediksi.db.")