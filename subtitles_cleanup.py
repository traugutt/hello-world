import re

x = open('C:\\Users\sofso\Desktop\Stranger.S01.1080p.Netflix.WEB-DL.DD+2.0.x264-QOQ\korS01E01.txt',
         encoding='UTF-8').readlines()
y = open('C:\\Users\sofso\PycharmProjects\konlp\\bbbbbb\sophie\\templates\sophie\clean eng.txt',
         encoding='UTF-8').readlines()

kor_subs = []
eng_subs = []
for a in x:
    kor_subs.append(a)
# for b in y:
#     eng_subs.append(b)

print(len(kor_subs))
# print(len(eng_subs))

for i in kor_subs:
    a = re.match('\[', i[0])
    b = re.match('\(', i[0])
    c = re.match('[0-9]', i[0])
    e = re.match('^\\n$',i)
    if a or b or c or e:
             kor_subs.remove(i)
             print(i)

print(len(kor_subs))
all_lines = ''.join(kor_subs)
with open('test.txt', mode='w', encoding='UTF-8')as my_file:
      my_file.write(all_lines)
# help(re.match)