from wordpress_xmlrpc import Client
from wordpress_xmlrpc.exceptions import ServerConnectionError
import xmlrpc.client
import json


#### Inicio de sesion en Wordpress

def conectarWP ():

    def login(url,username,password,estado):
        try:
            client = xmlrpc.client.ServerProxy(url)
            blogs = client.wp.getUsersBlogs(username, password)
            if blogs:
                estado=True
                print("Inicio de sesión exitoso")
            else:
                print("Las credenciales son válidas, pero el usuario no tiene acceso a ningún blog\n")
                url = input("Escribe la url de tu blog (https://www.ejemplo.com): ")
                if not not url:
                    if url[-1] =="/":
                        url=url+"xmlrpc.php"
                    else:
                        url=url+"/xmlrpc.php"           
                username = input("Escribe tu usuario de wordpress: ")
                password = input("Escribe la contraseña: ")
                login((url,username,password,estado))
                
        except ServerConnectionError:
            print("No se pudo establecer conexión con el servidor. Verifica tu conexión a Internet.")

        except Exception as e:
            print("Error desconocido:", str(e))
        finally:
            if not estado:
                print("No se pudo establecer conexión, revisa las credenciales")
                url = input("Escribe la url de tu blog (https://www.ejemplo.com): ")
                if not not url:
                    if url[-1] =="/":
                        url=url+"xmlrpc.php"
                    else:
                        url=url+"/xmlrpc.php"
                username = input("Escribe tu usuario de wordpress: ")
                password = input("Escribe la contraseña: ")
                login(url,username,password,estado)
            else:
                print("Guardando credenciales...")
                credenciales = {
                    'url': url,
                    'username': username,
                    'password': password
                }
                return credenciales

    estado=False
    url = input("Escribe la url de tu blog (https://www.ejemplo.com): ")
    if not not url:
        if url[-1] =="/":
            url=url+"xmlrpc.php"
        else:
            url=url+"/xmlrpc.php"

    print(url)
    username = input("Escribe tu usuario de wordpress: ")
    password = input("Escribe la contraseña: ")

    print("Validando...")

    credenciales=login(url,username,password,estado)

    ### Guardado de credenciales
    with open('credenciales.json', 'w') as file:
        json.dump(credenciales, file)

