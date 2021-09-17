import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN])
st.bar_chart(hist_values)

# Some number in the range 0-11
site_to_filter = st.slider('Site', 0, 6, 10)
filtered_data = data[data['Site'] == site_to_filter]

st.write(filtered_data)


# Some number in the range 0-11
site2_to_filter = st.slider('Quarter', 0, 2, 5)
filtered_data = data[data['Site'] == site2_to_filter]
filtered_data[['Zone','Site','System']]


#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.(filtered_data)

chart_data = filtered_data


st.line_chart(filtered_data['Date'],filtered_data['System'])


st.markdown('Second attempt at filtered line chart')
st.line_chart(data[(filtered_data.Date.dt.quarter.eq(site2_to_filter)][['Date','System']].plot(x='Date', y='System'))




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
