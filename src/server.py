from fastapi import FastAPI, HTTPException
import mysql.connector
from connection import myCursor
from connection import db

app = FastAPI()

@app.post("/create-dept")
async def add_dept(nome_departamento: str, nome_faculdade: str):
    if not nome_departamento or not nome_faculdade:
        raise HTTPException(status_code=400, detail="Input invalido")

    try:
        sql = "call set_dept(%s, %s);"
        value = (nome_departamento, nome_faculdade)
        myCursor.execute(sql, value)
        db.commit()
        return {"Mensagem": "Sucesso"}

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return {"Mensagem": "Departamento ja existente"}
