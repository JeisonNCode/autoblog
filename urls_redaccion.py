#import os
import openai
import time
import blogdewp
import FotosPexels
import json
import re
from unidecode import unidecode




def redacciones():
        
    with open("api_key.json", 'r') as key:
         api= json.load(key)

    openai.api_key = api
    
    def solicitud(prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
            
        gpt=(completion.choices[0].message.content)
        
        return gpt


    lisxlis=[]
    
    with open("categorias.json", 'r') as lista:
        lisxlis= json.load(lista)           



    for categoria in lisxlis:
        
        name_archivo="Cat."+categoria+".json"
        
        with open(name_archivo, 'r', encoding='latin-1') as archivo:
            tema = json.load(archivo)

            articulo=""
            titulo=""
            foto=""
            cat= categoria
                       
            # se toma el tema del .JSON y se pasa a tema se envia la solicitud de cada tema a gpt y se sacan titulos, articulo y una palabra para buscar la foto #########
        
            print("\nRedactando articulo de. "+cat+"\n")
            
            #TITULO
            
            text="Un titulo para este tema, solo redacta el titulo: "+tema        
            titulo_sin_procesar=solicitud(text)
            if '"' in titulo_sin_procesar:
                titulo=titulo_sin_procesar.replace('"','')
            else:
                titulo=titulo_sin_procesar
            print(titulo)       
            time.sleep(30)
            
            #ARTICULO
                        
            text="Redacta un articulo de 1000 PALABRAS para un blog de " +cat+ " del siguiente tema, no pongas titulo, solo redacta el articulo: "+tema
            articulo= solicitud(text)
            print(articulo)        
            time.sleep(30)
            
            #FOTO
            
            text="escribe solo 2 palabras cortas que describa lo que a continuacion se dice, solo redacta las 2 palabras: "+tema
            foto= solicitud(text).replace('.','')
            foto=foto.replace('"','').replace(",", " ").replace(".", " ").replace(":", " ").replace(';',' ').replace('\n',' ')
          
            foto = unidecode(re.sub(r"[^\w\s]", "", foto))
            print(foto)
            time.sleep(30)
                            
            uImg=FotosPexels.buscarImagen(foto)
            print(uImg)
                    
            respuesta = blogdewp.publicar(titulo,articulo,cat,tema,uImg)
            
            print(respuesta)
            
            time.sleep(60)
               
            
    return "Ya está todo Redactado"



    
    
    
    
    


