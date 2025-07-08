import sqlite3
condb = sqlite3.connect("banco.db")
cursor = condb.cursor()
def delete_tbl(condb):
    cursor.execute('''
    drop table if exists usuario;
''')
def create_fonte():
    cursor.execute('''
    create table if not exists(
    id integer primary key autoincrement,
    
                   )

    ''')



def create_metodo(condb):
    cursor.execute('''
    create table if not exists metodo(
    id integer primary key autoincrement,
    escolha integer not null,
    favorito boolean null)
    ''')
def create_login(condb):
    cursor.execute('''
    create table if not exists usuario(
    id integer primary key autoincrement,
    nome text not null,
    email text not null,
    senha text not null
    ''')



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






def insert_usuario(condb, nome, email, senha):
    cursor.execute('''
    insert into usuario(nome, email, senha) values(?, ?, ?);
    ''', (nome, email, senha))


def insert_caixa(condb,um = "", dois = "", tres = "", quatro = "", cinco = "", seis = "", sete = "", oito = "", nove = "", dez = "", onze = "", doze = ""):
    cursor.execute('''
    insert into caixa(um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez, onze, doze) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);
    ''', (um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez, onze, doze))


def insert_metodo(condb, metodo):
    cursor.execute('''
    insert into metodo(metodo) values(?);
    ''', (metodo,))

def verify_usuario(condb):
    cursor.execute('''
    select * from usuario;
    ''')
    return cursor.fetchall()


def verify_metodo(condb):
    cursor.execute('''
    select * from metodo;
    ''')
    return cursor.fetchall()



def verify_caixa(condb):
    cursor.execute('''
    select * from caixa;
    ''')
    return cursor.fetchall()


def delete_usuario(condb, id):
    global ids
    ids = int(input("Digite o ID do usuário que deseja excluir: "))
    cursor.execute('''
    delete from usuario where id = ?;
    ''', (id,))



def update_usuario(condb, id, nome, email, idade):
    cursor.execute('''
    update usuario set nome = ?, email = ?, idade = ? where id = ?;
    ''', (nome, email, idade, id))






create_login(condb)
create_agenda(condb)
create_metodo(condb)
insert_usuario(condb, "renan", "renan@example", "senha123")
insert_caixa(condb, "estudar geografia", "estudar matematica", "estudar portugues", "estudar ingles", "estudar historia", "estudar quimica", "estudar fisica", "estudar biologia", "estudar filosofia", "estudar sociologia", "estudar artes", "estudar educacao fisica")
insert_metodo(condb, 1)
for row in verify_caixa(condb):
    print(row)
for row in verify_usuario(condb):
    print(row)
for row in verify_metodo(condb):
    print(row)
condb.commit()