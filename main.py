import streamlit as st
from libraries.db import SQLiteConnection


def get_db_connection():
    """
    Get a database connection and store in the session state
    """
    db_conn = SQLiteConnection()
    st.session_state['conn'] = db_conn
    st.session_state['cur'] = db_conn.cursor


def show_login_screen():
    """
    Show the login screen, handle login and registration
    """
    st.subheader('Please login')
    username = st.text_input('Username', key='username').strip()
    password = st.text_input('Password', key='password', type='password').strip()

    st.session_state['login_btn_enabled'] = not (len(username) > 0 and len(password) > 0)

    col1, col2 = st.columns([1, 6])

    with col1:
        if st.button('Login', key='login', disabled=st.session_state.get('login_btn_enabled')):
            user = st.session_state['cur'].execute('SELECT * FROM user WHERE username=? AND password=?',
                                                   (username, password))
            user = user.fetchone()
            if user is not None:
                st.session_state['logged_in_user'] = user[0]
                st.experimental_rerun()
            else:
                st.error('Error!')
    with col2:
        if st.button('Register', key='register'):
            ...


# The login page
if st.session_state.get('conn', None) is None:
    # Get a database connection if we don't have one
    get_db_connection()

if st.session_state.get('logged_in_user', None) is None:
    # Show the login screen if we're not logged in
    show_login_screen()
else:
    st.write('Logged in as', st.session_state.get('logged_in_user', None))
