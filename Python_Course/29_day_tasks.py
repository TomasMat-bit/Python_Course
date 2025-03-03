# print(' - - - - - - - - - UZDUOTIS 1 - - - - - - - - -  - - -- - - -  ')
# # 1. Pagrindiniai maršrutai ir dinaminių parametrų naudojimas
# # Užduotis:
# # Sukurkite Flask aplikaciją, kurioje būtų šie maršrutai:
# # 1. Pagrindinis puslapis /, kuris grąžina "Sveiki atvykę į Flask aplikaciją!".
# # 2. Puslapis /apie, kuris grąžina "Tai yra apie mus puslapis.".
# # 3. Puslapis /vartotojas/<vardas>, kuris priima vartotojo vardą ir grąžina "Sveiki,
# # [vardas]!".
# # 4. Puslapis /skaicius/<int:nr>, kuris priima skaičių ir grąžina "Jūs įvedėte
# # skaičių: [nr]".
# # Papildoma užduotis:
# # Sukurkite maršrutą /kelione/<start>/<end>, kuris grąžina "Kelionės maršrutas:
# # iš [start] į [end]".
#
# from flask import Flask
#
# app = Flask(__name__)
#
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return 'Sveiki atvykę į Flask aplikaciją! !!!\nHOMEPAGE'
#
# @app.route('/apie')
# def apie():
#     return 'Tai yra apie mus puslapis.'
#
# @app.route('/vartotojas/<vardas>')
# def vartotojas(vardas):
#     return f'Sveiki, {vardas}!'
#
# @app.route('/skaicius/<int:nr>')
# def skaicius(nr):
#     return f'Jūs įvedėte skaičių: {nr}.'
#
# @app.route('/kelione/<start>/<end>')
# def kelione(start, end):
#     return f'Kelionės maršrutas: iš {start} į {end}.'
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# # if __name__ == '__main__':
# app.run()

print(' - - - - - - - - - UZDUOTIS 2 - - - - - - - - -  - - -- - - -  ')

# 2. HTML atsakymas ir nuorodos tarp puslapių
# Užduotis:
# 1. Sukurkite maršrutą /pagrindinis, kuris grąžina HTML su:
# a. Antrašte „Mano Flask puslapis“
# b. Paragrafu „Tai yra pagrindinis puslapis“
# c. Nuoroda į /apie puslapį.
# Papildoma užduotis:
# Pridėkite nuorodas į /vartotojas/<vardas> ir /skaicius/<int:nr> maršrutus.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Mano Flask puslapis</h1>' \
           '<p>Tai yra pagrindinis puslapis</p>' \
           '<p>Cia mano pirmas Flask projektas</p>' \
           '<p><a href="/apie">Apie puslapį</a></p>' \
           "<p><a href='/vartotojas/Argoras'>Pereiti į Vartotojo poskyrį</a></p>" \
           "<p><a href='/skaicius/10'>Pereiti į Skaičių poskyrį</a></p>"

@app.route('/apie')
def apie():
    return '<h1>Apie Puslapį</h1>' \
           '<p>Nuo ko susikūrė šis puslapis ir kas čia yra.</p>' \
           '<p><a href="/">Grįžti į pradinį puslapį</a></p>'

@app.route('/vartotojas/<vardas>')
def vartotojas(vardas):
    return f"<h1>Vartotojo Duomenys</h1><h2>Laba diena, {vardas}!</h2>" \
           '<p><a href="/">Grįžti į pradinį puslapį</a></p>'

@app.route('/skaicius/<int:nr>')
def skaicius(nr):
    return f"<h1>Skaicių skyrius</h1><h2>Jūs įvedėte skaičių: {nr}</h2>" \
           '<p><a href="/">Grįžti į pradinį puslapį</a></p>'

@app.route('/pagrindinis')
def pagrindinis():
    return '<h1>Mano Flask puslapis</h1>' \
           '<p>Tai yra pagrindinis puslapis</p>' \
           '<p><a href="/apie">Apie puslapį</a></p>' \
           "<p><a href='/vartotojas/Argoras'>Pereiti į Vartotojo poskyrį</a></p>" \
           "<p><a href='/skaicius/10'>Pereiti į Skaičių poskyrį</a></p>"

if __name__ == '__main__':
    app.run(debug=True)

