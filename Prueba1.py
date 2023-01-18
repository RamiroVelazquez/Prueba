import requests


resp=requests.get("https://jsonplaceholder.typicode.com/users")
resp2=resp.json()

def requestUser(id_s):
    idsi=int(id_s)
    if 11>idsi>0:
        idsi=idsi-1
        print(resp2[idsi].get("id"))
        print(resp2[idsi].get("name"))
        print(resp2[idsi].get("username"))
        print(resp2[idsi].get("email"))
        print(resp2[idsi].get("address").get("geo").get("lat"))
        print(resp2[idsi].get("address").get("geo").get("lng"))
    else:
        print("ID no encontrado")
    return

while (True):
    id=input("Teclee el ID: ")
    int(id)
    requestUser(id)
    print("------------------")
