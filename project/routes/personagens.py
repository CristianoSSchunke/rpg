from flask import render_template, request, jsonify
from connection import SessionLocal
from sqlalchemy import text
from main import main

@main.route('/personagens')
def personagens():
    campanha_id = request.args.get('campanha_id')

    session = SessionLocal()
    
    personagens = session.execute(
        text('''SELECT * 
                  FROM PERSONAGENS
                 WHERE CAMPANHA_ID = :id
                   AND COALESCE(NPC, 'N') <> 'S' '''),
        {'id': campanha_id}

    ).mappings().all()

    session.close()
    return render_template('personagens.html', personagens=personagens)

@main.route('/personagens/criar', methods=['POST'])
def criar_personagens():
    dados = request.get_json()

    nome = dados['nome']
    sexo = dados['sexo']
    altura = dados['altura']
    peso = dados['peso']
    idade = dados['idade']
    racaId = dados['racaId']
    classeId = dados['classeId']
    descricao = dados['descricao']
    honra = dados['honra']
    origem = dados['origem']
    pesoMax = dados['pesoMax']
    campanhaId = dados['campanhaId']

    vidaMax = dados['vidaMax']

    session = SessionLocal()

    session.execute(
        text('''
            INSERT INTO PERSONAGENS(NOME,
                                    SEXO,
                                    ALTURA,
                                    PESO,
                                    IDADE,
                                    RACA_ID,
                                    CLASSE_ID,
                                    DESCRICAO,
                                    NPC,
                                    NIVEL,
                                    XP,
                                    MORTES,
                                    HONRA,
                                    ORIGEM,
                                    VIDA_MAX,
                                    VIDA_ATUAL,
                                    NIVEL_MAGICO,
                                    PESO_MAX,
                                    PESO_ATUAL,
                                    CAMPANHA_ID
                             VALUES(:nome,
                                    :sexo,
                                    :altura,
                                    :peso,
                                    :idade,
                                    :racaId,
                                    :classeId,
                                    :descricao,
                                    'N',
                                    1,
                                    0,
                                    0,
                                    :honra,
                                    :origem,
                                    :vidaMax,
                                    :vidaAtual,
                                    1,
                                    :pesoMax,
                                    0,
                                    :campanhaId)
        '''),
        {
            'nome': nome,
            'sexo': sexo,
            'altura': altura,
            'peso': peso,
            'idade': idade,
            'racaId': racaId,
            'classeId': classeId,
            'descricao': descricao,
            'honra': honra,
            'origem': origem,
            'vidaMax': vidaMax,
            'vidaAtual': vidaMax,
            'pesoMax': pesoMax,
            'campanhaId': campanhaId,

        }
    )

    session.commit()
    session.close()

    return jsonify({'sucesso': True})