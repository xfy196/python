import pickle
data = {"filename": "f1.txt", "create_time": "today", "size": 111}
res = pickle.dumps(data)
print(res)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    read_data = pickle.load(f)
    print(read_data) 