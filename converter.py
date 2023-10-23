import json

file = input(".vrpython file > ")
out = input("output .py file > ")
outContent = ""

with open(file, "r") as vrpyf:
    vrpy = vrpyf.read()
    code = json.loads(vrpy)
    outContent = code["textContent"]
    vrpyf.close()

with open(out, "x") as outpy:
    outpy.write(outContent)
    outpy.close()
