import streamlit as st
import libraries.helper as hp


class AppUser:

    def __init__(self, db):
        """
        Initialise the AppUser class.
        :param db: The database connection
        """
        self.db = db
        self.cur = db.cursor
        self.pmin = db.pmin
        self.pmax = db.pmax

    def create_user(self, username, password):
        """
        Create a new user in the app database.
        :param username: The user's username
        :param password: The user's password
        :return: True if the user was created, False otherwise
        """
        if not hp.login_is_valid(username, password, self.pmax, self.pmin):
            return False

        try:
            self.cur.execute('INSERT INTO user (username, password) VALUES (?, ?)',
                             (username, password))

            self.db.conn.commit()
        except Exception as e:
            st.error(e)
            return False

        return True
