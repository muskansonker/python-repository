import streamlit as st
import pandas as pd
import numpy as np

# interactive visualization

import plotly.express as px
import plotly.graph_objects as go

# global variables
years = list(range(1980, 2014)) # list of years from 1980 to 2013
# Loading the data and  it for the sake of humanity
@st.cache_data
def load_dataset():
    df = pd.read_excel("dapp/canada.xlsx", sheet_name=1, skiprows=20, skipfooter=2)
    df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
    df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 
                       'RegName':'Region', 'DevName':'Status'}, inplace=True)
    df.set_index('Country', inplace=True)
    df['Total'] = df[years].sum(axis=1)
    return df
with st.spinner('Loading data...'):
    df = load_dataset()
    st.balloons()

# UI
#countries = df.index.tolist()
#sel_country = st.selectbox('Select a country', countries)
#st.info(f'You selected {sel_country}')
#
## KPI
#total_immigrants = df.loc[sel_country, 'Total']
#avg_immigrants = df.loc[sel_country, years].mean()
#st.subheader("Key Performance Indicators")
#c1, c2, c3 = st.columns(3)
#c1.metric("Total Immigrants", f'{total_immigrants} people', '👨‍👩‍👧‍👦')
#c2.metric('Avg. Immigrants/yr', f'{round(avg_immigrants)} people', '👨‍👩‍👧‍👦/Year')
#c3.metric("Total years", f'{len(years)} years', '📅')
#
#country_df =  df.loc[sel_country, years]
#fig = px.area(y=country_df, x=country_df.index, title=f'{sel_country} immigrants to Canada')
#fig2 = px.scatter(y=country_df, x=country_df.index, title=f'{sel_country}')
#
#c1, c2 = st.columns(2)
#c1.plotly_chart(fig, use_container_width=True)
#c2.plotly_chart(fig2, use_container_width=True)