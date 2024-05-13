from data import (
    district_scatter_mapbox,
    district_choropleth_mapbox,
    region_choropleth_mapbox,
    region_scatter_mapbox,
)

import streamlit as st

st.set_page_config(layout="wide")
st.title("GHW Data Week - 2024")


def scatter_mapbox(disable_data):
    if not disable_data:
        region_scatter_mapbox()
        district_scatter_mapbox()


def choropleth_mapbox(disable_data):
    if not disable_data:
        region_choropleth_mapbox()
        district_choropleth_mapbox()


SIDEBAR_DICT = {
    "RD SCATTER MAP": scatter_mapbox,
    "RD CHOROPLETH MAP": choropleth_mapbox,
}


def main():
    disable_data = st.checkbox("Disable Data", True)
    chart_type = st.sidebar.radio("Select chart type:", SIDEBAR_DICT.keys())
    SIDEBAR_DICT[chart_type](disable_data)


if __name__ == "__main__":
    main()
