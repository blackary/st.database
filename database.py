import streamlit_patches as st

st.database = st.Database("default")

"# st.database"

"""
What could we do if streamlit had a built-in database? Rather similar to st.session_state,
except the data in it never goes away. This wouldn't only be for caching, though.

It could be for saving and keeping track of all kinds of data. In this current
implementation, it can save any kind of data that is pickleable.

Here is a simple example of the usage:
"""

with st.echo():
    if "page_load_count" not in st.database:
        st.database["page_load_count"] = 0

    st.database["page_load_count"] += 1

    st.write("Page load count", st.database["page_load_count"])

"""
---

By default, all entries are in a default table. If you want to isolate data to a
specific table, you can do that with the `st.Database(<table_name>)` function, and
use that instead.

The data is only persistent locally, as it is saved to a local file. However,
 in the case of a server deployment, where the data needs to persist longer than
 the server itself, you could use something like
 [litestream](https://litestream.io/guides/kubernetes/).
"""
