import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt

st.markdown("This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files")

DATE_COLUMN = 'Date'
DATA_URL = ('SampleforWork4.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(190)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#st.subheader('Number of pickups by hour')
hist_values = data[['Date','Site']]
st.line_chart(hist_values)

# Some number in the range 0-11
site_to_filter = st.slider('Site', 0, 6, 10)
filtered_data = data[data['Site'] == site_to_filter]

st.write(filtered_data)


# Some number in the range 0-4
site2_to_filter = st.slider('Quarter', 0, 2, 5)
filtered_data = data[data['Site'] == site_to_filter]
filtered_data[['Zone','Site','Date','System']]


#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.(filtered_data)

#chart_data = filtered_data
filtered_again = filtered_data[(filtered_data.Date.dt.quarter.eq(site2_to_filter))][['Zone','Site','Date','System']]

st.markdown('Set as variable then st.write')
st.write(filtered_again)

st.markdown('Filtered Table')
#st.line_chart(filtered_data['Date'],filtered_data['System'])
st.write(filtered_data[(filtered_data.Date.dt.quarter.eq(site2_to_filter))][['Zone','Site','Date','System']])

st.markdown('Line Chart')                                                                             
basicc_chart = (filtered_data[(filtered_data.Date.dt.quarter.eq(site2_to_filter))][['Site','Date','System']].plot(x='Date', y='System'))

st.markdown('Second attempt at filtered line chart')

filter_data = basicc_chart.set_index('Date')['Date','Site','System']
st.line_chart(filter_data)

st.markdown("Third time's a charm? Nah")


# Basic Altair line chart where it picks automatically the colors for the lines
basic_chart = alt.Chart(pd.basicc_chart).mark_line().encode(
    x=['Date'],
    y=['System'],
    color=['Site'],
    # legend=alt.Legend(title='Animals by year')
)

st.altair_chart(basic_chart)


st.markdown('Picture and Title')

st.title('Proof of Concept Data App')
title_image = Image.open("AppTitle.jpg")
st.image(title_image)

#From music app file 
stats_df = load_data("SampleforWork4.csv")
color_map_df = load_data("color_map_df.csv")
sorted_site = stats_df.groupby('Site')['System'].count().sort_values(ascending=False).index
#summary_poster(sorted_site, color_map_df)


st.markdown("### **Select Site:**")
select_site = []
select_site.append(st.selectbox('', sorted_site))

#Filter df based on selection
site_df = stats_df[stats_df['Site'].isin(select_site)]


st.markdown("This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files")
st.markdown("Made it to the end.")
