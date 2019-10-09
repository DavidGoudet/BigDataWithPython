from ImageProcessor import *

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json

class Insta_Image_Links_Scraper:

    def getLinks(self, hashtag, url):       
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        script = soup.find('script', text=lambda t: \
                           t.startswith('window._sharedData'))
        page_json = script.text.split(' = ', 1)[1].rstrip(';')
        data = json.loads(page_json)
    
        for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
            print("------------------------")
            print("------------------------")
            print("------------------------")
            image_src = post['node']['thumbnail_resources'][1]['src']
            imageProcessor = ImageProcessor()
            print("Link de la imagen:")
            print(image_src)
            print("Objetos vistos por el programa:")
            print(imageProcessor.predictImageObjects(image_src))
            print(post['node']['accessibility_caption'])

    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        hashtags = ["indoor","venezuela"]
        for hashtag in hashtags:
            self.getLinks(hashtag,'https://www.instagram.com/explore/tags/'+ hashtag + '/')

if __name__ == '__main__':
    obj = Insta_Image_Links_Scraper()
    obj.main()
