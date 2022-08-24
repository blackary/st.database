import streamlit_patches as st

st.database = st.Database("default")

"# st.database"

"""
What could we do if streamlit had a built-in database? Rather similar to st.session_state,
except the data in it never goes away. This wouldn't only be for caching, though.

It could be for saving and keeping track of all kinds of data.

Examples so far:
* [Classic TODO App](./todo)
* [Fanilo's Ask Me Anything](./ama)
* [Streamlit Playground with url shortening](./playground)
* [The example comments app](./comments)
"""

with st.echo():
    if "page_load_count" not in st.database:
        st.database["page_load_count"] = 0

    st.database["page_load_count"] += 1

    st.write("Page load count", st.database["page_load_count"])
