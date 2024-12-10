import json
import requests as api

# with open("./clase.json") as archivo:
#     json_base = json.load(archivo)

#     print("\n---- jugando con json")
#     json_base = json.dumps(json_base)
#     json_base = json.loads(json_base)
#     print(json_base["nombre"])

#     if json_base["soltero"]:
#         print("Se va de fiesta")
#     else:
#         print("Se queda en casa")

info = api.get("https://mindicador.cl/api/dolar")
info = info.json()
print(json.dumps(info, indent=4))

