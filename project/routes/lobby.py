from flask import render_template
from connection import SessionLocal
from sqlalchemy import text
from main import main

@main.route('/lobby')
def lobby():
    return render_template('lobby.html')