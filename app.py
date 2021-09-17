import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def load_data(filename):
    df = pd.read_csv(filename, index_col=0)
    return df

def summary_poster(site_df, color_dict):
    #MAKE SUBPLOTS
    fig = make_subplots(
        rows=2, cols=2, 
        column_widths=[0.4, 0.6],
        specs=[[{"type": "pie"}, {"type": "bar"}],
            [ {"type":"scatter", "colspan": 2}, None]],
            subplot_titles=('Overall Share - Pie?', 
                            '#Bar? across Years', 
                            'Scatter?'),
            vertical_spacing=0.1, horizontal_spacing= 0.09)
    #PIE
    #data for pie
    pie_data = site_df.groupby('Site')['System'].count()

    fig.add_trace(go.Pie(labels = pie_data.index,
                            values = pie_data.values,
                            hole = 0.4,
                            legendgroup = 'grp1',
                            showlegend=False),
                row = 1, col = 1)
    fig.update_traces(hoverinfo = 'label+percent',
                        textinfo = 'value+percent',
                        textfont_color = 'white',
                        marker = dict(colors = pie_data.index.map(color_dict),
                                    line=dict(color='white', width=1)),
                        row = 1, col = 1)

    #STACKED BAR
    pivot_site_df = site_df.groupby(['Site','Date'])['System'].count()
    pivot_site_df = pivot_site_df.unstack()
    pivot_site_df.fillna(0, inplace = True)

    #plot params
    labels = pivot_site_df.columns    

    for i, label_name in enumerate(labels):
        x = pivot_site_df.iloc[:,i].index
        fig.add_trace(go.Bar(x = x, 
                                y = pivot_site_df.iloc[:,i],
                                name = label_name,
                                hovertemplate='<b>Year: %{x}</b><br>#Songs: %{y}',
                                marker_color = pd.Series([label_name]*len(x)).map(color_dict),
                                legendgroup = 'grp2',
                                showlegend=True),
                                row = 1, col = 2)
    fig.update_yaxes(title_text = '#Songs',linecolor = 'grey', mirror = True, 
                        title_standoff = 0, gridcolor = 'grey', gridwidth = 0.1,
                        zeroline = False,
                        row = 1, col = 2)
    fig.update_xaxes(linecolor = 'grey', mirror = True, dtick = 5,
                     row = 1, col = 2)

    #SCATTER
    fig.add_trace(go.Scatter(
                x=site_df['Date'],
                y=site_df['System'],
                mode = 'markers',
                marker_color = site_df['clusters'].map(color_dict),
                customdata = site_df.loc[:,['Site','Date','System']],
                hovertemplate='<b>Site: %{customdata[0]}</b><br>Date: %{customdata[1]} <br>System: %{customdata[2]}',
                legendgroup = 'grp1',
                showlegend=False
                ),
                row = 2, col = 1
                )
    fig.update_traces(marker = dict(symbol = 'triangle-right', size = 12
                                    #,line = dict(color = 'grey', width = 0.5)
                                    ),
                      name = "",
                      row = 2, col =1)
    fig.update_yaxes(autorange = 'reversed',title = 'Rank',showgrid=True, 
                    mirror = True, zeroline = False, linecolor = 'grey',
                    title_standoff = 0, gridcolor = 'grey', gridwidth = 0.1,
                    row = 2, col = 1)
    fig.update_xaxes(title="",showgrid=True, mirror = True,
                    linecolor = 'grey', range = [1969,2021],
                    gridcolor = 'grey', gridwidth = 0.1
                    , row = 2, col =1)

    fig.update_layout( # customize font and margins
                        barmode = 'stack',
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        #plot_bgcolor = '#0E1117',#'black',
                        font_family= 'Nunito',#"Helvetica",
                        width=1200,
                        height=800,
                        template = 'plotly_dark',
                        legend=dict(title="", orientation = 'v',
                                    font=dict(size = 10),
                                    bordercolor = 'LightGrey',
                                    borderwidth=0.5),
                        margin = dict(l = 40, t = 40, r = 40, b = 40)
                    )
    
    return fig







st.title('Proof of Concept Data App')
title_image = Image.open("AppTitle.jpg")
st.image(title_image)

#From music app file 
stats_df = load_data("SampleforWork4.csv")
color_map_df = load_data("color_map_df.csv")
sorted_site = stats_df.groupby('Site')['System'].count().sort_values(ascending=False).index
summary_poster(sorted_site, color_map_df)


st.markdown("### **Select Site:**")
select_site = []

select_site.append(st.selectbox('', sorted_site))

#Filter df based on selection
site_df = stats_df[stats_df['Site'].isin(select_site)]


st.markdown("This app is meant as a proof of concept to demonstrate the utility of web-based interfaces for Excel files")

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

st.line_chart(x = filtered_data['Date'], y=filtered_data['System'])


