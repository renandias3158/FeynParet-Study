import sqlite3
condb = sqlite3.connect("banco.db", check_same_thread=False)
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
        senha TEXT NOT NULL);
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
def update_usuario(condb, id, n_nome, n_email, n_senha, email, senha):
    cursor = condb.cursor()
    cursor.execute('UPDATE usuario SET nome = ?, email = ?, senha = ? WHERE id = ? OR (email = ? AND senha = ?);', (n_nome, n_email, n_senha, id, email, senha))
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
        nome TEXT NOT NULL CHECK(nome IN ('Pomodoro', 'Feynman', 'Pareto')));
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
    FOREIGN KEY (id_metodo) REFERENCES metodo(id));
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
    FOREIGN KEY (id_metodo) REFERENCES metodo(id));
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
    FOREIGN KEY (id_metodo) REFERENCES metodo(id));
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
    cursor = condb.cursor()
    cursor.execute('''
    create table if not exists referencias(
    id integer primary key autoincrement,
    nome text not null,
    referencias_link text unique not null
    );''')
    condb.commit()
def insert_referencias(condb,nome, referencias_link):
    cursor = condb.cursor()
    cursor.execute('''
    INSERT INTO referencias(nome, referencias_link) VALUES (?,?)
''',(nome, referencias_link))
    condb.commit()
def verify_referencias(condb):
    cursor = condb.cursor()
    cursor.execute('''
    SELECT * FROM referencias;
''')
    return cursor.fetchall()
def update_referencias(condb, nome,referencias_link, id):
    cursor = condb.cursor()
    cursor.execute('''
    UPDATE referencias SET nome = ?, referencias_link = ?
    WHERE id = ?
''',(nome,referencias_link, id))
    condb.commit()
def delete_referencias(condb, id):
    cursor = condb.cursor()
    cursor.execute('''
    DELETE FROM referencias WHERE id = ?;
''', (id,))
    condb.commit()

#CRUD PLAYLIST
def create_playlist(condb):
    cursor = condb.cursor()
    cursor.execute('''
    create table if not exists playlist(
        nome text not null unique,
        id integer primary key autoincrement,
        link_p text not null
        );
        ''')
    condb.commit()
def insert_playlist(condb, link_p, nome):
  cursor = condb.cursor()
  cursor.execute('''
  INSERT INTO playlist(link_p, nome) VALUES (?,?)
  ''', (link_p,nome))
  condb.commit()
def verify_playlist(condb):
  cursor = condb.cursor()
  cursor.execute('''
  SELECT * FROM playlist;
  ''')
  return cursor.fetchall()
def update_playlist(condb,nome,link_p,id):
  cursor = condb.cursor()
  cursor.execute('''
  UPDATE playlist SET nome = ?, link_p = ? WHERE id = ?;
  ''', (nome,link_p,id))
  condb.commit()
def delete_playlist(condb,id):
  cursor = condb.cursor()
  cursor.execute('''
  DELETE FROM playlist WHERE id = ?
  ''',(id,))
  condb.commit()

#CRUD ASSUNTO
def create_assunto(condb):
    cursor = condb.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS assunto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    disciplina TEXT NOT NULL,
    id_usuario INTEGER NOT NULL,
    id_metodo INTEGER NOT NULL,
    id_referencias INTEGER NOT NULL,
    id_playlist INTEGER NULL,
    
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_playlist) REFERENCES playlist(id),
    FOREIGN KEY (id_referencias) REFERENCES referencias(id),
    FOREIGN KEY (id_metodo) REFERENCES metodo(id)
    );
''')
    condb.commit()
def insert_assunto(condb, nome, disciplina, id_usuario, id_playlist, id_referencias, id_metodo):
    cursor = condb.cursor()
    cursor.execute('''
        INSERT INTO assunto (nome, disciplina, id_usuario, id_playlist, id_referencias, id_metodo)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', (nome, disciplina, id_usuario, id_playlist, id_referencias, id_metodo))
    condb.commit()
def verify_assuntos(condb):
    cursor = condb.cursor()
    cursor.execute('''
        SELECT * FROM assunto;
    ''')
    return cursor.fetchall()
def update_assunto(condb, nome, disciplina, id_playlist, id_referencias, id_metodo, id):
    cursor = condb.cursor()
    cursor.execute('''
        UPDATE assunto
        SET nome = ?, disciplina = ?, id_playlist = ?, id_referencias = ?, id_metodo = ?
        WHERE id = ?;
    ''', (nome, disciplina, id_playlist, id_referencias, id_metodo, id))
    condb.commit()
def delete_assunto(condb, id):
    cursor = condb.cursor()
    cursor.execute('''
        DELETE FROM assunto WHERE id = ?;
    ''', (id,))
    condb.commit()

# USUÁRIO (por email e senha)
def verifica_usuario(email, senha):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM usuario WHERE email = ? AND senha = ?;', (email, senha))
    return cursor.fetchone()

# METODO (por nome)
def verifica_metodo(nome):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM metodo WHERE nome = ?;', (nome,))
    return cursor.fetchone()

# POMODORO (por id_metodo)
def verifica_pomodoro(id_metodo):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM pomodoro WHERE id_metodo = ?;', (id_metodo,))
    return cursor.fetchone()

# FEYNMAN (por id_metodo)
def verifica_feynman(id_metodo):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM feynman WHERE id_metodo = ?;', (id_metodo,))
    return cursor.fetchone()

# PARETO (por id_metodo)
def verifica_pareto(id_metodo):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM pareto WHERE id_metodo = ?;', (id_metodo,))
    return cursor.fetchone()

# REFERENCIAS (por link ou por nome)
def verifica_referencias_por_link(link):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM referencias WHERE referencias_link = ?;', (link,))
    return cursor.fetchone()

def verifica_referencias_por_nome(nome):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM referencias WHERE nome = ?;', (nome,))
    return cursor.fetchone()

# PLAYLIST (por nome ou link)
def verifica_playlist_por_nome(nome):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM playlist WHERE nome = ?;', (nome,))
    return cursor.fetchone()

def verifica_playlist_por_link(link_p):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM playlist WHERE link_p = ?;', (link_p,))
    return cursor.fetchone()

# ASSUNTO (por nome)
def verifica_assunto(nome):
    cursor = condb.cursor()
    cursor.execute('SELECT * FROM assunto WHERE nome = ?;', (nome,))
    return cursor.fetchone()





create_usuario(condb)
create_metodo(condb)
create_pomodoro(condb)
create_feynman(condb)
create_pareto(condb)
create_referencias(condb)
create_playlist(condb)
create_assunto(condb)


condb.commit()