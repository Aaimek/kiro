import json
f = open('instances/tiny.json')
data = json.load(f)
print(data.keys())
