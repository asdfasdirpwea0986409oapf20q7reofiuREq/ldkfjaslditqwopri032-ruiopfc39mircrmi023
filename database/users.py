import sqlite3
import database.tools.schema as schema
import database.tools.utils as utils
import os

schemaJSON = schema.users()
columns = tuple(schemaJSON.keys())

def connect():
    path = "database/database.db"
    decoded = utils.decodeSchema(schemaJSON, columns)
    connection = sqlite3.connect(path, check_same_thread = False)
    try:
        connection.execute(f"CREATE TABLE users ({decoded});")
    except sqlite3.OperationalError:
        pass
    return connection

def create(connection, values):
    while True:
        try:
            connection.execute(f"INSERT INTO users {columns} VALUES {values};")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values[0] +=1
            continue

def retrieve(connection):
    cursor = connection.execute("SELECT * FROM users;")
    output = []
    for row in cursor:
        entry = {}
        entry["id"] = row[0]
        entry["created"] = row[1]
        entry["username"] = row[2]
        entry["name"] = row[3]
        entry["email"] = row[4]
        entry["asked"] = row[5]
        entry["answered"] = row[6]
        output.append(entry)
    return output

def update(connection, id, column, new):
    connection.execute(f"UPDATE users SET {column} = '{new}' WHERE id = {id}")
    connection.commit()

def delete(connection, id):
    connection.execute(f"DELETE FROM users WHERE id = {id}")
    connection.commit()