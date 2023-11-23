from fastapi import FastAPI
import mysql.connector
from connection import myCursor
from connection import db

app = FastAPI()
@app.post("/create-dept")
async def add_dept(nome_departamento: str, nome_faculdade: str):
    sql = 'select ver_dept(%s);'
    value = (nome_departamento)
    myCursor.execute(sql, value)
    db.commit()
    result = myCursor.fetchone()

    if (result == 1):
        return {"Mensagem: ", "Departamento ja existente"}
    
    sql = "call set_dept(%s, %s);"
    value = (nome_departamento, nome_faculdade)
    myCursor.execute(sql, value)
    db.commit()
    return {"Mensagem:", "Sucesso"}
    
    


