from flask import Flask

app = Flask(__name__)

@app.route('/about')
def about():
    return 'Esta página es acerca de nosotros'

@app.route('/contact')
def contact():
    return 'Esta es la página de contacto'

if __name__ == '__main__':
    app.run(debug=True)