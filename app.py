import requests
from bs4 import BeautifulSoup
import openai
import urls_redaccion
import time
import json


def seleccion():

    lista_categorias=[]


    with open("categorias.json", 'r') as lista:
        lista_categorias= json.load(lista)

    print(lista_categorias)


    lista_ulrs_bing=[]
    lista_contenido=[]


    for cat in lista_categorias:
        lista_ulrs_bing.append('https://www.bing.com/news/search?q='+cat)


    # Realizar la solicitud HTTP a la página web
    # Obtener el contenido HTML de la página
    # Crear un objeto BeautifulSoup para analizar el HTML
    # Extraer el texto de la página

    cont1=0
    for b in lista_ulrs_bing:
        
        response = requests.get(b)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        textLargo = soup.get_text()
        print(len(textLargo))
        if len(textLargo) >1236:
            text=textLargo[236:1236]
        else:
            text=textLargo
        
        print(text)
        lista_contenido.append(text)
        cont1=cont1+1
        if cont1 == len(lista_ulrs_bing):
            print("finalizo la busqueda en bing")
    print("30%****************************----------------------------------------------------------------------------------------")    


    # Definir el tema que deseas buscar OPEN AI

    with open("api_key.json", 'r') as key:
        api= json.load(key)

    openai.api_key = api

    indice =0

    for categoria in lista_categorias:
        
        print(categoria)
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "con referencia a los siguientes Titulares elige y crea solo 1 tema divertido para un blog de " + categoria+", que sean menos de 8 palabras por titulo y 60 palabras de descripción del tema, Titulares: "+ lista_contenido[indice]}
            ]
        )
        print(completion.choices[0].message.content)
        respuestaSinEdicion=(completion.choices[0].message.content)
        
        if '"' in respuestaSinEdicion:
            respuesta = respuestaSinEdicion.replace('"','')
        else:
            respuesta=respuestaSinEdicion
        
        nombreArchivo="Cat."+categoria+".json"
        
        with open (nombreArchivo, 'w') as file:
            json.dump(respuesta, file)
            
        indice=indice+1
        
        time.sleep(40)
        
            ###########################################################################################

    print("Temas de cada categoria han sido seleccionado---------------------------------------------------------------------")

    print("Se crearon los temas - se espera 1 min para empezar la redaccion")
    


    time.sleep(60)
    
    estado=urls_redaccion.redacciones()
    
    return estado



