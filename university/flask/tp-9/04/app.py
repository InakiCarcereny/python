from flask import Flask
from rutas.rutas_polizas import bp_polizas

app = Flask(__name__)

app.register_blueprint(bp_polizas)