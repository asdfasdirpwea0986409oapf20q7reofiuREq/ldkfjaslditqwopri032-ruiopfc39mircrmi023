import json
import os

with open("database/tools/schema.json", "r") as file:
    schema = json.load(file)

def users():
    return schema["users"]

def tackboards():
    return schema["tackboards"]

def questions():
    return schema["questions"]

def answers():
    return schema["answers"]