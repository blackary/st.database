import sqlite3
from datetime import datetime

import pandas as pd
import streamlit as st

_DB_PATH = ".streamlit/database.sqlite"


con = sqlite3.connect(_DB_PATH)

df = pd.read_sql_query("SELECT * FROM events ORDER BY time DESC", con)
st.subheader("Raw Data From Events Data")
st.write(df)

st.subheader("Widget Type Graph")
df_widgets = df.groupby("widget_type").count()["label"].reset_index()
df_widgets.columns = ["widget_type", "count"]
st.bar_chart(df_widgets, x="widget_type", y="count")

st.subheader("Individual Widget Graph")
df_labels = df.groupby("label").count()["time"].reset_index()
df_labels.columns = ["label", "count"]
st.bar_chart(df_labels, x="label", y="count")

df["date"] = pd.to_datetime(df["time"], unit="ms").dt.date
df["hour"] = pd.to_datetime(df["time"], unit="ms").dt.hour

df_hours = df.groupby("hour").count()["label"].reset_index()
df_hours.columns = ["hour_of_day", "count"]
st.bar_chart(df_hours, x="hour_of_day", y="count")
