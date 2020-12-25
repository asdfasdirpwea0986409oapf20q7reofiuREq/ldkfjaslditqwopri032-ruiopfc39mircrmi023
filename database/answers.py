import sqlite3
import tools.schema as schema
import tools.utils as utils
import os

schemaJSON = schema.tackboards()
columns = tuple(schemaJSON.keys())

def connect():
    path = "database/database.db"
    decoded = utils.decodeSchema(schemaJSON, columns)
    connection = sqlite3.connect(path, check_same_thread = False)
    try:
        connection.execute(f"CREATE TABLE tackboards ({decoded});")
    except sqlite3.OperationalError:
        pass
    return connection

def create(connection, values):
    while True:
        try:
            connection.execute(f"INSERT INTO tackboards {columns} VALUES {values};")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values[0] +=1
            continue

def retrieve(connection):
    cursor = connection.execute("SELECT * FROM tackboards;")
    output = []
    for row in cursor:
        entry = {}
        entry["id"] = row[0]
        entry["questionID"] = row[1]
        entry["authorID"] = row[2]
        entry["upvotes"] = row[3]
        entry["downvotes"] = row[4]
        entry["created"] = row[5]
        entry["answer"] = row[6]
        output.append(entry)
    return output

def update(connection, id, column, new):
    connection.execute(f"UPDATE tackboards SET {column} = '{new}' WHERE id = {id}")
    connection.commit()

def delete(connection, id):
    connection.execute(f"DELETE FROM tackboards WHERE id = {id}")
    connection.commit()