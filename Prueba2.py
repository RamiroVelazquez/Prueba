import requests
from tabulate import tabulate

resp1=requests.get("http://testing.iclounder.com/edsonfer/prueba.json")
resp2=resp1.json()



def requestConsumo():
    cont1=0
    cont21=0
    cont3=0
    tload1=0
    tload2=0
    tload3=0
    tdownload1=0
    tdownload2=0
    tdownload3=0
    for cont2 in resp2:
        claves=list(cont2.values())
        if claves[0]=='192.168.1.10' :
            cont1=cont1+1
            tdownload1=tdownload1+claves[1]
            tload1=tload1+claves[2]
            
            
        if claves[0]=='192.168.1.20' :
            cont21=cont21+1
            tdownload2=tdownload2+claves[1]
            tload2=tload2+claves[2]
            
        if claves[0]=='192.168.1.30' :
            cont3=cont3+1
            tdownload3=tdownload3+claves[1]
            tload3=tload3+claves[2]
    listd1=["192.168.1.10"]
    listd2=["192.168.1.20"]
    listd3=["192.168.1.30"]
    listFinal=[]
    listd1.append(cont1)
    listd1.append(tload1)
    listd1.append(tdownload1)
    listd2.append(cont21)
    listd2.append(tload2)
    listd2.append(tdownload2)
    listd3.append(cont3)
    listd3.append(tload3)
    listd3.append(tdownload3)
    listFinal.append(listd1)
    listFinal.append(listd2)
    listFinal.append(listd3)
    print(tabulate(listFinal, headers=["Device", "Connections", "Total Load","Total download"]))
    return

requestConsumo()
