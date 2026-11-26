from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

cliente = MongoClient(MONGO_URI)

cliente.admin.command("ping")
print("Conexión exitosa con MongoDB")

base_datos = cliente["CURSOS_CTPI_2026-CRISTIAN"]

aprendices = base_datos["APRENDICES_MONTILLA"]

app = Flask(__name__)


def filtro_por_ficha(ficha):
    return {"FICHA": ficha}




@app.route("/api/cantidadAprendices")
def cantidad_aprendices():

    cantidad = aprendices.count_documents({})

    return jsonify({
        "CantidadAprendices": cantidad
    })
    
    
    
if __name__ == "__main__":
    app.run(port=8000, debug=True)