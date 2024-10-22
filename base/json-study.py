import json
data = {"filename": "f1.txt", "create_time": "today", "size": 111}
j = json.dumps(data)
print(j)
print(type(j))