from time import time

import streamlit_patches as st

num_items = st.slider("Num items", min_value=1, max_value=1_000, value=100)

start = time()
for i in range(num_items):
    st.database[i] = i
end = time()
st.write(f"Time to write to database: {end - start:.3f} seconds")

st.write("Length of database:", len(st.database))

start = time()
for i in range(num_items):
    _ = st.database[i]
end = time()
st.write(f"Time to read: {end - start}")

start = time()
for key, val in st.database.items():
    pass
end = time()
st.write(f"Time to iterate over database: {end - start:.3f} seconds")

start = time()
for i in range(num_items):
    del st.database[i]
end = time()
st.write(f"Time to delete from database: {end - start:.3f} seconds")

st.write(len(st.database))
