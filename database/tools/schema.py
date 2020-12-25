import json
import os

with open("database/tools/schema.json", "r") as file:
    data = json.load(file)

def users():
    return data["users"]

def tackboards():
    return data["tackboards"]

def questions():
    return data["questions"]

def answers():
    return data["answers"]