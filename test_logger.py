import streamlit_patches as st

st.database = st.Database("default")


a = st.checkbox("my_widget_name", widget_logger=True)
