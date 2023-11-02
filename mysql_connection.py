import mysql.connector
import streamlit as st

conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    db="odontofeedback"
)

c = conn.cursor()

def view_all_data():
    c.execute('SELECT * FROM feedback ORDER BY id ASC')
    data = c.fetchall()
    return data

def view_all_tratamentos():
    c.execute('SELECT * FROM tratamentos')
    tratamentos = c.fetchall()
    return tratamentos