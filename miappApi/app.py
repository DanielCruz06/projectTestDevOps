from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Datos de ejemplo en memoria
tasks = [
    {'id': 1, 'title': 'Configurar la VNet en Azure', 'done': True},
    {'id': 2, 'title': 'Desplegar la VM del backend con Terraform', 'done': False}
]

# Endpoint para obtener todas las tareas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Endpoint de salud para verificar que la API funciona
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    # Escuchamos en 0.0.0.0 para que sea accesible desde fuera del contenedor/VM
    # El puerto 5000 es una convención común para desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)
