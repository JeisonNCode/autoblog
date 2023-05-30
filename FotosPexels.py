import requests
import os


base_url = "https://api.pexels.com/v1"
api_key = "sUw9V5DPmT6pzQTDbqmoNdCumwlTxnoj7RqYpNHqz51TjKbk29x7qiYX"
name_file=""


#####

def buscarImagen(palabra_clave):
    headers = {"Authorization": api_key}
    params = {"query": palabra_clave, "per_page": 1}
    url = f"{base_url}/search"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        resultados = response.json()
        if resultados["total_results"] > 0:
            image_id = resultados["photos"][0]["id"]
            file_path = ""+palabra_clave+".jpg"  

            #return imagen_id
            headers = {"Authorization": api_key}
            url = f"{base_url}/photos/{image_id}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                imagen_url = response.json()["src"]["original"]
                response = requests.get(imagen_url)
                if response.status_code == 200:
                    with open(file_path, "wb") as archivo:
                        archivo.write(response.content)
                    print("La imagen se ha descargado exitosamente.")
                    print(file_path)
                    name_file = file_path
                else:
                    print("Error al descargar la imagen.")
                    name_file = "man-791049.jpg"
            else:
                print("No se pudo obtener información de la imagen.")
                name_file = "man-791049.jpg"

            return name_file            
                                               
            

        else:
            print("No se encontraron imágenes para la palabra clave especificada.")
            name_file = "man-791049.jpg"
    else:
        print("Error al realizar la búsqueda de imágenes.")
        name_file = "man-791049.jpg"
        
    return name_file
