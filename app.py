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




# 1 punto 

@app.route("/api/cantidadAprendices")
def cantidad_aprendices():

    cantidad = aprendices.count_documents({})

    return jsonify({
        "CantidadAprendices": cantidad
    })
    
    
    
# 2 punto   
   
@app.route("/api/cantidadAprendices/<nivel>")
def cantidad_aprendices_nivel(nivel):

    nivel = nivel.upper()

    cantidad = aprendices.count_documents({
        "NIVEL_DE_FORMACION": nivel
    })

    return jsonify({
        "CantidadAprendices": cantidad,
        "Nivel de formación": nivel
    })   
   
   
   
   
   
# 3 punto
   
@app.route("/api/programas/<nivel>")
def programas_nivel(nivel):

    nivel = nivel.upper()

    programas = aprendices.distinct(
        "PROGRAMA",
        {"NIVEL_DE_FORMACION": nivel}
    )

    programas.sort()

    return jsonify({
        "Nivel de formación": nivel,
        "Programas": programas
    })
   
   
   
   
  
# 4 punto
    
@app.route("/api/certificados/<path:programa>")
def aprendices_certificados(programa):

    filtro = {
        "PROGRAMA": programa,
        "ESTADO_APRENDIZ": "Certificado"
    }

    proyeccion = {
        "_id": 0,
        "FICHA": 1,
        "NOMBRE": 1,
        "PRIMER_APELLIDO": 1,
        "SEGUNDO_APELLIDO": 1
    }

    lista = list(aprendices.find(filtro, proyeccion))

    return jsonify({
        "Aprendices_Certificados": lista,
        "Programa": programa
    })   
   
   
   
   
   
    
if __name__ == "__main__":
    app.run(port=8000, debug=True)