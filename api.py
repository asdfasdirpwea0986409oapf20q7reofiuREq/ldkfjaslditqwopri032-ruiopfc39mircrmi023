from flask import *
import database
import datetime
import json
import sys
import os

app = Flask("Tackboard API")

def log(severity, content):
    with open("error.log", "a+") as errorLog:
        line = f"\n{str(datetime.datetime.now())} | [{severity.upper()}] {content} | Made by {request.remote_addr}"
        errorLog.write(line)

def error():
    execptionType, _, exceptionTB = sys.exc_info()
    filename = os.path.split(exceptionTB.tb_frame.f_code.co_filename)[1]
    execptionType = str(execptionType).strip("<class '").strip("'>")
    details = f"caught {execptionType} in {filename} at line {exceptionTB.tb_lineno}"
    log("medium/extreme", details)
    return jsonify({"error" : "something went wrong", "details" : details}), 500

@app.errorhandler(404)
def notFound(error):
    log("info", "user went to a url that was not found on this webpage")
    return jsonify({"error" : "that view function was not found", "details" : str(error)}), 404

@app.errorhandler(405)
def requestForbidden(error):
    log("info", "user tried to make an forbidden http request")
    return jsonify({"error" : "that http request is forbidden", "details" : str(error)}), 
    
@app.errorhandler(406)
def insufficientData(error):
    log("info", "user passed insufficent data")
    return jsonify({"error" : "insufficient data", "details" : str(error)}), 406

@app.route("/", methods = ["GET"])
def homepage():
    return jsonify({"message" : "welcome to the Tackboard API!"}), 200

@app.route("/errors", methods = ["GET"])
def getErrors():
    with open("error.log", "r") as errorLog:
        data = errorLog.read()
    return f"<pre>{data}</pre>"

@app.route("/users", methods = ["POST", "GET", "PUT", "DELETE"])
def users():
    connection = database.users.connect()
    method = request.method
    try:
        values = json.loads(request.get_json()) # will only retrieve if request mimetype is JSON
    except TypeError:
        if method != "GET":
            abort(406) # means that request is faulty
        else:
            pass
    try:
        if method == "GET":
            return jsonify(database.users.retrieve(connection)), 200
        elif method == "POST":
            database.users.create(connection, tuple(values["data"]))
            return jsonify({"message" : "success"})
        elif method == "PUT":
            database.users.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"})
        elif method == "DELETE":
            database.users.delete(connection, values["id"])
            return jsonify({"message" : "success"})
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # cannot convert the data user passed into the nessesary type
        abort(406)
    except: # something went wrong in this function
        return error()

@app.route("/tackboards", methods = ["POST", "GET", "PUT", "DELETE"])
def tackboards():
    connection = database.tackboards.connect()
    method = request.method
    try:
        values = json.loads(request.get_json()) # will only retrieve if request mimetype is JSON
    except TypeError:
        if method != "GET":
            abort(406) # means that request is faulty
        else:
            pass
    try:
        if method == "GET":
            return jsonify(database.tackboards.retrieve(connection)), 200
        elif method == "POST":
            database.tackboards.create(connection, tuple(values["data"]))
            return jsonify({"message" : "success"})
        elif method == "PUT":
            database.tackboards.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"})
        elif method == "DELETE":
            database.tackboards.delete(connection, values["id"])
            return jsonify({"message" : "success"})
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # cannot convert the data user passed into the nessesary type
        abort(406)
    except: # something went wrong in this function
        return error()

@app.route("/questions", methods = ["POST", "GET", "PUT", "DELETE"])
def questions():
    connection = database.questions.connect()
    method = request.method
    try:
        values = json.loads(request.get_json()) # will only retrieve if request mimetype is JSON
    except TypeError:
        if method != "GET":
            abort(406) # means that request is faulty
        else:
            pass
    try:
        if method == "GET":
            return jsonify(database.questions.retrieve(connection)), 200
        elif method == "POST":
            database.questions.create(connection, tuple(values["data"]))
            return jsonify({"message" : "success"})
        elif method == "PUT":
            database.questions.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"})
        elif method == "DELETE":
            database.questions.delete(connection, values["id"])
            return jsonify({"message" : "success"})
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # cannot convert the data user passed into the nessesary type
        abort(406)
    except: # something went wrong in this function
        return error()

@app.route("/answers", methods = ["POST", "GET", "PUT", "DELETE"])
def answers():
    connection = database.answers.connect()
    method = request.method
    try:
        values = json.loads(request.get_json()) # will only retrieve if request mimetype is JSON
    except TypeError:
        if method != "GET":
            abort(406) # means that request is faulty
        else:
            pass
    try:
        if method == "GET":
            return jsonify(database.answers.retrieve(connection)), 200
        elif method == "POST":
            database.answers.create(connection, tuple(values["data"]))
            return jsonify({"message" : "success"})
        elif method == "PUT":
            database.answers.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"})
        elif method == "DELETE":
            database.answers.delete(connection, values["id"])
            return jsonify({"message" : "success"})
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # cannot convert the data user passed into the nessesary type
        abort(406)
    except Exception as e: # something went wrong in this function
        print(e)
        return error()

if __name__ == "__main__":
    app.run(debug = True)