import streamlit as st
import libraries.helper as hp
from libraries.users import AppUser


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
        if st.button('Register', key='register', disabled=st.session_state.get('login_btn_enabled')):

            new_user = users.create_user(username, password)
            if new_user:
                st.session_state['db'].conn.commit()
                st.session_state['logged_in_user'] = username
                st.experimental_rerun()
            else:
                st.error('Error!')


if st.session_state.get('db', None) is None:
    # Get a database connection if we don't have one
    db = hp.get_db_connection()
    st.session_state['db'] = db

users = AppUser(st.session_state.get('db', None))

if st.session_state.get('logged_in_user', None) is None:
    # Show the login screen if we're not logged in
    show_login_screen()
else:
    # TODO The main application logic goes here!
    st.write('Logged in as', st.session_state.get('logged_in_user', None))
