from flask import render_template, request, jsonify
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

@main.route('/campanha/criar', methods=['POST'])
def criar_campanha():
    dados = request.get_json()

    nome = dados['nome']
    descricao = dados['descricao']
    mestre = dados['mestre']
    dataInicio = dados['dataInicio']
    dataFim = dados['dataFim']

    session = SessionLocal()

    session.execute(
        text('''
            INSERT INTO CAMPANHAS(NOME,
                                  DESCRICAO,
                                  MESTRE,
                                  INICIO,
                                  FIM)
                           VALUES(:nome,
                                  :descricao,
                                  :mestre,
                                  :dataInicio,
                                  :dataFim)
        '''),
        {
            'nome': nome,
            'descricao': descricao,
            'mestre': mestre,
            'dataInicio': dataInicio,
            'dataFim': dataFim
        }
    )

    session.commit()
    session.close()

    return jsonify({'sucesso': True})

@main.route('/campanha/excluir', methods=['DELETE'])
def excluir_campanha():
    try:
        dados = request.get_json()

        id_campanha = dados['id']
        session = SessionLocal()

        try:
            session.execute(
                text('''
                    DELETE FROM CAMPANHAS
                    WHERE ID = :id
                '''),
                {'id': id_campanha}
            )
            session.commit()
            return jsonify({'sucesso': True})
            
        except Exception as e:
            session.rollback()
            return jsonify({'sucesso': False, 'erro': f'Erro no banco: {str(e)}'}), 500
        
        finally:
            session.close()
            
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Falha interna no servidor.'}), 500