import sqlite3
condb = sqlite3.connect("banco.db")
cursor = condb.cursor()


def create_tbl(condb):
    cursor.execute('''
    create table if not exists usuario(
    id integer primary key autoincrement,
    nome text,
    email text,
    idade integer
    );
    ''')

def insert_data(condb, nome, email, idade):
    cursor.execute('''
    insert into usuario(nome, email, idade) values(?, ?, ?);
    ''', (nome, email, idade))

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






create_tbl(condb)

verify_data(condb,)
for row in verify_data(condb):
    print(row)
condb.commit()