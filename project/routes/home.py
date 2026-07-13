from flask import render_template
from connection import SessionLocal
from sqlalchemy import text
from main import main

@main.route('/')
def home():
    session = SessionLocal()
    
    campanhas = session.execute(
        text('SELECT * FROM CAMPANHAS ORDER BY NOME')

    ).mappings().all()

    session.close()
    return render_template('home.html', campanhas=campanhas)