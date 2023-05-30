import json

def creacion_de_categorias():

    no_Categorias=""
    while True:
        numero=input("Escribe el número de categorias: ")
        try:
            no_Categorias= int(numero)
            
            if no_Categorias >0:
                print("Intruce el nombre de tu categoria, una por una")
                break

            else:
                
                print("Escribe un Número entero mayor a 0")

        except:
            print("NO ESCRIBAS DECIMALES, NI LETRAS")
        
    categorias=[]

    for i in range(no_Categorias):
        categoria=input("Escribe tu Categoria No."+ str(i+1)+" trata que la caterogia no contenga más de 2 palabras: ")
        categorias.append(categoria)


    print("Guardando categorias...")

        ### Guardado de categorias
    with open('categorias.json', 'w') as file:
        json.dump(categorias, file)

