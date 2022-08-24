import streamlit_patches as st

st.page("database.py", "st.database", ":floppy_disk:")
st.page("user.py", "Login and user settings", icon=":wood:")
st.page("ama.py", "Fanilo AMA Clone", icon=":question:")
st.page("todo.py", "TODO", icon=":white_check_mark:")
st.page("playground.py", "Streamlit Playground", icon=":video_game:")
st.page("comments.py", "Comments", icon=":speech_balloon:")
st.page("admin.py", "Admin", icon=":wrench:")

if st.session_state.get("logged_in_user", None):
    st.sidebar.write("Logged in as " + st.session_state["logged_in_user"])
else:
    st.sidebar.write("Not logged in")
