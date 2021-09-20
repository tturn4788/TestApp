import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt
import plotly.express as px


st.set_page_config(layout="wide")
#create a canvas for each item



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
#Variables for later

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


fig = go.Figure()
  


fig.add_trace(go.Scatter(x = data.index, y = data.System, mode = 'lines'))
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.beta_columns(2)
col_1 = st.beta_columns(1)
# Mask to filter dataframe
with st.beta_container():
    with col1:
        'Create a custom table:'
        SITES = data.Site.unique()
        SYSTEMS = ['System','System1','System2']
        SITES_SELECTED = st.multiselect('Select site(s)', SITES)
        SYSTEMS_SELECTED = st.multiselect('Select system(s)', SYSTEMS)
        COLUMNS = data.columns
        COLUMNS_SELECTED = st.multiselect('Select column(s)', COLUMNS)
        
        #d1 = data['Site']==SITES_SELECTED
        d2 = data[COLUMNS_SELECTED]
        d3 = data[SYSTEMS_SELECTED]
        #site_df = stats_df[stats_df['Site'].isin(select_site)
        #mask_site = data
        #mask_site = data[data[[d2]]]
        #st.write(mask_site[[mask_site.columns.isin(d2)]])


#with col2:
    #go.line(mask_site)
'mask_site'
#data_mask = data[mask_site]
#col1.st.write(data_mask)
#col2.st.line_chart(mask_site)
'data mask'

#df.set_index('Date', inplace=True)

#fig = px.line(df, y='System')
#fig.show()
#fig = px.line(data, "System")
#fig.show()










hist_values = data.groupby(['Zone','Site'])[['System']]
#hist_values = hist_values.set_index('Date', inplace=True)

'st.pyplot'
#st.pyplot(data.groupby(['Zone','Site']).plot(y='System', legend=True))
    #hist_values.plot(legend=True)

'st.line_chart(hist_values)'
st.line_chart(data.groupby(['Zone','Site'])[['System']])

siting = st.slider('Site', 1, 10)

with st.beta_container():
    'Before'
    subbed = data[(data.Site.eq(siting))]
    'st.line_chart(subbed)'
    st.line_chart(subbed[['System','System1','System2']])

    "st.line_chart(subbed[['Date','System']])"
    st.line_chart(subbed['System'])






with st.beta_container():
    
    'After'
    #st.write(subbed_twice)

    df3 = data.groupby(['Zone','Site'])
    df3[['Site','System']].plot(kind='scatter',x='Site',y = 'System')


with st.beta_container():
    # Some number in the range 0-11
    site_to_filter = st.slider('Site', 0, 6, 10)
    filtered_data = data[data['Site'] == site_to_filter]

    st.write(filtered_data)

with st.beta_container():
    # Some number in the range 0-4
    site2_to_filter = st.slider('Site to view:', 1, 11, 5)
    filtered_data = data[data['Site'] == site_to_filter]
    st.write(filtered_data.style.background_gradient(cmap='Greens'))


st.subheader('Map of all pickups at:')
#st.(filtered_data)

#chart_data = filtered_data
#filtered_data[ = filtered_data[(filtered_data.Date.dt.quarter is (site2_to_filter))]
with interactive:
    c0 = data.index.to_series().between('2021-01-01', '2021-01-10')
    #c1 = df['column A'] == 'Done'
    #c2 = df['column B'] < 3.14

    st.write(data[c0])

df1=data.pivot(columns=['Zone','Site'], values='System')
#st.write(data.pivot(columns=['Zone','Site'], values='System'))
#df1.reset_index()
#to obtain the 1st column content
#df1.reset_index().iloc[:,[0]]
#to obtain the 2rd column content
#df1.reset_index().iloc[:,[1]]

'Pivot Table'
df1.style.background_gradient(cmap='Greens')
st.write(df1.style.background_gradient(cmap='RdYlGn_r'))
   
             
'Probably nothing.'



data['Quarter'] = data.index.quarter.values
grouped = data.groupby(['Zone','Site','Quarter'])
#Sampled monthly
grouped.resample('Q')[['System']].mean().plot()


st.markdown('This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files.')
st.markdown("Made it to the end.")
