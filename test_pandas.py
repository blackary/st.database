from time import time

import pandas as pd

import streamlit_patches as st

df = pd.DataFrame(
    {
        "a": [1, 2, 3, 4],
        "b": [10, 20, 30, 40],
        "c": [100, 200, 300, 400],
    }
)

variable_slider = st.slider("hey", 1, 10)

st.file_uploader("hey upload the file")

st.write(variable_slider)

start = time()
st.database["df"] = df
end = time()
st.write(f"Time to write to database: {end - start} seconds")

start = time()
st.write(st.database["df"])
end = time()
st.write(f"Time to read: {end - start}")
