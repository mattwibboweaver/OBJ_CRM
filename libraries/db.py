import sqlite3
import streamlit as st
import secrets


class SQLiteConnection:
    def __init__(self):
        self.db_name = st.secrets['DATABASE']['dbname']
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.pmin = st.secrets['USER']['min_pwd_length']
        self.pmax = st.secrets['USER']['max_pwd_length']





