import streamlit as st

st.markdown("# Mapping")

# Tu código para la página de mapas aquí, incluyendo la visualización de Foursquare Studio
url_foursquare = "https://studio.foursquare.com/public/8729d261-aaf7-4cf6-ad1d-919a41da54d1"
st.components.v1.iframe(url_foursquare, width=800, height=600)

