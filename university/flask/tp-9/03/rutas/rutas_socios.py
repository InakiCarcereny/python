from flask import Blueprint, jsonify, request
from modelos.entidades.socio import Socio
from modelos.entidades.prestamo import Prestamo
from modelos.repositorios.repositorios import obtener_repositorio_socios

bp_socios = Blueprint('rutas_socios', __name__)

repo = obtener_repositorio_socios()

@bp_socios.route('/socios', methods = ['GET'])
def obtener_socios():
    socios = repo.obtener_socios()

    lista_socios_diccionario = [socio.to_diccionario() for socio in socios]
    
    return jsonify(lista_socios_diccionario), 200

@bp_socios.route('/socios/<int:DNI>', methods = ['GET'])
def obtener_socio_DNI(DNI):
    socio = repo.obtener_socio(DNI)

    if socio:
        return jsonify(socio.to_diccionario()), 200
    else:
        return jsonify({ 'mensaje': 'No existe un socio con ese DNI'}), 404
    
@bp_socios.route('/socios', methods = ['POST'])
def agregar_socio():
    if request.is_json:
        datos_socio = request.get_json()

        try:
            nuevo_socio = Socio.from_diccionario(datos_socio)

            if repo.agregar_socio(nuevo_socio):
                return jsonify({ 'mensaje': 'Socio agregado exitosamente', 'nuevo_socio': nuevo_socio.to_diccionario()}), 201
            else:
                return jsonify({ 'mensaje': 'No se pudo agregar el nuevo socio'}), 400
            
        except Exception as e:
            return jsonify({ 'mensaje': str(e)}), 400
        
    else:
        return jsonify({ 'mensaje': 'Los datos tiene que enviarse en formato JSON'}), 400
    
@bp_socios.route('/socios/<int:DNI>', methods = ['DELETE'])
def eliminar_socio(DNI, prestamos: list[Prestamo]):
    try:
        socio = repo.obtener_socio(DNI)

        if not socio:
            return jsonify({ 'mensaje': 'No existe un socio con ese DNI'}), 404
        
        if repo.eliminar_socio(DNI, prestamos):
            return jsonify({ 'mensaje': 'Socio eliminado exitosamente'}), 200
        else:
            return jsonify({ 'mensaje': 'No se pudo elimiar el socio'}), 404
        
    except Exception as e:
        return jsonify({ 'mensaje': str(e)}), 400
    
@bp_socios.route('/socios/<int:DNI>', methods = ['PUT'])
def actualizar_socio(DNI):
    if not request.is_json:
        return jsonify({ 'mensaje': 'La solicitud debe ser en formato JSON'})
    
    datos_actualizados = request.get_json()

    try:
        socio_existente = repo.obtener_socio(DNI)

        if not socio_existente:
            return jsonify({ 'mensaje': 'Socio no encontrado'}), 404
        
        if repo.actualizar_socio(DNI, datos_actualizados):
            socio_actualizado = repo.obtener_socio(DNI)

            if socio_actualizado:
                return jsonify({
                'mensaje': 'Socio actualizado exitosamente',
                'socio_actualizado': socio_actualizado.to_diccionario()
            }), 200
        
        return jsonify({ 'mensaje': 'No se puedo actualizar el socio'}), 404
    
    except Exception as e:
        return jsonify({ 'mensaje': str(e)}), 400

    
