from lxml import html
import requests
isu_rank = requests.get('http://www.isuresults.com/ws/ws/wsmen.htm')
fig_sktr_tree = html.fromstring(isu_rank.text)
isu_top_points = fig_sktr_tree.xpath('//tr[5]/td[2]//text()') #not going to loop through it
all_skaters = {}
for i in range(5,181):
    isu_rank = fig_sktr_tree.xpath('//tr['+str(i)+']/td[1]//text()')
    isu_points = fig_sktr_tree.xpath('//tr['+str(i)+']/td[2]//text()')
    isu_skater = fig_sktr_tree.xpath('//tr['+str(i)+']/td[3]//text()')
    skater_info = {'name':isu_skater[0], 'standing':isu_rank[0], 'rank':isu_rank[0], 'points':isu_points[0],
                  'points to beat':int(isu_top_points[0])-int(isu_points[0])}

    all_skaters[isu_skater[0]] = skater_info
print(all_skaters)
