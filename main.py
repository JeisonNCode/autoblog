import os
import Inicio_de_sesion, openKey, categorias, app


############ AL FINAL VA ALL AQUI
def inicio():

    def verificar_archivo_json(nombre_archivo):
        ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)  # Obtiene la ruta completa del archivo en la carpeta actual del proyecto

        if os.path.exists(ruta_archivo) and os.path.isfile(ruta_archivo):
            return True
        else:
            return False

    # Credenciales
    nombre_archivo_json = "credenciales.json"
    if verificar_archivo_json(nombre_archivo_json):
        print("Credenciales validadas")
    else:
        print("Valida tus credenciales para continuar")
        Inicio_de_sesion.conectarWP()

    # Api Open AI
    nombre_archivo_json = "api_key.json"
    if verificar_archivo_json(nombre_archivo_json):
        print("Api Key de Open AI validada")
    else:
        print("Valida tu clave api de Open AI")
        openKey.validarOpenAI()
            
    # Categorias
    nombre_archivo_json = "categorias.json"
    if verificar_archivo_json(nombre_archivo_json):
        print("Categorias validadas")
        print("Iniciando...")
        estado=app.seleccion()
        print("_______________________________________________________________________\n____________________________________________________"+estado+"_______________________________________________________________________\n____________________________________________________")
        
    else:
        print("Escribe cuantas y cuales categorias tiene tu blog")
        categorias.creacion_de_categorias()
        print("Iniciando...")
        inicio()


inicio()
