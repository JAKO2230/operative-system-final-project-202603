import os, psycopg
from flask import Flask, jsonify, request
app = Flask(__name__)
DB = os.environ["DATABASE_URL"]
ORIG = os.getenv("ORIGEN_PERMITIDO", "*")

def q(sql, p=None):
    with psycopg.connect(DB, connect_timeout=5) as c:
        with c.cursor() as cur:
            cur.execute(sql, p or ())
            if cur.description: return cur.fetchall()
            c.commit(); return []

@app.after_request
def cors(r):
    r.headers["Access-Control-Allow-Origin"] = ORIG or "*"
    r.headers["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
    r.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return r

@app.route("/api/sistemas", methods=["GET", "POST", "OPTIONS"])
def sistemas():
    if request.method == "OPTIONS": return ("", 204)
    if request.method == "POST":
        d = request.get_json(silent=True) or {}
        n, t, a = str(d.get("nombre","")).strip(), str(d.get("tipo","")).strip(), int(d.get("anio",0))
        desc, kern, fs = str(d.get("descripcion","")).strip(), str(d.get("kernel","")).strip(), str(d.get("sistema_archivos","")).strip()
        if not n or not t or not a: return jsonify(error="Faltan datos"), 400
        q("INSERT INTO sistemas_operativos (nombre, anio, tipo, descripcion, kernel, sistema_archivos) VALUES (%s,%s,%s,%s,%s,%s)", (n, a, t, desc, kern, fs))
        return jsonify({"nombre": n, "anio": a, "tipo": t, "descripcion": desc, "kernel": kern, "sistema_archivos": fs}), 201
    filas = q("SELECT id, nombre, anio, tipo, COALESCE(descripcion,''), COALESCE(kernel,''), COALESCE(sistema_archivos,'') FROM sistemas_operativos ORDER BY anio")
    return jsonify([{"id": i, "nombre": n, "anio": a, "tipo": t, "descripcion": d, "kernel": k, "sistema_archivos": f} for i, n, a, t, d, k, f in filas])

@app.route("/api/sistemas/<int:sid>", methods=["DELETE", "OPTIONS"])
def borrar(sid):
    if request.method == "OPTIONS": return ("", 204)
    q("DELETE FROM sistemas_operativos WHERE id = %s", (sid,))
    return jsonify(eliminado=sid), 200

@app.get("/api/salud")
def salud():
    q("SELECT 1"); return jsonify(estado="ok")
