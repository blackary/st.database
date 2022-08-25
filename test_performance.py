import sqlite3

import pandas as pd
import streamlit as st

_DB_PATH = ".streamlit/database.sqlite"


con = sqlite3.connect(_DB_PATH)

df = pd.read_sql_query("SELECT * FROM events", con)
st.write(df)

st.write(df.groupby("widget_type").count()["label"])

st.write(df.groupby("label").count()["time"])
