from flask import Flask
from rutas.rutas_libros import bp_libros
from rutas.rutas_socios import bp_socios
from rutas.rutas_prestamos import bp_prestamos

app = Flask(__name__)

app.register_blueprint(bp_libros)
app.register_blueprint(bp_socios)
app.register_blueprint(bp_prestamos)