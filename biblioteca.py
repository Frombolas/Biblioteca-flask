from flask import Flask, render_template, request

class Livro:
   def __init__(self, nome, genero, autor):
       self.nome = nome
       self.genero = genero
       self.autor = autor

livro1 = Livro('Manifesto do Partido Comunista','Filosofia', 'Karl Marx e Engels')
livro2 = Livro('Às portas da Revolução','Filosofia', 'Vladmir Lenin')
livro3 = Livro('O Capital','Filosofia', 'Karl Marx e Engels')
lista = [livro1, livro2, livro3]


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('lista.html', titulo="Livros", livros=lista)


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='Novo Livro')

@app.route('/criar', methods=["POST",])
def criar():
   nome = request.form['nome']
   genero = request.form['genero']
   autor = request.form['autor']
   livro = Livro(nome, genero, autor)
   lista.append(livro)
   return render_template('lista.html', titulo="Livros", livros=lista)




app.run(debug=True)
