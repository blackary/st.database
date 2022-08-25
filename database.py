import streamlit_patches as st

st.database = st.Database("default")

"# st.database"

"""
What could we do if streamlit had a built-in database? Rather similar to st.session_state,
except the data in it never goes away. This wouldn't only be for caching, though.

It could be for saving and keeping track of all kinds of data. In this current
implementation, it can save any kind of data that is pickleable.

## Usage

Here is a simple example of the usage:
"""

with st.echo():
    if "page_load_count" not in st.database:
        st.database["page_load_count"] = 0

    st.database["page_load_count"] += 1

    st.write("Page load count", st.database["page_load_count"])

"""
---

By default there is a default table that gets used for all database entries. If you
would like to use a different table for some or all of your app usage, you can use the
syntax `st.database(<table_name>)[<key>]`.

For example:
"""

with st.echo():
    if "page_load_count" not in st.database("my_table"):
        st.database("my_table")["page_load_count"] = 0

    st.database("my_table")["page_load_count"] += 1

    st.write(
        "Page load count in the `my_table` table",
        st.database("my_table")["page_load_count"],
    )

"""
---

## Persistence

The data is only persistent locally, as it is saved to a local file. However,
 in the case of a server deployment, where the data needs to persist longer than
 the server itself, you could use something like
 [litestream](https://litestream.io/guides/kubernetes/).
 Alternatively, we could provide a pluggable API that would allow people to bring their
 own database backend, but still use st.database.

It seems like there will be natural solutions to do this depending on where the
app is hosted (Snowflake, Community Cloud, etc.).

For now an Admin user can go to the Admin page and download a copy of the current
table, and upload a new one.
"""
