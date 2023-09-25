import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px

st.title('Nuclear Power Plants Dataset')

# Load the dataset
data = pd.read_csv("./archive/nuclear_power_plants.csv")

# Display the raw data if requested
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of Nuclear Power Plants by Country: ')
country_counts = data['Country'].value_counts()
st.bar_chart(country_counts)


st.subheader('The most capacity by Country: ')
st.scatter_chart(data=data, x="Country", y="Capacity")

st.subheader("The status by Country:")
fig = px.bar(data, x="Country", color="Status")
st.plotly_chart(fig)

st.subheader('Map of Nuclear Power Plants')
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=data['Latitude'].mean(),
        longitude=data['Longitude'].mean(),
        zoom=3,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[Longitude, Latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=40000,
        ),
    ],
))


st.title('Map of Big Countries')
big_countries = ["China", "Japan", "United States"] 
big_country_data = data[data['Country'].isin(big_countries)]
map_style = "mapbox://styles/mapbox/light-v9"
st.pydeck_chart(pdk.Deck(
    map_style=map_style, 
    initial_view_state=pdk.ViewState(
        latitude=big_country_data['Latitude'].mean(),
        longitude=big_country_data['Longitude'].mean(),
        zoom=3,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=big_country_data,
            get_position='[Longitude, Latitude]',
            get_color='[100, 30, 0, 160]',
            get_radius=20000,
        ),
    ],
))