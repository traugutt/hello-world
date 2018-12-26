# import requests
# import time
# from lxml import html
# web_page = requests.get("https://www.lyrics.com/artist/Bon%20Iver/991558")
# tree = html.fromstring(web_page.text)
# songs = tree.xpath('//tbody//td//a//@href')
# for item in songs:
#     r = requests.get("https://www.lyrics.com" + str(item))
# for n in r:
#     n.get('//body//pre')
# for i in n:
#     time.sleep(1)
#     with open(Bon_Iver.txt, mode='w', encoding='utf-8') as bon_iver_file:
#       bon_iver_file.write(i)
#       time.sleep(3)
# web_page = requests.get("https://www.lyrics.com/artist/Beyonc%C3%A9/349078")
# tree = html.fromstring(web_page.text)
# songs_urls = tree.xpath("//tbody//td//a[starts-with(@href, '/lyric')]//@href")
# for item in songs_urls:
#     r = requests.get("https://www.lyrics.com" + str(item))
#     tree2 = html.fromstring(r.text)
#     songs = " ".join(tree2.xpath('//body//pre//text()'))
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
