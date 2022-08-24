import uuid
from datetime import datetime

import streamlit_patches as st

"# TODO App"

# To make testing multiple apps easier, use a different table
st.database = st.Database("todo")


if st.button("Clear todos"):
    for key in st.database.keys():
        del st.database[key]


def toggle(item):
    item["completed"] = not item["completed"]
    item["updated"] = datetime.now()
    st.database[item["id"]] = item


"## TODOs"

show_completed = st.checkbox("Show completed", value=True)

"---"


to_show = []
for id, item in st.database.items():
    if not item["completed"] or show_completed:
        to_show.append(item)

for item in sorted(to_show, key=lambda x: x["created"]):
    st.checkbox(
        item["label"],
        key=item["id"],
        value=item["completed"],
        on_change=toggle,
        args=(item,),
        help=str(item["created"]),
    )


"---"

with st.form("add_item"):
    text = st.text_input("Add new item")
    if st.form_submit_button("Add"):
        id = str(uuid.uuid4())
        st.database[id] = {
            "id": id,
            "label": text,
            "completed": False,
            "created": datetime.now(),
            "updated": datetime.now(),
        }
        st.experimental_rerun()


with st.expander("Show all details"):
    st.write(st.database.values())
