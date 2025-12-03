import pymysql
from flask import Flask, jsonify, request
from config.bd_configuracao import bd_conexao

app = Flask(__name__)
app.json.sort_keys = False


# create, read, update e delete

# get, post, delete e put 

#     MUSICA 

@app.route('/Musica', methods = ['POST'])
def create_musica():
    """ 
    adiciona uma nova musica

    """
    try:
        _json = request.json
        _musica = _json.get('nome_musica')
        _streamings_numero = _json.get('streamings_numero')
        _duracao = _json.get('duracao')
        _id_album = _json.get('id_album')

        if _id_album and _duracao and _streamings_numero and _musica and request.method == 'POST':

            sql = "INSERT INTO `Unify`.`Musica` (nome_musica, streamings_numero, duracao, id_album) VALUES (%s, %s, %s, %s)"
            data = (_musica, _streamings_numero, _duracao, _id_album)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
          
            resposta = {
            'erro': False,
            'mensagem': 'musica lancada com sucesso',
            'data': _json
            }
        return jsonify(resposta), 201
    
    except Exception as e:
       resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
    return jsonify(resposta), 500
        

@app.route('/Musica', methods = ['GET'])
def get_musica():

   try:
       conn = bd_conexao()
       cursor = conn.cursor(pymysql.cursors.DictCursor)
       cursor.execute('SELECT * FROM `Unify`.`Musica`')
       rows = cursor.fetchall()

       lista_bonitinha = []
      

      # musica = [{'id': musica[0], 'nome': musica[1], 'streamings': musica [2], 'duracao': musica [3], 'id_album': musica [4]} for musica in data]

       for row in rows:
            
            time_para_str = str(row['duracao']) if row['duracao'] else '00:00:00'

            musica_organizadinha = {
                'id': row['id'],
                'nome_musica': row['nome_musica'],
                'streamings_numero': row['streamings_numero'],
                'duracao': time_para_str,
                'id_album': row['id_album']
            }
            lista_bonitinha.append(musica_organizadinha)

       cursor.close()
       conn.close()

       resposta = {
           'erro': False,
           'mensagem': 'musicas listadas com sucesso',
           'data': lista_bonitinha
        }
       return jsonify(resposta), 200
   
   except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500
       
       
@app.route('/Musica/<int:musica_id>', methods = ['PUT'])
def put_musica(musica_id):
    try:
        _json = request.json
        _musica = _json.get('nome_musica')
        _streamings_numero = _json.get('streamings_numero')
        _duracao = _json.get('duracao')
        _id_album = _json.get('id_album')

        if _id_album and _duracao and _streamings_numero and _musica and request.method == 'PUT':

            sql = ('UPDATE `Unify`.`Musica` SET nome_musica = %s, streamings_numero = %s, duracao = %s, id_album = %s WHERE id = %s')
            data = (_musica, _streamings_numero, _duracao, _id_album, musica_id)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()

            resposta = {
            'erro': False,
            'mensagem': 'musica atualizada com sucesso',
            'data': { 'musica_id' : musica_id}
            }
            return jsonify(resposta), 201
        else:
            return jsonify({'erro':True, 'mensagem': 'falta dados para atualizar'})
    
    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500

@app.route('/Musica/<int:musica_id>', methods = ['DELETE'])
def del_musica(musica_id):
    try:
        sql = ('DELETE FROM `Unify`.`Musica` WHERE id = %s')
        data = (musica_id,)

        conn = bd_conexao()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

        resposta = {
                'erro': False,
                'mensagem': 'musica excluida com sucesso',
                'data': { 'musica_id' : musica_id}
                }
        return jsonify(resposta), 201

    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500
    
#   ARTISTA

@app.route('/Artista', methods = ['POST'])
def create_artista():
    """ 
    adiciona um nova artista

    """
    try:
        _json = request.json
        _artista = _json.get('nome_artista')
        _pais = _json.get('pais')
        _streamings_mensal= _json.get('streamings_mensal')
     
        if _streamings_mensal and _pais and _artista and request.method == 'POST':

            sql = "INSERT INTO `Unify`.`Artista` (nome_artista, pais, streamings_mensal) VALUES (%s, %s, %s)"
            data = (_artista, _pais, _streamings_mensal)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
          
            resposta = {
            'erro': False,
            'mensagem': 'artista cadastrado com sucesso',
            'data': _json
            }
        return jsonify(resposta), 201
    
    except Exception as e:
       resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
    return jsonify(resposta), 500

@app.route('/Artista', methods = ['GET'])
def get_artista():
   try:
       conn = bd_conexao()
       cursor = conn.cursor(pymysql.cursors.DictCursor)
       cursor.execute('SELECT * FROM `Unify`.`Artista`')
       rows = cursor.fetchall()

       lista_bonitinha = []

       for row in rows:

            artista_organizadinho = {
                'id': row['id'],
                'nome_artista': row['nome_artista'],
                'pais': row['pais'],
                'streamings_mensal': row['streamings_mensal']
            }
            lista_bonitinha.append(artista_organizadinho)

       cursor.close()
       conn.close()

       resposta = {
           'erro': False,
           'mensagem': 'artista listados com sucesso',
           'data': lista_bonitinha
        }
       return jsonify(resposta), 200
   
   except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500
   
@app.route('/Artista/<int:artista_id>', methods = ['PUT'])
def put_artista(artista_id):
    try:
        _json = request.json
        _artista = _json.get('nome_artista')
        _pais = _json.get('pais')
        _streamings_mensal= _json.get('streamings_mensal')

        if _streamings_mensal and _pais and _artista and request.method == 'PUT':

            sql = ('UPDATE `Unify`.`Artista` SET nome_artista = %s, pais = %s, streamings_mensal = %s WHERE id = %s')
            data = (_artista, _pais, _streamings_mensal, artista_id)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()

            resposta = {
            'erro': False,
            'mensagem': 'artista atualizado com sucesso',
            'data': { 'artista_id' : artista_id}
            }
            return jsonify(resposta), 201
        else:
            return jsonify({'erro':True, 'mensagem': 'falta dados para atualizar'})
    
    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500

@app.route('/Artista/<int:artista_id>', methods = ['DELETE'])
def del_artista(artista_id):
    try:
        sql = ('DELETE FROM `Unify`.`Artista` WHERE id = %s')
        data = (artista_id,)

        conn = bd_conexao()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

        resposta = {
                'erro': False,
                'mensagem': 'artista excluido com sucesso',
                'data': { 'artista_id' : artista_id}
                }
        return jsonify(resposta), 201

    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500
    
#  GENERO
       
@app.route('/Genero', methods = ['POST'])
def create_genero():
    """ 
    adiciona um novo genero

    """
    try:
        _json = request.json
        _nome_genero = _json.get('nome_genero')
        _descricao = _json.get('descricao')
     
        if _descricao and _nome_genero and request.method == 'POST':

            sql = "INSERT INTO `unify`.`Genero` (nome_genero, descricao) VALUES (%s, %s)"
            data = (_nome_genero, _descricao)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
          
            resposta = {
            'erro': False,
            'mensagem': 'genero cadastrado com sucesso',
            'data': _json
            }
        return jsonify(resposta), 201
    
    except Exception as e:
       resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
    return jsonify(resposta), 500

@app.route('/Genero', methods = ['GET'])
def get_genero():
   try:
       conn = bd_conexao()
       cursor = conn.cursor(pymysql.cursors.DictCursor)
       cursor.execute('SELECT * FROM `Unify`.`Genero`')
       rows = cursor.fetchall()

       lista_bonitinha = []

       for row in rows:

            genero_organizadinho = {
                'id': row['id'],
                'nome_genero': row['nome_genero'],
                'descricao': row['descricao'],
            }
            lista_bonitinha.append(genero_organizadinho)

       cursor.close()
       conn.close()

       resposta = {
           'erro': False,
           'mensagem': 'generos listados com sucesso',
           'data': lista_bonitinha
        }
       return jsonify(resposta), 200
   
   except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500
   
@app.route('/Genero/<int:genero_id>', methods = ['PUT'])
def put_genero(genero_id):
    try:
        _json = request.json
        _nome_genero = _json.get('nome_genero')
        _descricao = _json.get('descricao')

        if _descricao and _nome_genero and request.method == 'PUT':

            sql = ('UPDATE `Unify`.`Genero` SET nome_genero = %s, descricao = %s WHERE id = %s')
            data = (_nome_genero, _descricao, genero_id)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()

            resposta = {
            'erro': False,
            'mensagem': 'genero atualizado com sucesso',
            'data': { 'genero_id' : genero_id}
            }
            return jsonify(resposta), 201
        else:
            return jsonify({'erro':True, 'mensagem': 'falta dados para atualizar'})
    
    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500

@app.route('/Genero/<int:genero_id>', methods = ['DELETE'])
def del_genero(genero_id):
    try:
        sql = ('DELETE FROM `Unify`.`Genero` WHERE id = %s')
        data = (genero_id,)

        conn = bd_conexao()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

        resposta = {
                'erro': False,
                'mensagem': 'genero excluido com sucesso',
                'data': { 'genero_id' : genero_id}
                }
        return jsonify(resposta), 201

    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500
    
#   ALBUM

@app.route('/Album', methods = ['POST'])
def create_album():
    """ 
    adiciona um novo album

    """
    try:
        _json = request.json
        _nome_album = _json.get('nome_album')
        _ano_lancamento = _json.get('ano_lancamento')
        _id_artista = _json.get("id_artista")
        _id_genero = _json.get("id_genero")
     
        if _id_genero and _id_artista and _ano_lancamento and _nome_album and request.method == 'POST':

            sql = "INSERT INTO `unify`.`Album` (nome_album, ano_lancamento, id_artista, id_genero) VALUES (%s, %s, %s, %s)"
            data = (_nome_album, _ano_lancamento, _id_artista, _id_genero)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
          
            return jsonify({'erro': False, 'mensagem': 'Album criado!', 'data': _json}), 201
    
    except Exception as e:
       resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
    return jsonify(resposta), 500

@app.route('/Album', methods = ['GET'])
def get_album():
   try:
       conn = bd_conexao()
       cursor = conn.cursor(pymysql.cursors.DictCursor)
       cursor.execute('SELECT * FROM `Unify`.`Album`')
       rows = cursor.fetchall()

       lista_bonitinha = []

       for row in rows:

            album_organizadinho = {
                'id': row['id'],
                'nome_album': row['nome_album'],
                'ano_lancamento': row['ano_lancamento'],
                'id_artista' : row['id_artista'],
                'id_genero': row['id_genero']
            }
            lista_bonitinha.append(album_organizadinho)

       cursor.close()
       conn.close()

       resposta = {
           'erro': False,
           'mensagem': 'album listados com sucesso',
           'data': lista_bonitinha
        }
       return jsonify(resposta), 200
   
   except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500
   
@app.route('/Album/<int:album_id>', methods = ['PUT'])
def put_album(album_id):
    try:
        _json = request.json
        _nome_album = _json.get('nome_album')
        _ano_lancamento = _json.get('ano_lancamento')
        _id_artista = _json.get("id_artista")
        _id_genero = _json.get("id_genero")

        if _id_genero and _id_artista and _ano_lancamento and _nome_album and request.method == 'PUT':

            sql = ('UPDATE `Unify`.`Album` SET nome_album = %s, ano_lancamento = %s, id_artista = %s, id_genero = %s WHERE id = %s')
            data = (_nome_album, _ano_lancamento, _id_artista, _id_genero, album_id)

            conn = bd_conexao()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()

            resposta = {
            'erro': False,
            'mensagem': 'album atualizado com sucesso',
            'data': { 'album_id' : album_id}
            }
            return jsonify(resposta), 201
        else:
            return jsonify({'erro':True, 'mensagem': 'falta dados para atualizar'})
    
    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500

@app.route('/Album/<int:album_id>', methods = ['DELETE'])
def del_album(album_id):
    try:
        sql = ('DELETE FROM `Unify`.`Album` WHERE id = %s')
        data = (album_id,)

        conn = bd_conexao()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()

        resposta = {
                'erro': False,
                'mensagem': 'album excluido com sucesso',
                'data': { 'album_id' : album_id}
                }
        return jsonify(resposta), 201

    except Exception as e:    
        resposta = {
           'erro': False,
           'mensagem': f'um erro ocorreu: {e}',
           'data': None
        }
        return jsonify(resposta), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)