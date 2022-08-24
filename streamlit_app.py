import uuid
from datetime import datetime

import streamlit_patches as st

"# TODO App"

# To make testing multiple apps easier, use a different table
st.database = st.Database("default")

with st.expander("Show all details"):
    st.write(st.database.values())
