from flask import Flask
import random

app = Flask(__name__)

# Lista de mensajes
mensajes = [
    "Hoy es un gran día para aprender algo nuevo.",
    "La práctica hace al maestro.",
    "Cada línea de código te acerca a tu objetivo.",
    "Nunca dejes de mejorar.",
    "Recuerda siempre depurar y probar tu código."
]

@app.route('/')
def home():
    # Selecciona un mensaje aleatorio
    mensaje = random.choice(mensajes)
    return mensaje

if __name__ == '__main__':
    app.run(debug=True)
