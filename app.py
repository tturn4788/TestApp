import streamlit as st
import pandas as pd
import numpy as np

st.title('Proof of Concept Data App')

DATE_COLUMN = 'Date'
DATA_URL = ('./Data/SampleforWork4.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(190)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-11
site_to_filter = st.slider('Site', 0, 11, 17)
filtered_data = data[data['Site'] == site_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.(filtered_data)

chart_data = filtered_data(
     columns=['', 'b', 'c'])

st.line_chart(x = filtered_data['Date'], y=filtered_data['System'])ex[0]
