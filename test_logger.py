import sqlite3

import streamlit_patches as st

a = st.checkbox("my_widget_name", widget_logger=True)
b = st.text_input("my_text_input", widget_logger=True)
c = st.selectbox(label="my_selection_input", options=[1, 2, 3], widget_logger=True)
