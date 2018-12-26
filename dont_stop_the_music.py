import requests
import time
from lxml import html
import sys
def get_songs(url,url_xpath,url_xpath2,domain):
web_page = requests.get(url)
tree = html.fromstring(web_page.text)
songs_urls = tree.xpath(url_xpath)
for item in songs_urls:
    r = requests.get(domain + str(item))
    tree2 = html.fromstring(r.text)
    songs = " ".join(tree2.xpath(url_xpath2))
    print(songs)
    with open("Beyonce.txt", mode='a+', encoding='utf-8') as beyonce_file:
        beyonce_file.write(songs)

 if __name__ == '__main__':
    get_songs(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
