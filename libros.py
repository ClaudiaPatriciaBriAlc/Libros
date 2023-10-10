from flask import Flask, jsonify, request
from http import HTTPStatus
app = Flask(__name__)
libros = [
    {
        'id': 1,
        'titulo': 'No soy un serial killer',
        'autor': 'Dan Wells',
        'editorial': 'VRYA',
        'paginas': '325'
    },
    {
        'id': 2,
        'titulo': 'Todo oscuro, sin estrellas',
        'autor': 'Stephen King',
        'editorial': 'DEBOLS!LLO',
        'paginas': '439'
    }
]
@app.route('/libros/', methods=['GET'])
def get_libros():
    return jsonify({'data': libros})
@app.route('/libros/<int:libro_id>', methods=['GET'])
def get_libro(libro_id):
    libro = next((libro for libro in libros if libro['id'] == libro_id), None)
    if libro:
        return jsonify(libro)
    return jsonify({'message': 'book not found'}), HTTPStatus.NOT_FOUND
@app.route('/libros', methods=['POST'])
def create_libro():
    data = request.get_json()
    titulo = data.get('titulo')
    autor = data.get('autor')
    editorial = data.get('editorial')
    paginas = data.get('paginas')
    libro = {
        'id': len(libros) + 1,
        'titulo': titulo,
        'autor': autor,
        'editorial': editorial,
        'paginas': paginas
    }
    libros.append(libro)
    return jsonify(libro), HTTPStatus.CREATED
@app.route('/libros/<int:libro_id>', methods=['PUT'])
def update_libro(libro_id):
    libro = next((libro for libro in libros if libro['id'] == libro_id), None)
    if not libro:
        return jsonify({'message': 'book not found'}), HTTPStatus.NOT_FOUND
    data = request.get_json()
    libro.update(
        {
            'titulo': data.get('titulo'),
            'autor': data.get('autor'),
            'editorial': data.get('editorial'),
            'paginas': data.get('paginas')
        }
    )
    return jsonify(libro)
@app.route('/libros/<int:libro_id>', methods=['DELETE'])
def delete_libro(libro_id):
    libro = next((libro for libro in libros if libro['id'] == libro_id), None)
    if not libro:
        return jsonify({'message': 'book not found'}), HTTPStatus.NOT_FOUND
    libros.remove(libro)
    return '', HTTPStatus.NO_CONTENT
if __name__ == '__main__':
    app.run()