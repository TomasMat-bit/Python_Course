from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def home():
#     # return '<h1>Hello, World!</h1>'
#     return '<p>Hello, <strong>World</strong>!</p>'

@app.route('/')
def home():
    return """
<h1> Sveiki, cia mano naujas puslapis<h/1<
<p> Super MEGA puslapis!</p>
<p> Super MEGA puslapis!</p>
<p> Super MEGA puslapis!</p>
<h2> Viso gero ammigos!</h2>
    """

if __name__ == '__main__':
    app.run()