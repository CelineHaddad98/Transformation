import json
from transformers.employee_transformer import transform

with open('data/input.json') as file:
    lines = file.readlines()


with open("data/output.json", "w") as outfile:
    for line in lines:
        edited = transform(json.loads(line))
        outfile.write(json.dumps(edited))
