import json    

with open("credenciales.json") as lista:
    credenciales=json.load(lista)
        


    
        # XMLRPC Wordpress
wpSiteXMLRPC = credenciales['url']
loginId = credenciales['username']
password = credenciales['password']

print(loginId)