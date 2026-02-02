from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base de datos en memoria
puntos_guardados = []
ultimo_id = 0  # CRÍTICO: Contador global para evitar IDs duplicados al borrar

# RUTA 1: Landing Page
@app.route("/")
def home():
    return render_template("index.html")

# RUTA 2: Dashboard / Mapa
@app.route("/explorar")
def ver_mapa():
    return render_template("guardar_punto.html")

# RUTA 3: Guardar Punto (POST)
@app.route("/guardar_punto", methods=["POST"])
def guardar_punto():
    global ultimo_id
    datos = request.get_json()

    if not datos or 'lat' not in datos or 'lng' not in datos:
        return jsonify({"error": "Faltan datos"}), 400

    # Lógica segura de IDs
    ultimo_id += 1
    
    nuevo_punto = {
        "id": ultimo_id,
        "latitud": datos['lat'],
        "longitud": datos['lng']
    }
    puntos_guardados.append(nuevo_punto)
    
    print(f"✅ Guardado ID {ultimo_id}: {datos['lat']}, {datos['lng']}")
    
    # Devolvemos el ID al frontend para que el botón de borrar funcione inmediatamente
    return jsonify({"mensaje": "Éxito", "id": ultimo_id}), 201

# RUTA 4: Eliminar Punto (DELETE)
@app.route("/eliminar_punto/<int:id_punto>", methods=["DELETE"])
def eliminar_punto(id_punto):
    global puntos_guardados
    # Filtramos la lista para quitar el elemento con ese ID
    puntos_guardados = [p for p in puntos_guardados if p['id'] != id_punto]
    
    print(f"🗑️ Eliminado punto ID: {id_punto}")
    return jsonify({"mensaje": "Eliminado correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)