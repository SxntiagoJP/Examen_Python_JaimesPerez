import json

from modulo import *

def abrirJSON(ruta):
    dicFinal={}
    with open(f'./{ruta}.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(ruta,dic):
    with open(f"./ruta.json",'w') as outFile:
        json.dump(dic,outFile)  
clientes={}

datos=[]
    
lie= True
while (lie == True):


    print("PLATAFORMA MOVISTAR")
    print('''
            What do you do?
        -------------------
        1. Ver usuarios (Quejas), (sugerencias), (fidelidad)
        2. Eliminar usuario/s
        3. Agregar usuarios/s''')
    
    opc=input(":")

    if (opc =="1"):

        leer_clientes()
        lie = False

    elif (opc =="2"):

        eliminar_clientes()
        lie = False


    elif (opc =="3"):

        agergar_clientes()
        lie = False
        break
