from flask import Blueprint, request, jsonify
from modelos.entidades.hotel import Hotel
from modelos.repositorios.repositorios import obtener_repositorio_hoteles

bp_hoteles = Blueprint('rutas_hoteles', __name__)

repo = obtener_repositorio_hoteles()

@bp_hoteles.route('/hoteles', methods = ['GET'])
def obtener_hoteles():
    hoteles = repo.obtener_hoteles()

    lista_hoteles_diccionario = [hotel.to_diccionario() for hotel in hoteles]

    return jsonify(lista_hoteles_diccionario), 200

@bp_hoteles.route('/hoteles/<int:id>', methods = ['GET'])
def obtener_hotel(id):
    hotel = repo.obtener_hotel(id)

    if hotel:
        return jsonify(hotel.to_diccionario()), 200
    else:
        return jsonify({
            'mensaje': 'Hotel no encontrado'
        }), 404
    
@bp_hoteles.route('/hoteles', methods = ['POST'])
def agregar_hotel():
    if not request.is_json:
        return jsonify({
            'mensaje': 'Los datos deben ser enviados en formato JSON'
        }), 400
    
    datos_hotel = request.get_json()

    try:
        nuevo_hotel = Hotel.from_diccionario(datos_hotel)

        if repo.agregar_hotel(nuevo_hotel):
            return jsonify({
                'mensaje': 'Hotel agregado exitosamente',
                'nuevo_hotel': nuevo_hotel.to_diccionario()
            }), 201
        else:
            return jsonify({
                'mensaje': 'No se pudo agregar el hotel'
            }), 400
        
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400
    
@bp_hoteles.route('/hoteles/<int:id>', methods = ['DELETE'])
def eliminar_hotel(id):
    hotel = repo.obtener_hotel(id)

    if not hotel:
        return jsonify({
            'mensaje': 'Hotel no encontrado'
        }), 404

    try:
        if repo.eliminar_hotel(id):
            return jsonify({
                'mensaje': 'Hotel eliminado exitosamente'
            }), 200
        else:
            return jsonify({
                'mensaje': 'No se pudo borrar el hotel'
            }), 400
        
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400
    
@bp_hoteles.route('/hoteles/<int:id>', methods = ['PUT'])
def actualizar_hotel(id):
    if not request.is_json:
        return jsonify({
            'mensaje': 'Los datos deben ser enviados en formato JSON'
        }), 400
    
    datos_actualizados = request.get_json()

    try:
        hotel = repo.obtener_hotel(id)

        if not hotel:
            return jsonify({
                'mensaje': 'Hotel no encontrado' 
            }), 404
        
        if repo.actualizar_hotel(id, datos_actualizados):
            hotel_actualizado = repo.obtener_hotel(id)

            if hotel_actualizado is not None:
                return jsonify({
                    'mensaje': 'Hotel actualizado exitosamente',
                    'hotel_actualizado': hotel_actualizado.to_diccionario()
                }), 200
            
        return jsonify({
            'mensaje': 'No se pudo actualizar el hotel'
        }), 400
    
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400

