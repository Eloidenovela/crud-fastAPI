from fastapi import FastAPI, HTTPException
import mysql.connector
from connection import db, myCursor

app = FastAPI()

# C
@app.post("/create-dept")
async def __add_dept__(__name_dept: str, __name_faculty: str):
    if not __name_dept or not __name_faculty:
        raise HTTPException(status_code=400, detail="_INVALID_INPUT_")

    try:
        sql = "CALL SET_DEPT(%s, %s);"
        value = (__name_dept, __name_faculty)
        myCursor.execute(sql, value)
        db.commit()
        return {"OUTPUT": "SUCESS"}

    except mysql.connector.Error as err:

        return {"ERROR: ", "{}".format(err)}

# R
@app.get("/read-dept")
async def __get_dept__():
    myCursor.execute("SELECT * FROM DEPARTAMENTO")

    result = myCursor.fetchall()
    db.commit()
    data = []

    for row in result:
        row_data = {
            "Id-Dept": row[0],
            "Name-Dept": row[1],
            "Name-Faculty": row[2],
        }

        data.append(row_data)

    return {"Depts": data}

# U
@app.put("/update-dept")
async def __update_dept__(__name_dept: str, __name_faculty: str, id: int):
    try:
        sql = "CALL UPDATE_DEPT(%s, %s, %s);"
        value = (__name_dept, __name_faculty, id)
        myCursor.execute(sql, value)
        db.commit()
        return {"OUTPUT": "__UPDATED_SUCESSFULL__"}
    except mysql.connector.Error as err:

        return {"ERROR: ", "{}".format(err)}

# D
@app.delete("/del-dept")
async def __delete_dept__(id: int):
    try:
        sql = "CALL DEL_DEPT({});".format(id)
        myCursor.execute(sql)
        db.commit()
        return {"OUTPUT": "__REMOVED_SUCESSFULL__"}
    
    except mysql.connector.Error as err:

        return{"Erro: ", "{}".format(err)}
