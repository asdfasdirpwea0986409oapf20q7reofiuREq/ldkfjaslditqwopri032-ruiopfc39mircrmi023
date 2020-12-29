import requests
import datetime
import json

online = "https://ldkfjaslditqwopri032-ruiopfc39mircrmi023.asdfasdirpwea09.repl.co/tackboards"
local = "http://127.0.0.1:5000/tackboards"

post = {"data" : [0, "Tackboard's Tackboard", "Education", "The first one here!", 0, 0, str(datetime.datetime.now()), "[0]", "[0]", "[0]"]}
put = {"id" : 0, "column" : "public", "new" : 1}
delete = {"id" : 0}

response = requests.post(online, json = json.dumps(post)).text

print(response)
