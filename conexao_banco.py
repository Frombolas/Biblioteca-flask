import psycopg2

conn = psycopg2.connect(
       host="localhost",
       database="biblioteca-flask",
       user='postgres',
       password='123456')

# Abra um cursor para realizar operações de banco de dados
cur = conn.cursor()

# Execute um comando: isso cria uma nova tabela
cur.execute('DROP TABLE IF EXISTS Livros;')
cur.execute('CREATE TABLE Livros (id serial PRIMARY KEY,'
                                'nome varchar (150) NOT NULL,'
                                'genero varchar (50) NOT NULL,'
                                'autor varchar (150) NOT NULL,'
                                'num_paginas integer NOT NULL);'
                                )
cur.execute('DROP TABLE IF EXISTS Usuarios;')
cur.execute('CREATE TABLE Usuarios (id serial PRIMARY KEY,'
                                'nome varchar (150) NOT NULL,'
                                'username varchar (30) NOT NULL,'
                                'senha varchar (30) NOT NULL);'
                                )

# Inserindo dados nas tabelas

cur.execute('INSERT INTO Livros (nome, genero, autor, num_paginas)'
           'VALUES (%s, %s, %s, %s)',
           ('O Estado e a Revolução',
            'Filosofia',
            'Vladmir Lenin',
            216)
           )


cur.execute('INSERT INTO Livros (nome, genero, autor, num_paginas)'
           'VALUES (%s, %s, %s, %s)',
           ('O Capital',
            'Filosofia',
            'Karl Marx',
            752)
           )

cur.execute('INSERT INTO Usuarios (nome, username, senha)'
           'VALUES (%s, %s, %s)',
           ('Gustavo Lopes',
            'gugalps',
            'guga071105')
           )

conn.commit()

cur.close()
conn.close()
