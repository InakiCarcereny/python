from flask import Blueprint, request, jsonify
from modelos.entidades.ciudad import Ciudad
from modelos.repositorios.repositorios import obtener_repositorio_ciudades

bp_ciudades = Blueprint('rutas_ciudades', __name__)

repo = obtener_repositorio_ciudades()

@bp_ciudades.route('/ciudades', methods = ['GET'])
def obtener_ciudades():
    ciudades = repo.obtener_ciudades()

    lista_ciudades_diccionario = [ciudad.to_diccionario() for ciudad in ciudades]

    return jsonify(lista_ciudades_diccionario), 200

@bp_ciudades.route('/ciudades/<int:id>', methods = ['GET'])
def obtener_ciudad_id(id):
    ciudad = repo.obtener_ciudad_id(id)

    if ciudad:
        return jsonify(ciudad.to_diccionario()), 200
    else:
        return jsonify({ 
            'mensaje': 'Ciudad no encontrada'
        }), 404
    
@bp_ciudades.route('/ciudades/<string:nombre>', methods = ['GET'])
def obtener_ciudad_nombre(nombre):
    ciudad = repo.obtener_ciudad_nombre(nombre)

    if ciudad:
        return jsonify(ciudad.to_diccionario()), 200
    else:
        return jsonify({
            'mensaje': 'Ciudad no encontrada'
        }), 404
    
@bp_ciudades.route('/ciudades', methods = ['POST'])
def agregar_ciudad():
    if not request.is_json:
        return jsonify({
            'mensaje': 'Los datos deben ser enviados en forma JSON'
        }), 400
    
    datos_ciudad = request.get_json()

    try:
        nueva_ciudad = Ciudad.from_diccionario(datos_ciudad)

        if repo.agregar_ciudad(nueva_ciudad):
            return jsonify({
                'mensaje': 'Ciudad agregada exitosamente',
                'nueva_ciudad': nueva_ciudad.to_diccionario()
            }), 201
        else:
            return jsonify({
                'mensaje': 'No se pudo agregar la nueva ciudad'
            }), 400
        
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400

@bp_ciudades.route('/ciudades/<int:id>', methods = ['DELETE'])
def eliminar_ciudad(id):
    try:
        ciudad = repo.obtener_ciudad_id(id)

        if not ciudad:
            return jsonify({
                'mensaje': 'Ciudad no encontrada'
            }), 404
        
        if repo.eliminar_ciudad(id):
            return jsonify({
                'mensaje': 'Ciudad eliminada exitosamente'
            }), 200
        else:
            return jsonify({
                'mensaje': 'No se pudo eliminar la ciudad'
            }), 400
        
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400

@bp_ciudades.route('/ciudades/<int:id>', methods = ['PUT'])
def actualizar_ciudad(id):
    if not request.is_json:
        return jsonify({
            'mensaje': 'Los datos deben ser enviados en formato JSON'
        }), 400
    
    datos_actualizados = request.get_json()

    try:
        ciudad = repo.obtener_ciudad_id(id)

        if not ciudad:
            return jsonify({
                'mensaje': 'Ciudad no encontrada'
            }), 404

        if repo.actualizar_ciudad(id, datos_actualizados):
            ciudad_actualiazada = repo.obtener_ciudad_id(id)

            if ciudad_actualiazada is not None:
                return jsonify({
                    'mensaje': 'Ciudad actualizada exitosamente',
                    'ciudad_actualizada': ciudad_actualiazada.to_diccionario()
                }), 200
        
        return jsonify({
                    'mensaje': 'No se pudo actualizar la ciudad'
                }), 400
        
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400
            
