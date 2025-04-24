from flask import Flask

app = Flask(__name__)

# Ruta principal - bienvenida
@app.route('/')
def inicio():
   
    # Mensaje de bienvenida
    return """
        👋 ¡Bienvenido al Restaurante Flask!<br>
        Pedí tu plato en la URL escribiendo:<br>
        <a href="/orden/pizza">/orden/pizza</a> <br>
        <a href="/orden/hamburguesa">/orden/hamburguesa</a> <br>
        <a href="/orden/empanadas">/orden/empanadas</a>
    """

# Ruta para recibir el pedido
@app.route('/orden/<plato>')
def ordenar(plato):
    menu = {
        'pizza': '🍕 Aquí está tu deliciosa pizza',
        'hamburguesa': '🍔 Tu hamburguesa está lista',
        'empanadas': '🥟 Unas empanadas recién salidas del horno'
    }

    if plato in menu:
        return menu[plato]
    else:
        return f'❌ Lo siento, no tenemos {plato} en el menú.'

# Iniciar la app
if __name__ == '__main__':
    app.run(debug=True)
