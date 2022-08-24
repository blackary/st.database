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


start = time()
st.database["df"] = df
end = time()
st.write(f"Time to write to database: {end - start} seconds")

start = time()
st.write(st.database["df"])
end = time()
st.write(f"Time to read: {end - start}")
