
# Import necessary libraries
import streamlit as st
import pandas as pd
import pyodbc

# Title of the page
st.title("Vodafone Churn Data")

def initialize_connection():
     connection = pyodbc.connect(
          "DRIVER={{SQL Server}};SERVER="
          +st.secrets['SERVER']
          +";DATABASE="
          +st.secrets['DATABASE']
          +";UID="
          +st.secrets['LP_project']
          +";PWD="
          +st.secrets['PWD']
     )
     return connection

conn = initialize_connection()

def query_database(query):
     with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

        df=pd.DataFrame.from_records(data=rows, columns=[column[0] for column in cur.description])

     return df
