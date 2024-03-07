
# Import necessary libraries
import streamlit as st
import pandas as pd
import pyodbc

# Title of the page
st.title("Vodafone Churn Data")

 
@st.cache_resource(show_spinner='Connecting to Database......')
def initialize_connection():
    connection = pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets["SERVER"]
        +";DATABASE="
        + st.secrets["DATABASE"]
        +";UID="
        + st.secrets["UID"]
        +";PWD="
        + st.secrets["PWD"]
    )
    return connection
   
conn = initialize_connection()
 
def query_database(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        df = pd.DataFrame. from_records(data=rows, columns=[ column[0] for column in cur.description])
    return df
 
@st.cache_data()
def select_all_features():
    query = "SELECT * FROM LP2_Telco_churn_first_3000"
    df = query_database(query)
    return df
 
@st.cache_data()
def select_numeric_features():
    query = "SELECT * FROM LP2_Telco_churn_first_3000"
    df = query_database(query)
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df
 
if __name__ == "__main__":
    col1, col2 = st.columns(2)
 
    with col1:
        selected_option = st.selectbox("Select type of features", options=['All features', 'Numeric features'], key="selected_columns")
 
    with col2:
        pass
 
    if selected_option == "All features":
        data = select_all_features()
    elif selected_option == "Numeric features":
        data = select_numeric_features()



st.dataframe(data)
def load_dataset(file_path):
    df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
    return df
 
# Function to display dataset overview
def display_dataset_overview(data):
    st.subheader('Dataset Overview')
    st.write(data)
# Summary statistics
    st.subheader('Summary Statistics')
    st.write(data.describe())

st.title('Telco data')
 
# Add selectbox to choose dataset
selected_dataset = st.selectbox('Select Dataset', ['LP2_Telco_churn_first_3000', 'Telco-churn-second-2000.csv', 'LP2_Telco-churn-last-2000.csv'])
 
if selected_dataset == 'LP2_Telco_churn_first_3000':
    # Load data from the first dataset
    data = query_database("SELECT gender, tenure, Contract,Churn,SeniorCitizen, MonthlyCharges, TotalCharges FROM LP2_Telco_churn_first_3000")
else:
    # Load data from the selected file
    file_path = f"data/{selected_dataset}"
    data = load_dataset(file_path)

 # Display dataset overview and visualizations
display_dataset_overview(data)

 
