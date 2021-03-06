import sqlite3
import database.tools.schema as schema
import database.tools.utils as utils
import os

schemaJSON = schema.questions()
columns = tuple(schemaJSON.keys())

def connect():
    path = "database/database.db"
    decoded = utils.decodeSchema(schemaJSON, columns)
    connection = sqlite3.connect(path, check_same_thread = False)
    try:
        connection.execute(f"CREATE TABLE questions ({decoded});")
    except sqlite3.OperationalError:
        pass
    return connection

def create(connection, values):
    while True:
        try:
            connection.execute(f"INSERT INTO questions {columns} VALUES {values};")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values = list(values)
            values[0] +=1
            values = tuple(values)
            continue

def retrieve(connection):
    cursor = connection.execute("SELECT * FROM questions;")
    output = []
    for row in cursor:
        entry = {}
        entry["id"] = row[0]
        entry["authorID"] = row[1]
        entry["upvotes"] = row[2]
        entry["downvotes"] = row[3]
        entry["upvotedMemberIDs"] = row[4]
        entry["answeredMemberIDs"] = row[5]
        entry["created"] = row[6]
        entry["question"] = row[7]
        output.append(entry)
    return output

def update(connection, id, column, new):
    connection.execute(f"UPDATE questions SET {column} = '{new}' WHERE id = {id}")
    connection.commit()

def delete(connection, id):
    connection.execute(f"DELETE FROM questions WHERE id = {id}")
    connection.commit()