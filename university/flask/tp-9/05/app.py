from flask import Flask
from rutas.rutas_ciudades import bp_ciudades
from rutas.rutas_hoteles import bp_hoteles
from rutas.rutas_paquetes_grupales import bp_paquetes_grupales

app = Flask(__name__)

app.register_blueprint(bp_ciudades)
app.register_blueprint(bp_hoteles)
app.register_blueprint(bp_paquetes_grupales)