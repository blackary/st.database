import os
from hashlib import scrypt
from typing import Callable

import streamlit_patches as st

st.database = st.Database("user")

"# User login / saving settings"


def hash_password(password: str) -> str:
    salt = st.secrets.get("salt", os.environ.get("salt"))
    return scrypt(
        password.encode(), salt=salt.encode(), n=2**10, r=10, p=100
    ).hex()


if "logged_in_user" not in st.session_state:
    st.session_state["logged_in_user"] = None


def show_login():
    st.warning(
        (
            "This is a demo app, and does not necessarily demonstrate best practices for "
            "dealing with usernames and passwords."
        ),
        icon="⚠️",
    )
    sign_in, create = st.tabs(["Sign into account", "Create account"])
    with create:
        with st.form("Create account"):
            "## Create account"
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Save"):
                if username in st.database:
                    st.error("Username already exists")
                else:
                    pw = hash_password(password)

                    st.database[username] = {
                        "username": username,
                        "password": pw,
                        "settings": {},
                    }

                    st.success(f"Saved account for {username}")

    with sign_in:
        with st.form("Sign in"):
            "## Sign into existing account"
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Sign in"):
                pw = hash_password(password)

                if username in st.database and st.database[username]["password"] == pw:
                    st.session_state["logged_in_user"] = username
                    st.success("Signed in")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")


if not st.session_state["logged_in_user"]:
    show_login()
    st.stop()

username = st.session_state["logged_in_user"]

"### Welcome, " + username

user = st.database[username]

for key, value in user["settings"].items():
    if value != "":
        st.write(f"**{key.title()}**: {value}")

with st.expander("Edit account"):
    with st.form("Edit account"):
        settings = [
            "full name",
            "bio",
            "email",
            "website",
            "twitter",
            "github",
            "wide mode",
        ]
        for setting in settings:
            if setting == "bio":
                input: Callable = st.text_area
            elif setting == "wide mode":
                input = st.checkbox
            else:
                input = st.text_input
            s = input(f"{setting.title()}", value=user["settings"].get(setting, ""))  # type: ignore
            if s != "":
                user["settings"][setting] = s

        if st.form_submit_button("Save"):
            st.database[username] = user
            st.success("Saved")
            st.experimental_rerun()
