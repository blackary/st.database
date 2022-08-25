import streamlit_patches as st
import urllib
import hashlib


def get_profile_pic(email: str):
    size = 100
    gravatar_url = (
        "https://www.gravatar.com/avatar/"
        + hashlib.md5(email.encode()).hexdigest()
        + "?"
    )
    gravatar_url += urllib.parse.urlencode({"s": str(size), "d": "robohash"})
    st.sidebar.image(gravatar_url)


if st.session_state.get("logged_in_user", None):
    user = st.database("user")[st.session_state["logged_in_user"]]
    if user["settings"].get("wide mode") is True:
        st.set_page_config(layout="wide")
    else:
        st.set_page_config(layout="centered")
    if user["settings"].get("email"):
        st.sidebar.write(f"Email: {user['settings']['email']}")
        get_profile_pic(user["settings"]["email"])

    st.sidebar.write("Logged in as " + st.session_state["logged_in_user"])

    if st.sidebar.button("Logout"):
        st.session_state["logged_in_user"] = None
        st.experimental_rerun()
else:
    st.set_page_config(layout="centered")
    st.sidebar.write("Not logged in")
    if st.sidebar.button("Go to login page"):
        st.switch_page("Login and user settings")

st.page("database.py", "st.database", ":floppy_disk:")
st.page("user.py", "Login and user settings", icon=":wood:")
st.page("ama.py", "Fanilo AMA Clone", icon=":question:")
st.page("todo.py", "TODO", icon=":white_check_mark:")
st.page("playground.py", "Streamlit Playground", icon=":video_game:")
st.page("comments.py", "Comments", icon=":speech_balloon:")
st.page("poll.py", "Poll", icon=":chart_with_upwards_trend:")
st.page("admin.py", "Admin", icon=":wrench:")
