import streamlit as st

class MultiPage:
    def __init__(self):
        self.pages = {}

    def add_page(self, title, page):
        self.pages[title] = page

    def run(self):
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(self.pages.keys()))

        page = self.pages[selection]
        page.app()

