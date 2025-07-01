import sqlite3
condb = sqlite3.connect("banco.db")
cursor = condb.cursor()

def delete_tbl(condb):
    cursor.execute('''
    drop table if exists usuario;
''')
def create_login(condb):
    cursor.execute('''
    create table if not exists usuario(
    id integer primary key autoincrement,
    nome text,
    email text,
    senha text
    );
    ''')



def create_agenda(condb):
     cursor.execute('''
    create table if not exists caixa(
    id integer primary key autoincrement,
    um text,
    dois text,
    tres text,
    quatro text,
    cinco text,
    seis text,
    sete text,
    oito text,
    nove text,
    dez text,
    onze text,
    doze text
    )
    ''')




def insert_data(condb, nome, email, senha):
    cursor.execute('''
    insert into usuario(nome, email, senha) values(?, ?, ?);
    ''', (nome, email, senha))

def verify_data(condb):
    cursor.execute('''
    select * from usuario;
    ''')

    return cursor.fetchall()
def delete_data(condb, id):
    global ids
    ids = int(input("Digite o ID do usuário que deseja excluir: "))
    cursor.execute('''
    delete from usuario where id = ?;
    ''', (id,))

def update_data(condb, id, nome, email, idade):
    cursor.execute('''
    update usuario set nome = ?, email = ?, idade = ? where id = ?;
    ''', (nome, email, idade, id))






create_login(condb)
insert_data(condb, "renan", "renan@example.com", "senha123")
create_agenda(condb)
verify_data(condb)
for row in verify_data(condb):
    print(row)
condb.commit()