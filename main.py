from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Base de datos en memoria
# CRÍTICA: Esto se borra al reiniciar. Para producción necesitas SQLite.
puntos_guardados = []
ultimo_id = 0 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explorar")
def ver_mapa():
    return render_template("guardar_punto.html")

@app.route("/guardar_punto", methods=["POST"])
def guardar_punto():
    global ultimo_id
    
    # LÓGICA DE RUTA: Solo permitimos 2 puntos (A y B)
    if len(puntos_guardados) >= 2:
        return jsonify({"error": "Ruta completa. Elimina un punto para crear otro."}), 409

    datos = request.get_json()
    if not datos or 'lat' not in datos or 'lng' not in datos:
        return jsonify({"error": "Faltan datos"}), 400

    ultimo_id += 1
    
    # Determinamos si es Origen o Destino basado en cuántos hay
    tipo_punto = "ORIGEN (A)" if len(puntos_guardados) == 0 else "DESTINO (B)"
    
    nuevo_punto = {
        "id": ultimo_id,
        "latitud": datos['lat'],
        "longitud": datos['lng'],
        "tipo": tipo_punto
    }
    puntos_guardados.append(nuevo_punto)
    
    # Devolvemos el estado actual para que el frontend sepa si dibujar la línea
    return jsonify({
        "mensaje": "Éxito", 
        "id": ultimo_id, 
        "tipo": tipo_punto,
        "total_puntos": len(puntos_guardados)
    }), 201

@app.route("/eliminar_punto/<int:id_punto>", methods=["DELETE"])
def eliminar_punto(id_punto):
    global puntos_guardados
    puntos_guardados = [p for p in puntos_guardados if p['id'] != id_punto]
    print(f"🗑️ Eliminado punto ID: {id_punto}")
    return jsonify({"mensaje": "Eliminado correctamente", "restantes": len(puntos_guardados)}), 200

# RUTA NUEVA: Para recuperar los puntos al recargar la página (Persistencia visual)
@app.route("/obtener_ruta", methods=["GET"])
def obtener_ruta():
    return jsonify(puntos_guardados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)