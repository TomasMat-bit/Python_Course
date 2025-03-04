print(' - - - - - Flask pagrindai – maršrutai, šablonai ir formos - - - - - - ')
print(' - - - - - 2. Flask aplikacijų kodas - - - - - - ')

# from flask import Flask
#
# app = Flask(__name__)

# # # https:///gothub.com/contacts/
# # @app.route('/contacts')
#
# # https:///gothub.com/
#
# @app.route('/')
# def home():
#     return 'Hello World from my first FLASK webApp !!!\nHOMEPAGE'
#
# @app.route('/news')
# def news():
#     return 'Cia pagrindinis naujienu puslapis'
#
# @app.route('/products/<int:item>')
# def news_item(item):
#     return f'Cia naujiena NR {item}'
#
# @app.route('/<text>')
# def any_route(text):
#     return f'Jus surinkote marsruta {text}. Jokio resurso cia nera. '
#
#
#
# # if __name__ == '__main__':
# app.run()


print(' - - - - - 3. HTML failai naudojami Flask aplikacijose - - - - - - ')

# @app.route('/')
# def home():
#     return '<h1> HOME PAGE </h1> <p>Hello World !!!</p> <p>Cia mano pirmas FLAK</p>' \
#             '<p><a href="verslas"> Pereiti i verslo skyriu </a></p>'\
#             "<p><a href='/verslas/nekilnojamas-turtas'>Pereiti i NT poskyris</a></p>"
#
# @app.route('/verslas')
# def verslas():
#     return '<h1> Verslo skyrius</h1> <p>Verslo naujienos</p>'\
#             '<p><a href="/"> grizti i pradini</a></p>'\
#             "<p><a href='/verslas/nekilnojamas-turtas'>Pereiti i NT poskyris</a></p>"
#
# @app.route('/verslas/nekilnojamas-turtas')
# def verslas_nt():
#     return "<h1>Verslo skyrius</h1><h2>NT poskyris</h2>" \
#            "<p><a href='/'>grizti i pradini</a></p>" \
#            "<p><a href='/verslas'>Pereiti i verslo skyriu</a></p>"
#
#
# app.run()

print(' - - - - - 3. HTML failai naudojami Flask aplikacijose - - - - - - ')
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/vardusarasas')
def names_list():
    names = ['Adomas', 'Antanas', 'Valdas', 'Jonas']

    return render_template('vardai.html', names_for_template=names)


app.run()