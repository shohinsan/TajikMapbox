import json
import pandas as pd
import plotly.express as px
import streamlit as st
import os

import warnings

warnings.filterwarnings("ignore")


current_dir = os.path.dirname(__file__)
MARKER = os.path.join(current_dir, "marker.json")
POLYGON = os.path.join(current_dir, "polygon.geojson")


def district_scatter_mapbox():
    # Give a subtitle in the streamlit app
    st.subheader("Visualising Cities of Tajikistan - Scatter Map")
    # Loading region and city data from JSON file into a Pandas Dataframe
    region_city_data = pd.read_json(MARKER)
    # show a table
    st.dataframe(region_city_data, hide_index=True)
    # plotly scatter plot
    fig = px.scatter_mapbox(
        data_frame=region_city_data,
        lat="lat",
        lon="long",
        hover_name="district",
        hover_data="district",
        color="district",
        # color_discrete_sequence=px.colors.qualitative.Plotly,
        # color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=3,
        opacity=0.9,
        height=700,
        center={"lat": 38.86, "lon": 71.27},
    )
    # Basemap style
    # options: open-street-map, carto-positron, carto-darkmatter
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"t": 0, "r": 0, "b": 0, "l": 0})
    return st.plotly_chart(fig)


def district_choropleth_mapbox():
    # Give a subtitle in the streamlit app
    st.subheader("Visualising Cities of Tajikistan - Scatter Map")

    # Loading region and city data from JSON file into a Pandas Dataframe
    region_city_data = pd.read_json(MARKER)

    # show a table
    st.dataframe(region_city_data, hide_index=True)

    # Load GeoJSON data
    with open(POLYGON, "r") as f:
        geojson_data = json.load(f)

    # Reset index to avoid FutureWarning
    region_city_data_reset = region_city_data.reset_index()

    # plotly choropleth plot
    fig = px.choropleth_mapbox(
        data_frame=region_city_data_reset,
        geojson=geojson_data,
        locations="district",
        featureidkey="properties.name",
        color="district",
        color_discrete_sequence=px.colors.qualitative.Plotly,
        hover_name="district",
        hover_data=["district"],
        mapbox_style="open-street-map",
        zoom=3,
        opacity=0.9,
        height=700,
        center={"lat": 38.86, "lon": 71.27},
    )

    fig.update_layout(margin={"t": 0, "r": 0, "b": 0, "l": 0})

    return st.plotly_chart(fig)
