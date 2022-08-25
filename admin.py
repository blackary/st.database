from datetime import date
import streamlit_patches as st
from pathlib import Path

if st.session_state.get("logged_in_user", None) != "blackary":
    st.write("You are not authorized to view this page.")
    st.stop()

tables = st.get_tables()

table = st.selectbox("Select table", tables)

db = st.Database(table)

items_dict = {k: v for k, v in db.items()}

st.json(items_dict)

db_path = Path(st._DB_PATH)
db_filename = f"{date.today()}-{db_path.name}"
st.download_button(
    "Download Database", data=db_path.read_bytes(), file_name=db_filename
)

uploaded = st.file_uploader("Upload Database", type="sqlite")

if uploaded is not None:
    new_file = uploaded.read()
    new_length = len(new_file)
    old_length = len(db_path.read_bytes())
    st.warning(
        (
            f"Are you sure you want to overwrite the database (old size: {old_length} "
            f"bytes, new size: {new_length} bytes)?"
        ),
        icon="❗",
    )
    if st.button("Overwrite"):
        db_path.write_bytes(new_file)
        st.success("Database uploaded")
