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

        return {"Erro: ", "{}".format(err)}

@app.get("/read-dept")
async def get_dept():
    myCursor.execute("SELECT * FROM get_dept")

    result = myCursor.fetchall()
    data = []

    for row in result:
        row_data = {
            "Nome-Departamento": row[0],
            "Nome-Faculdade": row[1],
        }

        data.append(row_data)

    return {"data": data}

@app.put("/update-dept")
async def update_dept():
    