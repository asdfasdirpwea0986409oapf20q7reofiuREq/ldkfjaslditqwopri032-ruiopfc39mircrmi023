import requests
import datetime
import json

online = "https://ldkfjaslditqwopri032-ruiopfc39mircrmi023.asdfasdirpwea09.repl.co/users"
local = "http://127.0.0.1:5000/users"

post = {"data" : [0, str(datetime.datetime.now().strftime(r"%m/%d/%Y")), "aarushgupta", "Aarush Gupta", "hello@aarushgupta.tk", "[1, 2]", 3, 4]}
put = {"id" : 0, "column" : "username", "new" : "aargup"}
delete = {"id" : 0}

response = requests.post(online, json = json.dumps(post)).text

print(response)