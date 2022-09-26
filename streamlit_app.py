import gspread
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def get_data():
    gc = gspread.service_account(filename="service_account.json") # from google cloud
    wks = gc.open("Tsla").sheet1 # Open a sheet from a spreadsheet //get_worksheet(0), worksheet("name")

    get_values_c1 = wks.col_values(1) # get all values from a column & for rows //row_values(1)
    get_values_c2 = wks.col_values(2)

    df = pd.DataFrame({'Date' : get_values_c1, "Closing_Price" : get_values_c2})
    df = df.drop([0])
    
    df["Closing_Price"] = df["Closing_Price"].str.replace(',', '.').astype(float)
   
    print(df.dtypes)
    print(df)
    return df

st.title('Tesla Stock')
st.text('This is a test version for tesla stock')

def plot_data():
    df = get_data()
    fig = px.line(data_frame = df, 
                x = 'Date' ,
                y = 'Closing_Price')
    st.plotly_chart(fig)
    
plot_data()

#def read_data():
#    gc = gspread.service_account(filename="service_account.json")
#    sh = gc.open("Tsla").get_worksheet(0) # index 0 = sheet1, index 1 = sheet2, etc.
#    df = pd.DataFrame(sh.get_all_records())
#    return df
#
#def plot_data():
#    df = read_data()
#    df['price'] = df['price'].astype(float)
#
#    fig = px.line(data_frame = df, 
#                x = 'date' ,
#                y = 'price')
#    st.plotly_chart(fig)
#    
#plot_data()



