print(' - - - - - - - - - - - -  Uzduotis 4 - -- - - - - - - - - ')
print(' - - - - - - - - - - - -  4. GET ir POST formos su Flask - -- - - - - - - - - ')

# Užduotis:
# 1. Sukurkite maršrutą /paieska, kuris rodo GET formą (forma_get.html).
# 2. Kai vartotojas įveda paieškos frazę ir paspaudžia „Ieškoti“, ji turi būti rodoma
# puslapyje.
# Papildoma užduotis:
# Sukurkite maršrutą /prisijungti, kuris naudoja POST metodą:
# 1. Rodo POST formą (forma_post.html).
# 2. Po prisijungimo parodo pranešimą: "Prisijungėte kaip: [vartotojo
# vardas]".

from flask import Flask, render_template, request

app = Flask(__name__)

valid_users = ['hello', 'labas', 'ate']
@app.route('/')
def home():
    search_text = request.args.get('paieskoslaukelis')
    search_product = request.args.get('produkto_pavadinimas')
    print(search_text)
    print(search_product)
    return render_template('forma_get.html')

@app.route('/paieska', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('forma_get.html')
    elif request.method == 'POST':
        search_text = request.form.get('paieskoslaukelis')
        search_product = request.form.get('produkto_pavadinimas')
        print(search_text)  # for debugging
        print(search_product)  # for debugging
        return render_template('forma_get.html', search_text=search_text, search_product=search_product)


@app.route('/prisijungti', methods=['POST', 'GET'])
def login_user():
    if request.method == 'GET':
        return render_template('forma_post.html')
    elif request.method == 'POST':
        username = request.form.get('loginlaukelis')
        if username in valid_users:
            return render_template('login_result.html', user_login=username)
        else:
            return render_template('forma_post.html', error="Neteisingas vartotojo vardas")


if __name__ == "__main__":
    app.run(debug=True)





















print(' - - - - - - - - - - - -  Uzduotis 5 - -- - - - - - - - - ')


# 5. Paprasta registracijos forma su validacija
# Užduotis:
# 1. Sukurkite maršrutą /registracija, kuris rodo POST formą su laukais:
# a. Vartotojo vardas
# b. Slaptažodis
# c. Pakartotas slaptažodis
# 2. Kai vartotojas užpildo formą, patikrinkite:
# a. Ar visi laukai užpildyti.
# b. Ar slaptažodis sutampa su pakartotu slaptažodžiu.
# 3. Jei viskas gerai, parodykite "Sėkmingai užsiregistravote!", kitu atveju –
# klaidos pranešimą.
# Papildoma užduotis:
# Pridėkite validaciją, kad slaptažodis būtų bent 6 simbolių ilgio.