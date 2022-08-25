import logging
from datetime import date, datetime
from functools import wraps
from typing import Any, Callable

from sqlitedict import SqliteDict
from streamlit import *
from streamlit import _get_script_run_ctx

logging.getLogger("sqlitedict").disabled = True


_DB_PATH = ".streamlit/database.sqlite"


class Database:
    def __init__(self, table_name: str = "unnamed") -> None:
        self.table_name = table_name
        self.read_args = {
            "filename": _DB_PATH,
            "tablename": self.table_name,
            "flag": "r",
        }
        self.write_args = {
            "filename": _DB_PATH,
            "tablename": self.table_name,
            "autocommit": True,
        }

    def __getitem__(self, key):
        with SqliteDict(**self.read_args) as db:
            return db[key]

    def __setitem__(self, key, value):
        with SqliteDict(**self.write_args) as db:
            db[key] = value

    def __delitem__(self, key):
        with SqliteDict(**self.write_args) as db:
            del db[key]

    def __iter__(self):
        with SqliteDict(**self.read_args) as db:
            return iter(db)

    def __len__(self):
        with SqliteDict(**self.read_args) as db:
            return len(db)

    def __repr__(self):
        return str(self.read_args)

    def __contains__(self, key):
        with SqliteDict(**self.read_args) as db:
            return key in db

    def items(self):
        with SqliteDict(**self.read_args) as db:
            return list(db.items())

    def keys(self):
        with SqliteDict(**self.read_args) as db:
            return list(db.keys())

    def values(self):
        with SqliteDict(**self.read_args) as db:
            return list(db.values())


database = Database()


def widget_logger(widget: Callable, value_type: type = None, default_value: Any = None):
    @wraps(widget)
    def wrapper(label: str, *args, **kwargs) -> Any:
        """
        Wrapps a streamlit widget, adding a new optional parameter `widget_logger`. If it is
        not True, then this simply returns the standard version of the widget

        If widget_logger=True, add an event in our events table with the label, value,
        and timestamp on change
        """
        try:
            widget_logger = kwargs.pop("widget_logger", False)
            if widget_logger == False:
                raise KeyError
        except KeyError:
            return widget(label, *args, **kwargs)

        # Derive widget class from string representation of widget
        # e.g. "<bound method CheckboxMixin.checkbox of..." -> "checkbox"
        widget_type = str(widget).split("Mixin.")[1].split()[0]

        # Make key that will be used in both session state and url param
        label = f"{widget_type}_{label}".replace(" ", "_").lower()

        def on_change():
            print("this is on the change")

        kwargs["on_change"] = on_change
        print(
            f"your widget, called {label} and of the type {widget_type} was rendered at {datetime.now()}"
        )

        new_value = widget(label, widget_type, *args, **kwargs)

        return new_value

    return wrapper


checkbox = widget_logger(checkbox, bool, False)
radio = widget_logger(radio, int, 0)
text_input = widget_logger(text_input, str, "")
text_area = widget_logger(text_area, str, "")
number_input = widget_logger(number_input, float)
slider = widget_logger(slider)
date_input = widget_logger(date_input, date)
selectbox = widget_logger(selectbox, int, 0)
multiselect = widget_logger(multiselect, list)
