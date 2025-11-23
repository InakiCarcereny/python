from flask import Blueprint, request, jsonify
from modelos.entidades.polizaInmueble import PolizaInmueble
from modelos.entidades.polizaInmuebleEscolar import PolizaInmuebleEscolar
from modelos.repositorios.repositorios import obtener_repositorio_polizas

bp_polizas = Blueprint('rutas_polizas', __name__)

repo = obtener_repositorio_polizas()

@bp_polizas.route("/polizas", methods = ['GET'])
def obtener_polizas():
    polizas = repo.obtener_polizas()

    lista_polizas_diccionario = [poliza.to_diccionario() for poliza in polizas]

    return jsonify(lista_polizas_diccionario), 200

@bp_polizas.route("/polizas/<int:numero>", methods = ['GET'])
def obtener_poliza(numero):
    poliza = repo.obtener_poliza(numero)

    if poliza:
        return jsonify(poliza.to_diccionario()), 200
    else:
        return jsonify({ 'mensaje': 'Poliza no encontrada'}), 404
    
@bp_polizas.route("/polizas/ingresos-mensuales", methods = ['GET'])
def valor_mensual_polizas():
    if not repo.obtener_polizas():
        return jsonify({ 'mensaje': 'No hay polizas cargadas'}), 200
    
    ingresos_mensuales = repo.ingresos_mensuales()

    return jsonify({ 'ingresos_mensuales': ingresos_mensuales}), 200

@bp_polizas.route("/polizas", methods = ['POST'])
def agregar_poliza():
    if request.is_json:
        data_poliza = request.get_json()

        try:
            if 'cant_personas' in data_poliza:
                nueva_poliza = PolizaInmuebleEscolar.from_diccionario(data_poliza)
            else:
                nueva_poliza = PolizaInmueble.from_diccionario(data_poliza)

            if repo.agregar_poliza(nueva_poliza):
                return jsonify({ 'mensaje': 'Poliza agregada exitosamente',
                                'nueva_poliza': nueva_poliza.to_diccionario()}), 201
            else:
                return jsonify({ 'mensaje': 'No se pudo agregar la poliza'}), 400
            
        except Exception as e:
            return jsonify({ 'mensaje': str(e)}), 400
        
    else:
        return jsonify({ 'mensaje': 'Los datos debe enviarse en formato JSON'}), 400
    
@bp_polizas.route("/polizas/<int:numero>", methods = ['DELETE'])
def eliminar_poliza(numero):
    poliza = repo.obtener_poliza(numero)

    if not poliza:
        return jsonify({ 'mensaje': 'Poliza no encontrada'}), 404
    
    if repo.elimiar_poliza(numero):
        return jsonify({ 'mensaje': 'Poliza eliminada exitosamente'}), 200
    else:
        return jsonify({ 'mensaje': 'No se puedo eliminar la poliza'}), 400
    
@bp_polizas.route("/polizas/<int:numero>", methods = ['PUT'])
def actualizar_poliza(numero):
    poliza = repo.obtener_poliza(numero)

    if poliza is None:
        return jsonify({'mensaje': 'Poliza no encontrada'}), 404

    if not request.is_json:
        return jsonify({'mensaje': 'Los datos deben ser enviados en formato JSON'}), 400

    datos_actualizados = request.get_json()

    try:
        actualizado = repo.actualizar_poliza(numero, datos_actualizados)

        if not actualizado:
            return jsonify({'mensaje': 'No se pudo actualizar la poliza'}), 400

        poliza_final = repo.obtener_poliza(numero)

        if poliza_final is None:
            return jsonify({'mensaje': 'Error interno: poliza no encontrada luego de actualizar'}), 500

        return jsonify({
            'mensaje': 'Poliza actualizada exitosamente',
            'poliza_actualizada': poliza_final.to_diccionario()
        }), 200

    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
