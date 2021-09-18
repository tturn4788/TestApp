import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt

st.markdown('Picture and Title')

st.title('Proof of Concept Data App')
title_image = Image.open("AppTitle.jpg")
st.image(title_image)
st.markdown("This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files")

DATE_COLUMN = 'Date'
DATA_URL = ('SampleforWork4.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#data_load_state = st.text('Loading data...')
data = load_data(190)
#data_load_state.text("Done! (using st.cache)")

ts = pd.Series(data[data['Site']==1]['System'].values, index=pd.DataFrame(data.Date[1:20]))

#ts = ts.cumsum()

st.line_chart(ts)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#st.subheader('Number of pickups by hour')
hist_values = data[['Site','Date','System']]
st.line_chart(hist_values)

siting = st.slider('Site', 1, 5, 10)
'Before'
subbed = data[(data.Site.eq(siting))]
st.line_chart(subbed[['Date','System']])
subbed.plot()


st.line_chart(subbed)
st.write(subbed)
'After'
#st.write(subbed_twice)

'And even more after'
data[data.Date.dt.quarter.eq(1)].groupby('Zone').plot.scatter(x='Date',y = 'System')


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
basically_chart = filtered_data[(filtered_data.Date.dt.quarter.eq(site2_to_filter))]
basicc_chart = basically_chart[['Site','Date','System']].plot(x='Date', y='System', subplots=True)
st.write(basicc_chart)
st.markdown('Second attempt at filtered line chart')

'Heres the problem.'


#filter_data = basicc_chart[['Date','Site','System']]
#filter_data.groupby('Site').plot(x='Date', y = 'System')

st.markdown("Third time's a charm? Nah")


# Basic Altair line chart where it picks automatically the colors for the lines
#alt.Chart(basicc_chart).mark_line().encode(
    #x=['Date'],
    #y=['System'],
    #color=['Site'],
    # legend=alt.Legend(title='Animals by year')
#)

#st.altair_chart(basic_chart)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()


#From music app file 
stats_df = pd.read_csv("SampleforWork4.csv")
color_map_df = pd.read_csv("color_map_df.csv")
sorted_site = stats_df.groupby('Site')['System'].count().sort_values(ascending=False)
#summary_poster(sorted_site, color_map_df)

select_site = [1]
#Filter df based on selection

stats_df[stats_df['Site'].isin(select_site)].plot(x='Date',y=['System','System1','System2'])


st.markdown("This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files")
st.markdown("Made it to the end.")
