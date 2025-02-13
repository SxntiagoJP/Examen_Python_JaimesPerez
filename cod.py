import json

def abrirJSON():
    dicFinal={}
    with open('./clientes.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./clientes.json",'w') as outFile:
        json.dump(dic,outFile)
    
clientes={}
    
lie= True
while (lie == True):
    print("PLATAFORMA MOVISTAR")
    print('''
            What do you do?
        -------------------
        1. Agregar usuario/s
        2. Eliminar usuario/s
        3. Ver usuarios''')
    opc=input(":")
    if (opc =="1"):
        