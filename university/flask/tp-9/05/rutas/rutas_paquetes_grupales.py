from flask import Blueprint, request, jsonify
from modelos.entidades.paqueteGrupal import PaqueteGrupal
from modelos.repositorios.repositorios import obtener_repositorio_paquetes_grupales

bp_paquetes_grupales = Blueprint('rutas_paquetes_grupales', __name__)

repo = obtener_repositorio_paquetes_grupales()

@bp_paquetes_grupales.route('/paquetes-grupales', methods = ['GET'])
def obtener_paquetes_grupales():
    paquetes_grupales = repo.obtener_paquetes_grupales()

    lista_paquetes_grupales_diccionario = [paquete_grupal.to_diccionario() for paquete_grupal in paquetes_grupales]

    return jsonify(lista_paquetes_grupales_diccionario), 200

@bp_paquetes_grupales.route('/paquetes-grupales/<int:id>', methods = ['GET'])
def obtener_paquete(id):
    paquete = repo.obtener_paquete_grupal_id(id)

    if paquete:
        return jsonify(paquete.to_diccionario()), 200
    else:
        return jsonify({
            'mensaje': 'Paquete grupal no encontrado'
        }), 404
    
@bp_paquetes_grupales.route('/paquetes-grupales', methods = ['POST'])
def agregar_paquete_grupal():
    if not request.is_json:
        return jsonify({
            'mensaje': 'Los datos deben ser enviados en formato JSON'
        }), 400
    
    datos_paquete_grupal = request.get_json()

    try:
        nuevo_paquete = PaqueteGrupal.from_diccionario(datos_paquete_grupal)

        if repo.agregar_paquete_grupal(nuevo_paquete):
            return jsonify({
                'mensaje': 'Paquete grupal agregado exitosamente',
                'nuevo_paquete': nuevo_paquete.to_diccionario()
            }), 201
        else:
            return jsonify({
                'mensaje': 'Error al agregar Paquete grupal'
            }), 400
        
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400
    
@bp_paquetes_grupales.route('/paquetes-grupales/<int:id>', methods = ['DELETE'])
def eliminar_paquete_grupal(id):
    paquete_grupal = repo.obtener_paquete_grupal_id(id)

    if not paquete_grupal:
        return jsonify({
            'mensaje': 'Paquete grupal no encontrado'
        }), 404
    
    try:
        if repo.eliminar_paquete_grupal(id):
            return jsonify({
                'mensaje': 'Paquete grupal eliminado exitosamente'
            }), 200
        
        return jsonify({
            'mensaje': 'Error al eliminar paquete grupal'
        }), 400
    
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400
    
@bp_paquetes_grupales.route('/paquetes-grupales/<int:id>', methods = ['PUT'])
def actualizar_paquete_grupal(id):
    if not request.is_json:
        return jsonify({
            'mensaje': 'Los datos deben ser enviados en formato JSON'
        }), 400
    
    nuevos_datos_paquete_grupal = request.get_json()

    try:
        paquete_grupal = repo.obtener_paquete_grupal_id(id)

        if not paquete_grupal:
            return jsonify({
                'mensaje': 'Paquete grupal no encontrado'
            }), 404
        
        if repo.actualizar_paquete_grupal(id, nuevos_datos_paquete_grupal):
            paquete_grupal_final = repo.obtener_paquete_grupal_id(id)

            if paquete_grupal_final is not None:
                return jsonify({
                    'mensaje': 'Paquete grupal actualizado exitosamente',
                    'paquete_grupal_actualizado': paquete_grupal_final.to_diccionario()
                }), 200
            
        return jsonify({
            'mensaje': 'No se pudo actualizar el paquete grupal'
        }), 400
    
    except Exception as e:
        return jsonify({
            'mensaje': str(e)
        }), 400