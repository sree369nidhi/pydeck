import streamlit as st
import pandas as pd 
import pydeck as pdk

#LOADING DATA
DATA_URL = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"

def load_data():
    """Choose here your data format"""
    #data = pd.read_csv(DATA_URL).dropna() ## super slow if used
    # data.to_csv('./data.csv',index=False)
    data = pd.read_csv('heatmap-data.csv') ## super slow if used
    # data = data.to_dict('records') ## super slow if used

    return data

# LAYER 
def map(data):
    view_state = pdk.ViewState(
        longitude=-1.415,
        latitude=52.2323,
        zoom=6,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36,
    )
    
    layer = pdk.Layer(
        "HexagonLayer",
        data,
        get_position=["lng", "lat"],
        auto_highlight=True,
        elevation_scale=height,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,
        coverage=1,
        radius=radius,
        opacity=opacity
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state, 
        tooltip=True
        )        
    )

# SIDEBARs
radius = st.sidebar.slider("Diameter of ⬡ (meters) ", 100, 20000, 10000, 100) // 2
height = st.sidebar.slider("Height of  ⬡",1, 200, 100, 10)
opacity = st.sidebar.slider('Opacity', 0.01, 1.0, 1.0, 0.01)

# RENDER
data = load_data()

if st.checkbox('Display data ?'):
    data

map(DATA_URL)