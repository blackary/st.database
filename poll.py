import streamlit_patches as st
import pandas as pd

table = st.database("poll_submissions")

with st.form(key="poll"):
    favorite_animal = st.text_input(
        "What's your favorite animal?",
    )

    submitted = st.form_submit_button("Submit answer!")


if submitted:
    favorite_animal = favorite_animal.lower()

    if favorite_animal not in table:
        table[favorite_animal] = 0
    table[favorite_animal] += 1

if len(table) == 0:
    st.write("Submit your favorite pet!")
    st.stop()

values = pd.DataFrame([{"name": name, "value": value} for name, value in table.items()])

st.bar_chart(values, x="name", y="value")
