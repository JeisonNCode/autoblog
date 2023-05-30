
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import json





def publicar(title,body,cat,extracto,fileImg):
    
        #Abre json y guarda en lista local
    
        with open("credenciales.json") as lista:
            credenciales=json.load(lista)
        
    
        # XMLRPC Wordpress
        wpSiteXMLRPC = credenciales['url']
        loginId = credenciales['username']
        password = credenciales['password']

        wp = Client(wpSiteXMLRPC, loginId, password)
        post = WordPressPost()
    

        post.title = title

        
        post.terms_names = {
        # 'post_tag': ['Tag', 'Tag2', 'Tag3'],
        'category': [cat]
        }

        post.post_status = 'publish'
        # post.post_status = 'publish'

        # custom field
        customFields = []
        customFields.append({
        'key': 'comunidad',
        'value': 'DTI'
        })

        post.custom_fields = customFields


        data = {'name': 'picture.jpg','type': 'image/jpg',}

        with open(fileImg, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())
        foto = wp.call(media.UploadFile(data))

        # foto == {
        #       'id': 6,
        #       'file': 'picture.jpg'
        #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
        #       'type': 'image/jpeg',
        # }
        attachment_id = foto['id']
        image_url1 = foto['url']

        post.thumbnail = attachment_id

        image_html1 = '<img src="{}" alt="Imagen 1">'.format(image_url1)

        post.content = image_html1
        post.content += '\n' + body
        post.excerpt = extracto



        new_id = int(wp.call(NewPost(post)))
        if new_id > 0:
            resultado ='Se ha publicado del articulo de ' + cat+ ' en wordpress '
        
        else:
            resultado ='Ha fallado la publicación en de '+cat +' en wordpress'
            
        return resultado
        
        

