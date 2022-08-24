from datetime import datetime

import streamlit_patches as st

st.database = st.Database("comments")

"# Comments:"

if "comments" not in st.database or st.button("Clear comments"):
    st.database["comments"] = []

comments = st.database["comments"]
for idx, entry in enumerate(comments):
    st.write(
        f"""
        {entry["name"]} - {entry["date"]}
        > {entry["comment"]}
        """
    )
    is_last = idx == len(comments) - 1
    is_new = "just_posted" in st.session_state and is_last
    if is_new:
        st.success("☝️ Your comment was successfully posted.")

"# "

"**Add your own comment**"

with st.form("comment"):
    name = st.text_input("Name")
    comment = st.text_area("Comment")
    if st.form_submit_button("Add comment"):
        st.database["comments"] += [
            {
                "name": name,
                "comment": comment,
                "date": datetime.now(),
            }
        ]
        st.session_state["just_posted"] = True
        st.experimental_rerun()
