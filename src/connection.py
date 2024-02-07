from fastapi import FastAPI
import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user= "root",
    passwd = "",
    database = "sigma"
)

myCursor = db.cursor()

