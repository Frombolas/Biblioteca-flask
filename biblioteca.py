from flask import Flask, render_template, request, redirect, session, flash

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

app.secret_key = 'guga071105'

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
   return redirect('/')


@app.route('/login')
def login():
   return render_template('login.html')


@app.route('/autenticar', methods=["POST",])
def autenticar():
   if '12345' == request.form['senha']:
      session['usuario_logado'] = request.form['usuario']
      flash(request.form['usuario'] + ' logado com sucesso' )
      return redirect('/')
   else:
      flash('senha ou usuario incorretos')
      return redirect('/login')


@app.route('/logout')
def logout():
   session['usuario_logado'] = None
   flash('Logout efetuado com sucesso')
   return redirect('/login')

app.run(debug=True)
