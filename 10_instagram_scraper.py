#Part of a Course from Hezion Studios on Big Data: Trinity

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json

#Para entender este programa primero salta a la función main
class Insta_Image_Links_Scraper:

    def getLinks(self, hashtag, url):
        #Leemos el html de la url y la interpretamos con BeautifulSoup, para convertirla en un objeto que podamos manipular
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        #Buscamos la variable window._sharedData y la convertimos en un objeto
        script = soup.find('script', text=lambda t: \
                           t.startswith('window._sharedData'))
        page_json = script.text.split(' = ', 1)[1].rstrip(';')
        data = json.loads(page_json)
        
        #Ya que tenemos el objeto data, que es la variable de la que hablamos antes, accedemos a los posts
        #Los posts están ubicados en "edges" ¿Cómo lo sabemos? Hay que leer la variable para buscarlos.
        #Por cada post imprimimos el texto y el link de la imagen
        for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
            print("------------------------")
            print("------------------------")
            try:
                print(post['node']['edge_media_to_caption']['edges'][0]['node']['text'])
            except:
                pass
            image_src = post['node']['thumbnail_resources'][1]['src']
            print(image_src)

    #Esto es lo primero que ejecutará el programa
    def main(self):
        #Creamos la variable ctx que nos servirá de configuración para conectarnos a Instagram
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        #Definimos los hashtags que usaremos y colocamos la página de hashtags de Instagram
        #Por cada uno de ellos saltamos a la función getLinks
        hashtags = ["ingenieria","venezuela"]
        for hashtag in hashtags:
            self.getLinks(hashtag,'https://www.instagram.com/explore/tags/'+ hashtag + '/')

if __name__ == '__main__':
    obj = Insta_Image_Links_Scraper()
    obj.main()
