from flask import Blueprint, request, jsonify
from modelos.entidades.libro import Libro
from modelos.entidades.prestamo import Prestamo
from modelos.repositorios.repositorios import obtener_repositorio_libros

bp_libros = Blueprint('rutas_libros', __name__)

repo = obtener_repositorio_libros()

@bp_libros.route('/libros', methods = ['GET'])
def obtener_libros():
    libros = repo.obtener_libros()

    lista_libros_diccionario = [libro.to_diccionario() for libro in libros]

    return jsonify(lista_libros_diccionario), 200

@bp_libros.route('/libros/<int:ISBN>', methods = ['GET'])
def obtener_libro(ISBN):
    libro = repo.obtener_libro_ISBN(ISBN)

    if libro:
        return jsonify(libro.to_diccionario()), 200
    else:
        return jsonify({ 'mensaje': 'Libro no encontrado'}), 404
    
@bp_libros.route('/libros', methods = ['POST'])
def agregar_libro():
    if request.is_json:
        datos_libros = request.get_json()

        try:
            nuevo_libro = Libro.from_diccionario(datos_libros)

            if repo.agregar_libro(nuevo_libro):
                return jsonify({ 'mensaje': 'Libro agregado exitosamente',
                                'nuevo_libro': nuevo_libro.to_diccionario()}), 201
            else:
                return jsonify({ 'mensaje': 'No se pudo agregar el libro'}), 400
            
        except Exception as e:
            return jsonify({ 'mensaje': str(e)}), 400
    else:
        return jsonify({ 'mensaje': 'La solicitud debe ser en formato JSON'}), 400
    
@bp_libros.route('/libros/<int:ISBN>', methods = ['DELETE'])
def eliminar_libro(ISBN, prestamos: list[Prestamo]):
    try:
        if repo.existe_libro_ISBN(ISBN):
            if repo.eliminar_libro(ISBN, prestamos):
                return jsonify({ 'mensaje': 'Libro borrado exitosamente'}), 200
            else:
                return jsonify({ 'mensaje': 'No se pudo borrar el libro'}), 400
        else:
            return jsonify({ 'mensaje': 'Libro no encontrado'}), 404
        
    except Exception as e:
        return jsonify({ 'mensaje': str(e)}), 400
    
@bp_libros.route('/libros/<int:ISBN>', methods = ['PUT'])
def actualizar_libro(ISBN):
    if not request.is_json:
        return jsonify({"mensaje": "La solicitud debe ser en formato JSON"}), 400

    datos_actualizados = request.get_json()

    try:
        libro_existente = repo.obtener_libro_ISBN(ISBN)
        
        if not libro_existente:
            return jsonify({"mensaje": "Libro no encontrado"}), 404

        if repo.actualizar_libro(ISBN, datos_actualizados):
            libro_final = repo.obtener_libro_ISBN(ISBN)
            
            if libro_final:
                return jsonify({
                "mensaje": "Libro actualizado exitosamente",
                "libro_actualizado": libro_final.to_diccionario()
            }), 200

        return jsonify({"mensaje": "No se pudo actualizar el libro"}), 400

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
    
