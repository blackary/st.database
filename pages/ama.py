from datetime import datetime

import streamlit_patches as st

st.database = st.Database("ama")

if "questions" not in st.database:
    st.database["questions"] = []

with st.expander("Get all messages"):
    st.json(st.database["questions"])
    if st.button("Clear questions"):
        del st.database["questions"]
        st.experimental_rerun()

with st.form("ama"):
    name = st.text_input("Your name (optional)")

    question = st.text_area("Your question")

    private = st.checkbox("Hide your message from the public board")

    if st.form_submit_button("Submit form"):
        if not question.strip():
            st.error("Please enter a question")
            st.stop()

        st.database["questions"] += [
            {
                "name": name,
                "question": question,
                "private": private,
                "created": datetime.now(),
            }
        ]
        st.experimental_rerun()
