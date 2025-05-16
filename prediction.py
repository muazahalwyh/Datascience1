import pandas as pd
import numpy as np
import joblib
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

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
# Construct connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Simpan ke tabel
df_new.to_sql('hasil_prediksi', engine, if_exists='replace', index=False)
print("Data berhasil disimpan ke Supabase PostgreSQL.")

# 3. Simpan lokal ke file SQLite bernama hasil_prediksi.db
engine = create_engine('sqlite:///docker/database/hasil_prediksi.db')

df_new.to_sql('hasil_prediksi', engine, if_exists='replace', index=False)
print("Data berhasil disimpan ke file lokal hasil_prediksi.db.")