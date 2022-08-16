from uuid import uuid4
from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/api/v1/database_status")
async def database_status():
    mydb = mysql.connector.connect(
    host="mariadb",
    user="reikinoapp",
    password="reikinoapp"
    # database="reikinoapp"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    return {'databases': mycursor.fetchall()}