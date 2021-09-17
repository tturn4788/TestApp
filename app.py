app.py

import numpy as np
from PIL import Image
import streamlit as st
from Helper import load_data, summary_poster

stats_df = load_data("./data/SampleforWork4.csv")
color_map_df = load_data("./data/color_map_df.csv")

st.set_page_config(page_title="Proof of Concept for Tables of Data", 
                   page_icon=":notes:", 
                   layout='wide')

#--------------------------------- ---------------------------------  ---------------------------------
#--------------------------------- SETTING UP THE APP
#--------------------------------- ---------------------------------  ---------------------------------
title_image = Image.open("./plots/AppTitle.jpg")
st.image(title_image)

st.markdown("A Data Geek's take on the question ***'How have music tastes changed through the years?'***")
st.markdown("This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files")
#---------------------------------------------------------------#
# SELECT ARTIST AND SETUP DATA
#---------------------------------------------------------------#
sorted_site = stats_df.groupby('Site')['search_query'].count().sort_values(ascending=False).index

st.markdown("### **Select Site:**")
select_site = []

select_site.append(st.selectbox('', sorted_site))

#Filter df based on selection
site_df = stats_df[stats_df['search_site'].isin(select_site)]

major_cluster = site_df.groupby('Date')['search_query'].count().sort_values(ascending = False).index[0]
