from uuid import uuid4
from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def connect_to_database():
    mydb = mysql.connector.connect(
    host="mariadb",
    user="reikinoapp",
    password="reikinoapp"
    # database="reikinoapp"
    )
    return mydb

@app.post("/api/v1/user/create_user")
async def create_user(first_name: str, last_name: str, email: str, password: str, is_active: bool):
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    query = "INSERT INTO reikinoapp.user (first_name, last_name, email, password, is_active) VALUES (%s, %s, %s, %s, %s)"
    values = (first_name, last_name, email, password, is_active)
    mycursor.execute(query, values)
    mydb.commit()
    return {'message': 'dale gremio'}