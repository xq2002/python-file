'''
import requests
#with open("E://pic//9b.jpg", "wb") as f:
r = requests.get("http://img12.360buyimg.com/n7/jfs/t1/118064/27/12885/59959/5f17b7efE453f688d/5b33ac76b2aaea9b.jpg")
url = "http://img12.360buyimg.com/n7/jfs/t1/118064/27/12885/59959/5f17b7efE453f688d/5b33ac76b2aaea9b.jpg"
a = url.split('/')[-1]

name = "三星 Galaxy S21 5G（SM-G9910）双模5G 骁龙888 超高清专业摄像 120Hz护目屏 游戏"
aa = name.split(' ')[0]

print(aa)

'''

'''
import requests
from bs4 import BeautifulSoup
url = "https://www.weatheronline.co.uk/weather/maps?LANG=en&CONT=ukuk&LAND=UK&WMO=03772&LEVEL=51&R=0&NOREGION=1"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
date = soup.select('tbody td[class="dt_n"][style="background-image: url(/gfx/tsub.gif);"]')
tmax = soup.select('tr[style="vertical-align:bottom;"]')[0].select('td')
tmin = soup.select('tr[style="vertical-align:middle;"]')[0].select('td')

for a in tmin[1:]:
    print(a.text)
'''



import os
with open('data.txt', 'wb') as f:
    f.write('整体'.encode('utf-8'))
    f.close()
with open('data.txt', 'ab') as f:
    f.write('das'.encode('utf-8'))
    f.close()
'''
who = {}
who['sssd'] = 'fasd'
who['ssa'] = 'adf'
for i in who:
    print(i)
    print(who[i])
print(who)
'''

