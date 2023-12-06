import streamlit as st
from multipage import MultiPage
from pages import home, maps, results

app = MultiPage()

app.add_page("Home", home)
app.add_page("Maps", maps)
app.add_page("Conclusiones", results)

app.run()