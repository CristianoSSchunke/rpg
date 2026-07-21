from flask import render_template, request
from connection import SessionLocal
from sqlalchemy import text
from main import main

@main.route('/lobby')
def lobby():
    campanha_id = request.args.get('campanha_id')

    session = SessionLocal()
    
    campanha = session.execute(
        text('SELECT * FROM CAMPANHAS WHERE ID = :id'),
        {'id': campanha_id}

    ).mappings().first()

    session.close()
    return render_template('lobby.html', campanha=campanha)