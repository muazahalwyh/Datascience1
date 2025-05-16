from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
import plotly.express as px

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

# Construct connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
try:
    engine = create_engine(DATABASE_URL)
    # Test the connection
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")

    
# --- Streamlit App ---
st.title(" Mu'azah Al'Adawiyah - Dashboard Analisis Employee Attrition")

# Query to read data
@st.cache_data(ttl=300)
def load_data():
    query = "SELECT * FROM hasil_prediksi;"
    df = pd.read_sql(query, engine)
    return df

df = load_data()

# Sidebar - Filter Section
st.sidebar.header(" Filter Data")

# Usia
age_filter = st.sidebar.slider(
    "Pilih Rentang Usia",
    int(df['Age'].min()),
    int(df['Age'].max()),
    (int(df['Age'].min()), int(df['Age'].max()))
)

# Departemen - hanya satu pilihan
department = st.sidebar.selectbox("Pilih Departemen", options=df['Department'].unique())

# Job Role - hanya satu pilihan, yang tersedia berdasarkan departemen
jobroles_filtered = df[df['Department'] == department]['JobRole'].unique()
jobrole = st.sidebar.selectbox("Pilih Job Role", options=jobroles_filtered)

# Attrition
attrition = st.sidebar.selectbox("Prediksi Attrition", options=["All"] + list(df['PredictedAttritionLabel'].unique()))

# Filter data berdasarkan semua input
filtered_df = df[
    (df['Age'] >= age_filter[0]) &
    (df['Age'] <= age_filter[1]) &
    (df['Department'] == department) &
    (df['JobRole'] == jobrole)
]

if attrition != "All":
    filtered_df = filtered_df[filtered_df['PredictedAttritionLabel'] == attrition]

# Tampilkan tabel hasil filter
st.subheader(" Data Karyawan Hasil Filter")
st.dataframe(filtered_df)

# Visualisasi distribusi usia berdasarkan attrition
st.subheader(" Distribusi Usia Berdasarkan Prediksi Attrition")
fig = px.histogram(filtered_df, x="Age", color="PredictedAttritionLabel", barmode="overlay")
st.plotly_chart(fig)

# Employee-specific detail
st.sidebar.subheader(" Lihat Detail Karyawan")

if not filtered_df.empty:
    employee_ids = filtered_df['EmployeeId'].unique()
    selected_id = st.sidebar.selectbox("Pilih Employee ID", sorted(employee_ids))

    selected_data = filtered_df[filtered_df['EmployeeId'] == selected_id]

    st.subheader(" Detail Karyawan Terpilih")
    st.write(selected_data.drop(columns=["PredictedAttrition"]))

    label = selected_data['PredictedAttritionLabel'].values[0]
    if label == "Yes":
        st.error(f" Karyawan dengan ID {selected_id} diprediksi akan **Resign**.")
    else:
        st.success(f" Karyawan dengan ID {selected_id} diprediksi akan **Bertahan**.")
else:
    st.warning("Tidak ada data karyawan sesuai dengan filter.")
