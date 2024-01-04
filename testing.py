import streamlit as st
import sqlite3
import socket


class Get_IP:
    def __init__(self):
        st.markdown('''
                # Happy-day
                ''', True
                    )
        self.connection = sqlite3.connect('db_user.sqlite3')
        self.cursor = self.connection.cursor()

    def get_ip_address(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    def save(self):
        name = st.text_input("Enter your name...")
        em = st.text_input("Enter your email address...")
        ip = self.get_ip_address()
        sb_button = st.button('Submit')
        if sb_button:
            st.write(f'Your name is {name} and email address is {em}')
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                                id INTEGER PRIMARY KEY,
                                Name TEXT,
                                Email TEXT,
                                ip_address TEXT
                            )''')
            self.insert_to_db(name, em, ip)

    def insert_to_db(self, name, email, ip):
        self.cursor.execute("INSERT INTO User (Name, Email, ip_address) VALUES (?, ?, ?)", (name, email, ip))
        self.connection.commit()


if __name__ == '__main__':
    Test = Get_IP()
    Test.save()
