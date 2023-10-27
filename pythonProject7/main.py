from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class NumeroInput(BaseModel):
    numeros: List[int]

@app.get("/")
def root():
    return {
        "Servicio": "Estructuras de datos"
    }

@app.post("/floyd")
def encontrar_duplicado(input_data: NumeroInput):
    numeros = input_data.numeros

    tortuga = numeros[0]
    liebre = numeros[0]
    while True:
        tortuga = numeros[tortuga]
        liebre = numeros[numeros[liebre]]
        if tortuga == liebre:
            break

    # Fase de búsqueda
    puntero1 = numeros[0]
    puntero2 = tortuga
    while puntero1 != puntero2:
        puntero1 = numeros[puntero1]
        puntero2 = numeros[puntero2]

    # Encontrar el número que se repite y sus índices
    numero_repetido = puntero1
    indices_repetidos = []
    for i, num in enumerate(numeros):
        if num == numero_repetido:
            indices_repetidos.append(i)

    resultado = {
        "numero_repetido": numero_repetido,
        "indices_repetidos": indices_repetidos
    }

    return {"result": resultado}