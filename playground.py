import hashlib
from time import sleep
from urllib import parse

from streamlit_ace import st_ace

import streamlit_patches as st

st.database = st.Database("playground")

DEFAULT_HASH_LENGTH = 6
BASE_URL = "https://database.streamlitapp.com/Streamlit%20Playground"

"""
# Streamlit Playground!

Allows you to create and share streamlit apps by saving the code into the database,
and then creating a short, shareable url to access the app.

By default it's in read-only mode, unless you pass in the right query parameter,
 or are logged into the right account in the /user page.

But, you can see some examples of what it looks like by clicking the buttons in the
sidebar.
"""


def expand_short_url():
    ctx = st.get_script_run_ctx()
    query = parse.parse_qs(ctx.query_string)
    if "q" not in query:
        return
    hash = query["q"][0]
    st.session_state["python"] = st.database[hash]


expand_short_url()

examples = ["balloons", "empty-issues"]

st.sidebar.write("Switch to example:")
for example in examples:
    if st.sidebar.button("Switch to " + example + " example"):
        st.experimental_set_query_params(q=example)
        sleep(0.1)
        st.experimental_rerun()


def get_hash_from_python() -> str:
    """
    Given a string representation of the python code, return a truncated hash
    """
    python = st.session_state["python"]
    return hashlib.md5(python.encode()).hexdigest()[:DEFAULT_HASH_LENGTH]


def get_short_url_button():
    custom_hash = st.text_input("Custom Hash").strip()
    if st.button("Get shareable url"):
        if custom_hash:
            hash = custom_hash
        else:
            hash = get_hash_from_python()

        st.database[hash] = st.session_state["python"]

        url = f"{BASE_URL}/?q={hash}"
        st.write(url)


def can_edit() -> bool:
    if st.session_state.get("logged_in_user", None) in ["blackary", "tylerjrichards"]:
        return True

    ctx = st.get_script_run_ctx()
    if ctx is None:
        return False
    query = parse.parse_qs(ctx.query_string)
    return query.get("edit_password", [""])[0] == st.secrets["edit_password"]


if "python" not in st.session_state:
    st.session_state["python"] = ""


def execute(code: str):
    try:
        exec(code, globals(), globals())
    except Exception as e:
        st.exception(e)


if can_edit():
    python = st_ace(
        value=st.session_state["python"],
        key="python",
        language="python",
        min_lines=20,
    )
    get_short_url_button()

else:
    st.expander("Show code").code(st.session_state["python"])


execute(st.session_state["python"])
