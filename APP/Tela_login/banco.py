import sqlite3
condb = sqlite3.connect("banco.db")
cursor = condb.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

def delete_tbl(condb):
    cursor = condb.cursor()
    cursor.execute('DROP TABLE IF EXISTS usuario;')
    condb.commit()

# CRUD USUARIO
def create_usuario(condb):
    cursor = condb.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        senha TEXT NOT NULL)
        ''')
    condb.commit()
def insert_usuario(condb, nome, email, senha):
    cursor = condb.cursor()
    cursor.execute('INSERT INTO usuario(nome, email, senha) VALUES (?, ?, ?);', (nome, email, senha))
    condb.commit()
def verify_usuario(condb):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM usuario;')
    return cursor.fetchall()
def update_usuario(condb, id, nome, email, senha):
    cursor = condb.cursor()
    cursor.execute('UPDATE usuario SET nome = ?, email = ?, senha = ? WHERE id = ?;', (nome, email, senha, id))
    condb.commit()
def delete_usuario(condb, id):
    cursor = condb.cursor()
    cursor.execute('DELETE FROM usuario WHERE id = ?;', (id,))
    condb.commit()

# CRUD METODO
def create_metodo(condb):
    cursor = condb.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS metodo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL CHECK(nome IN ('Pomodoro', 'Feynman', 'Pareto')))
    ''')
    condb.commit()
def insert_metodo(condb, nome):
    cursor = condb.cursor()
    cursor.execute('INSERT INTO metodo(nome) VALUES (?);', (nome,))
    condb.commit()
def verify_metodo(condb):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM metodo;')
    return cursor.fetchall()
def update_metodo(condb, id, nome):
    cursor = condb.cursor()
    cursor.execute('UPDATE metodo SET nome = ? WHERE id = ?;', (nome, id))
    condb.commit()
def delete_metodo(condb, id):
    cursor = condb.cursor()
    cursor.execute('DELETE FROM metodo WHERE id = ?;', (id,))
    condb.commit()

# CRUD POMODORO
def create_pomodoro(condb):
    cursor = condb.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pomodoro (
    id_metodo INTEGER PRIMARY KEY,
    tempo_trabalho INTEGER NOT NULL,
    tempo_descanso INTEGER NOT NULL,
    ciclos INTEGER NOT NULL,
    FOREIGN KEY (id_metodo) REFERENCES metodo(id))
    ''')
    condb.commit()
def insert_pomodoro(condb, id, tempo_trabalho, tempo_descanso, ciclos):
    cursor = condb.cursor()
    cursor.execute('INSERT INTO pomodoro VALUES (?, ?, ?, ?);', (id, tempo_trabalho, tempo_descanso, ciclos))
    condb.commit()
def verify_pomodoro(condb):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM pomodoro;')
    return cursor.fetchall()
def update_pomodoro(condb, id, tempo_trabalho, tempo_descanso, ciclos):
    cursor = condb.cursor()
    cursor.execute('''
    UPDATE pomodoro SET tempo_trabalho = ?, tempo_descanso = ?, ciclos = ? WHERE id_metodo = ?;
    ''', (tempo_trabalho, tempo_descanso, ciclos, id))
    condb.commit()
def delete_pomodoro(condb, id):
    cursor = condb.cursor()
    cursor.execute('DELETE FROM pomodoro WHERE id_metodo = ?;', (id,))
    condb.commit()

# CRUD FEYNMAN
def create_feynman(condb):
    cursor = condb.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feynman (
    id_metodo INTEGER PRIMARY KEY,
    conceito TEXT NOT NULL,
    modo_explicacao TEXT, 
    estrategia_revisao TEXT,
    FOREIGN KEY (id_metodo) REFERENCES metodo(id))
    ''')
    condb.commit()
def insert_feyman(condb, id, conceito, modo_explicacao, estrategia_revisao):
    cursor = condb.cursor()
    cursor.execute('INSERT INTO feynman VALUES (?, ?, ?, ?);', (id, conceito, modo_explicacao, estrategia_revisao))
    condb.commit()
def verify_feynman(condb):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM feynman;')
    return cursor.fetchall()
def update_feynman(condb, id, conceito, modo_explicacao, estrategia_revisao):
    cursor = condb.cursor()
    cursor.execute('''
    UPDATE feynman SET conceito = ?, modo_explicacao = ?, estrategia_revisao = ? WHERE id_metodo = ?;
    ''', (conceito, modo_explicacao, estrategia_revisao, id))
    condb.commit()
def delete_feynman(condb, id):
    cursor = condb.cursor()
    cursor.execute('DELETE FROM feynman WHERE id_metodo = ?;', (id,))
    condb.commit()

# CRUD PARETO
def create_pareto(condb):
    cursor = condb.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pareto (
    id_metodo INTEGER PRIMARY KEY,
    percentual_foco INTEGER NOT NULL,
    impacto TEXT,
    FOREIGN KEY (id_metodo) REFERENCES metodo(id))
    ''')
    condb.commit()
def insert_pareto(condb, id, percentual_foco, impacto):
    cursor = condb.cursor()
    cursor.execute('INSERT INTO pareto VALUES (?, ?, ?);', (id, percentual_foco, impacto))
    condb.commit()
def verify_pareto(condb):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM pareto;')
    return cursor.fetchall()
def update_pareto(condb, id, percentual_foco, impacto):
    cursor = condb.cursor()
    cursor.execute('UPDATE pareto SET percentual_foco = ?, impacto = ? WHERE id_metodo = ?;', (percentual_foco, impacto, id))
    condb.commit()
def delete_pareto(condb, id):
    cursor = condb.cursor()
    cursor.execute('DELETE FROM pareto WHERE id_metodo = ?;', (id,))
    condb.commit()

#CRUD REFERENCIAS
def create_referencias(condb):
    cursor.execute('''
    create table if not exists referencias(
    id integer primary key autoincrement,
    nome text not null,
    referencias_link text unique key not null
    )''')
    condb.commit()
def insert_referencias(condb, referencias_link):
    cursor.execute('''
    INSERT INTO referencias(referencias_link) VALUES (?,?,?)
''',(referencias_link))
    condb.commit()
def verify_referencias(condb):
    cursor.execute('''
    SELECT * FROM referencias;
''')
    return cursor.fetchall()
def update_referencias(condb, referencias_link, id):
    cursor.execute('''
    UPDATE metodo SET referencias_link = ? = ?
    WHERE id = ?
''',(referencias_link, id))
    condb.commit
def delete_referencias(condb, id):
    cursor.execute('''
    DELETE FROM referencias WHERE id = ?;
''', (id,))
    condb.commit()

#CRUD PLAYLIST
def create_playlist(condb):
    cursor.execute('''
    create table if not exists playlist(
        nome text not null unique key,
        id integer primary key autoincrement,
        link_p text not null
        )
        ''')
    condb.commit()
def insert_playlist(condb, link_p, nome):
  cursor.execute('''
  INSERT INTO playlist(link_p, nome) VALUES (?,?)
  ''', (link_p,nome))
  condb.commit()
def verify_playlist(condb):
  cursor.execute('''
  SELECT * FROM playlist;
  ''')
  return cursor.fetchall()
def update_playlist(nome,condb,link_p,id):
  cursor.execute('''
  UPDATE playlist SET nome = ?, link_p = ? WHERE id = ?;
  ''', (nome,link_p,id))
  condb.commit()
def delete_playlist(condb,id):
  cursor.execute('''
  DELETE FROM playlist WHERE id = ?
  ''',(id,))
  condb.commit()

#CRUD ASSUNTO
def create_assunto(condb):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS assunto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE KEY NOT NULL,
    disciplina TEXT NOT NULL,
    id_usuario INTEGER NOT NULL,
    id_metodo INTEGER NOT NULL,
    id_referencias INTEGER NOT NULL,
    id_playlist INTEGER NULL,
    
    FOREIGN (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_playlist) REFERENCES playlist(id),
    FOREIGN KEY (id_referencia) REFERENCES referencia(id),
    FOREIGN KEY (id_metodo) REFERENCES metodo(id)
    )
''')
    condb.commit()
def insert_assunto(condb, nome, disciplina, id_usuario, id_playlist, id_referencia, id_metodo):
    cursor = condb.cursor()
    cursor.execute('''
        INSERT INTO assunto (nome, disciplina, id_usuario, id_playlist, id_referencia, id_metodo)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', (nome, disciplina, id_usuario, id_playlist, id_referencia, id_metodo))
    condb.commit()
def verify_assuntos(condb):
    cursor = condb.cursor()
    cursor.execute('''
        SELECT * FROM assunto;
    ''')
    return cursor.fetchall()
def update_assunto(condb, nome, disciplina, id_playlist, id_referencia, id_metodo, id):
    cursor = condb.cursor()
    cursor.execute('''
        UPDATE assunto
        SET nome = ?, disciplina = ?, id_playlist = ?, id_referencia = ?, id_metodo = ?
        WHERE id = ?;
    ''', (nome, disciplina, id_playlist, id_referencia, id_metodo, id))
    condb.commit()
def delete_assunto(condb, id):
    cursor = condb.cursor()
    cursor.execute('''
        DELETE FROM assunto WHERE id = ?;
    ''', (id,))
    condb.commit()



def create_agenda(condb):
    cursor.execute('''
    create table if not exists caixa(
    id integer primary key autoincrement,
    um text null,
    dois text null,
    tres text null,
    quatro text null,
    cinco text null,
    seis text null,
    sete text null,
    oito text null,
    nove text null,
    dez text null,
    onze text null,
    doze text null
    )
    ''')


def insert_caixa(condb,um = "Livre", dois = "Livre", tres = "Livre", quatro = "Livre", cinco = "Livre", seis = "Livre", sete = "Livre", oito = "Livre", nove = "Livre", dez = "Livre", onze = "Livre", doze = "Livre"):
    cursor.execute('''
    insert into caixa(um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez, onze, doze) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);
    ''', (um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez, onze, doze))


    cursor.execute('''
    select * from metodo;
    ''')
    return cursor.fetchall()



def create_organização(condb):
    cursor.execute('''
    create table if not exists organizaçao(
        id integer primary key autoincrement,
        tipo text not null,
        nome text not null
    )
    ''')



def verify_caixa(condb):
    cursor.execute('''
    select * from caixa;
    ''')
    return cursor.fetchall()


create_usuario(condb)
create_assunto(condb)
create_metodo(condb)
create_pomodoro(condb)
create_feynman(condb)
create_pareto(condb)
create_referencias(condb)
create_playlist(condb)

