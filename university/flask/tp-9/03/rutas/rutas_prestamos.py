from flask import Blueprint, request, jsonify
from modelos.entidades.prestamo import Prestamo
from modelos.repositorios.repositorios import obtener_repositorio_prestamos

bp_prestamos = Blueprint('rutas_prestamos', __name__)

repo = obtener_repositorio_prestamos()

@bp_prestamos.get('/prestamos')
def obtener_prestamos():
    prestamos = repo.obtener_prestamos()
    return jsonify([p.to_diccionario() for p in prestamos]), 200

@bp_prestamos.get('/prestamos/<int:id>')
def obtener_prestamo_id(id):
    prestamo = repo.obtener_prestamo_id(id)
    if prestamo:
        return jsonify(prestamo.to_diccionario()), 200
    return jsonify({'error': 'Prestamo no encontrado'}), 404

@bp_prestamos.get('/prestamos/buscar')
def obtener_prestamo():
    socio_dni = request.args.get('socio_dni', type=int)
    libro_isbn = request.args.get('libro_isbn', type=int)
    fecha_retiro = request.args.get('fecha_retiro', type=int)

    if socio_dni is None or libro_isbn is None or fecha_retiro is None:
        return jsonify({'error': 'Faltan parámetros'}), 400

    prestamo = repo.obtener_prestamo(socio_dni, libro_isbn, fecha_retiro)
    if prestamo:
        return jsonify(prestamo.to_diccionario()), 200
    return jsonify({'error': 'Prestamo no encontrado'}), 404

@bp_prestamos.post('/prestamos')
def agregar_prestamo():
    data = request.get_json()

    try:
        prestamo = Prestamo.from_diccionario(data)
        if repo.agregar_prestamo(prestamo):
            return jsonify({'mensaje': 'Prestamo agregado correctamente'}), 201
        else:
            return jsonify({'error': 'El prestamo ya existe o no hay ejemplares disponibles'}), 400
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp_prestamos.put('/prestamos/<int:id>')
def actualizar_prestamo(id):
    data = request.get_json()

    try:
        if repo.actualizar_prestamo(id, data):
            return jsonify({'mensaje': 'Prestamo actualizado correctamente'}), 200
        return jsonify({'error': 'Prestamo no encontrado'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp_prestamos.put('/prestamos/<int:id>/devolver')
def devolver_libro(id):
    data = request.get_json()
    fecha_devolucion = data.get('fecha_devolucion')

    try:
        if repo.devolver_libro(id, fecha_devolucion):
            return jsonify({'mensaje': 'Libro devuelto correctamente'}), 200
        return jsonify({'error': 'Prestamo no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp_prestamos.delete('/prestamos/<int:id>')
def eliminar_prestamo(id):
    if repo.eliminar_prestamo(id):
        return jsonify({'mensaje': 'Prestamo eliminado correctamente'}), 200
    return jsonify({'error': 'Prestamo no encontrado'}), 404
