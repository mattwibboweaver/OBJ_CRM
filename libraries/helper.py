import re
import streamlit as st
from libraries.db import SQLiteConnection


def get_db_connection():
    """
    Get a database connection and store in the session state
    """
    if st.session_state.get('db', None) is None:
        db = SQLiteConnection()
        st.session_state['db'] = db
        st.session_state['cur'] = db.cursor

    return st.session_state['db']


def login_is_valid(username, password, pmax, pmin):
    """
    Return True if the username/password combination is valid, False otherwise.
    """
    user = username_is_valid(username)
    pwd = password_is_valid(password, pmax, pmin)
    return user and pwd


def password_is_valid(password, pmax, pmin):
    """
    Return True if the password string is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9!@£$%^&*()_=+\[\]#]+$'
    valid = bool(re.match(pattern, password))
    valid = valid and len(password) >= pmin
    valid = valid and len(password) <= pmax

    return valid


def username_is_valid(email):
    """
    Return True if the email string is a valid email address, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    x = bool(re.match(pattern, email))
    return x
