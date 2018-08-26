import json
from pprint import pprint

with open('message.json') as f:
    data = json.load(f)

F = open("out","w")
for message in data["messages"]:
    if message["sender_name"]  == "Eric Alfonso":
        if "content" in message:
            # print message["content"]
            F.write(message["content"]+"\n")
F.close()
