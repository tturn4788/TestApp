import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt
import plotly.express as px


#create a canvas for each item
interactive =  st.beta_container()


st.markdown('Picture and Title')

st.title('Proof of Concept Data App')
title_image = Image.open("AppTitle.jpg")
st.image(title_image)
st.markdown("This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files")

DATE_COLUMN = 'Date'
DATA_URL = ('SampleforWork4.csv')


data = pd.read_csv('SampleforWork4.csv',parse_dates=['Date'])
#data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
data.dropna()
#Variables for later
SITES = data.Site.unique()
SYSTEMS = ['System','System1','System2']

interactive = st.beta_container()
    

#data_load_state = st.text('Loading data...')

#data_load_state.text("Done! (using st.cache)")

#ts = pd.Series(data[data['Site']==1]['System'].values, index=pd.DataFrame(data.Date[1:20]))


#ts = ts.cumsum()

#st.line_chart(ts)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

                                   
#st.subheader('Number of pickups by hour')
#hist_values = data[['Site','Date','System']]
#hist_values = hist_values.set_index('Date', inplace=True)
'hist_values.groupby("Site")["System"].plot(legend=True)'




col1, col2 = st.beta_columns(2)
col_1 = st.beta_columns(1)
# Mask to filter dataframe
with st.beta_container():
    with col1:
        'Create a custom table:'
        COLUMNS = data.columns
        COLUMNS_SELECTED = st.multiselect('Select column(s)', COLUMNS)
        mask_site = data[COLUMNS_SELECTED]
        st.write(mask_site)


#with col2:
    #go.line(mask_site)
'mask_site'
#data_mask = data[mask_site]
#col1.st.write(data_mask)
#col2.st.line_chart(mask_site)
'data mask'

SITES_SELECTED = st.multiselect('Select site(s)', SITES)
SYSTEMS_SELECTED = st.multiselect('Select system(s)', SYSTEMS)

df = data[['Site','System']]
#df.set_index('Date', inplace=True)

fig = px.line(df, y='System')
fig.show()
fig = px.line(data, "System")
fig.show()










hist_values = data[['Site','System']]
#hist_values = hist_values.set_index('Date', inplace=True)


    #hist_values.plot(legend=True)

'st.line_chart(hist_values)'
st.line_chart(hist_values)

siting = st.slider('Site', 1, 10)

with st.beta_container():
    with col1:
        'Before'
        subbed = data[(data.Site.eq(siting))]

    with col2:
        "st.line_chart(subbed[['Date','System']])"
        st.line_chart(subbed['System'])

with st.beta_container():
    with col1:
        'st.write(subbed)'
        st.write(subbed)

    with col2:
        'st.line_chart(subbed)'
        st.line_chart(subbed)

with st.beta_container():
    with col1:



        'After'
        #st.write(subbed_twice)

    with col2:
        'And even more after'
        data.groupby(['Zone','Site'])[['Site','System']].mean().plot.scatter(x='Site',y = 'System')


with st.beta_container():
    # Some number in the range 0-11
    site_to_filter = st.slider('Site', 0, 6, 10)
    filtered_data = data[data['Site'] == site_to_filter]

    st.write(filtered_data)

with st.beta_container():
    # Some number in the range 0-4
    site2_to_filter = st.slider('Site to view:', 1, 11, 5)
    filtered_data = data[data['Site'] == site_to_filter]
    st.write(filtered_data)


st.subheader('Map of all pickups at:')
#st.(filtered_data)

#chart_data = filtered_data
#filtered_data[ = filtered_data[(filtered_data.Date.dt.quarter is (site2_to_filter))]
with interactive:
    c0 = data.index.to_series().between('2021-01-01', '2021-01-10')
    #c1 = df['column A'] == 'Done'
    #c2 = df['column B'] < 3.14

    df[c0]

df1=data.pivot_table(columns=['Zone','Site'], values='System')
df1.reset_index()
#to obtain the 1st column content
df1.reset_index().iloc[:,[0]]
#to obtain the 2rd column content
df1.reset_index().iloc[:,[1]]

'Pivot Table'
st.write(df1)
   
             
'Probably nothing.'             
st.write(data.pivot(columns='Site', values='System'))




st.markdown('This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files.')
st.markdown("Made it to the end.")
