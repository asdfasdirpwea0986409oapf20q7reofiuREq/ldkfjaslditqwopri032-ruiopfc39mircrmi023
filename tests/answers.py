import requests
import datetime
import json

online = "https://ldkfjaslditqwopri032-ruiopfc39mircrmi023.asdfasdirpwea09.repl.co/answers"
local = "http://127.0.0.1:5000/answers"

post = {"data" : [0, 0, 0, 10, 0, str(datetime.datetime.now()), "Yeah!"]}
put = {"id" : 0, "column" : "upvotes", "new" : 11}
delete = {"id" : 0}

response = requests.post(local, json = json.dumps(post)).text

print(response)