import requests
import time
from lxml import html
import re
url = 'https://www.50languages.com/phrasebook/lesson/ko/pt/'
korean_phrases = open('korean.txt', mode='a+', encoding='UTF-8')
portuguese_phrases = open('portuguese.txt', mode='a+', encoding='UTF-8')
urls = []
scraped_pages = []
sentences_xpath = []
for item in range(1, 19):
    xpath = '//*[@id="hn_' + str(item) + '"]/text()'
    sentences_xpath.append(xpath)

for i in range(1, 101):
    urls.append(url + str(i))
for b in urls:
    page = requests.get(b)
    tree = html.fromstring(page.text)
    for path in sentences_xpath:
        all_phrases = tree.xpath(path)
        scraped_pages.append(all_phrases)
print(len(page_list))
for page in scraped_pages:
    both_langs.write("".join(page))
    both_langs.write("\n")

    # time.sleep(1)
    # f.write(all)
    # f.write(all_phrases)

# for b in all_phrases:
#         print(b)
#         f.write(b[0])
#         all = [all.append(v) for v in all_phrases]
# # f.write('\n' + split_lines[0])
#              both_langs.write('\n' + x)
