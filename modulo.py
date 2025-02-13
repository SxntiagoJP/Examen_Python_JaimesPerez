import json

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
    
def leer_clientes ():

    print ("lista de clientes")
    for i in range(f'/{clientes}'):
        print (i)

def eliminar_clientes ():

    print ("que cliente desea elimniar")
    clientes.pop (input)


def agergar_clientes ():

    print("cliente que desea agregar ")
    clientes.append ({clientes}[{datos}])
    input("nombre:")
    input("direccion:")
    input("c.c:")
    input("cliente:")