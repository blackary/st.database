import streamlit_patches as st

if st.session_state.get("logged_in_user", None) != "blackary":
    st.write("You are not authorized to view this page.")
    st.stop()

tables = st.get_tables()

table = st.selectbox("Select table", tables)

db = st.Database(table)

items_dict = {k: v for k, v in db.items()}

st.json(items_dict)
