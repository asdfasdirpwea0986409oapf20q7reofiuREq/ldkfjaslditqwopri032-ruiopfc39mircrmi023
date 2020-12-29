import requests
import datetime
import json

online = "https://ldkfjaslditqwopri032-ruiopfc39mircrmi023.asdfasdirpwea09.repl.co/questions"
local = "http://127.0.0.1:5000/questions"

post = {"data" : [0, 0, 10, 0, "[0]", str(datetime.datetime.now()), "Is this cool!"]}
put = {"id" : 0, "column" : "upvotes", "new" : 11}
delete = {"id" : 0}

response = requests.delete(local, json = json.dumps(delete)).text

print(response)