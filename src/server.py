from fastapi import FastAPI, HTTPException
import mysql.connector
from connection import db, myCursor

app = FastAPI()

# C
@app.post("/create-dept")
async def add_dept(nome_departamento: str, nome_faculdade: str):
    if not nome_departamento or not nome_faculdade:
        raise HTTPException(status_code=400, detail="Input invalido")

    try:
        sql = "CALL SET_DEPT(%s, %s);"
        value = (nome_departamento, nome_faculdade)
        myCursor.execute(sql, value)
        db.commit()
        return {"Mensagem": "Sucesso"}

    except mysql.connector.Error as err:

        return {"Erro: ", "{}".format(err)}

# R
@app.get("/read-dept")
async def get_dept():
    myCursor.execute("SELECT * FROM DEPARTAMENTO")

    result = myCursor.fetchall()
    db.commit()
    data = []

    for row in result:
        row_data = {
            "Id-Departamento": row[0],
            "Nome-Departamento": row[1],
            "Nome-Faculdade": row[2],
        }

        data.append(row_data)

    return {"Departamentos": data}

# U
@app.put("/update-dept")
async def update_dept(nome_departamento:str, nome_faculdade: str, id: int):
    try:
        sql = "CALL UPDATE_DEPT(%s, %s, %s);"
        value = (nome_departamento, nome_faculdade, id)
        myCursor.execute(sql, value)
        db.commit()
        return {"Sucesso": "Atualizacao feita com sucesso"}
    except mysql.connector.Error as err:

        return {"Erro: ", "{}".format(err)}

# D
@app.delete("/del-dept")
async def delete_dept(id: int):
    try:
        sql = "CALL DEL_DEPT({});".format(id)
        myCursor.execute(sql)
        db.commit()
        return {"Sucesso": "item removido!"}
    
    except mysql.connector.Error as err:

        return{"Erro: ", "{}".format(err)}