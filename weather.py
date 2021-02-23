# This Python file uses the following encoding: utf-8
import requests
from bs4 import BeautifulSoup
import httplib2
import urllib
import random
import json
from hashlib import md5
import threading
import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本
from email.mime.multipart import MIMEMultipart

# 邮件构建
def sendemail (content):
    subject = "英国城市天气预报信息"  # 邮件标题
    sender = "xq020121@163.com"  # 发送方
    recver = "663609101@qq.com"  # 接收方
    password = "BXZZXIKXYCPNSKVL"
    msg = MIMEMultipart()
    msg['Subject'] = subject#邮件标题
    msg['To'] = recver  #收件人
    msg['From'] = sender#发件人
    att1 = MIMEText(content, 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="Englang_weather.txt"'
    msg.attach(att1)
    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)#实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recver], msg.as_string())#as_string对msg的消息进行了封装
    smtp.close()


#翻译，参数为字符串，翻译为中文
def translate(text):
    appid = '20210216000698997'  # 你的appid
    secretKey = 'Q1Y0y5mRSdf4b0S_zgmv'  # 你的密钥
    httpClient = None
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = 'en'  # 翻译源语言
    toLang = 'zh'  # 译文语言
    salt = random.randint(32768, 65536)
    # 签名
    sign = appid + text + str(salt) + secretKey
    m1 = md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?q=' + urllib.parse.quote(text) + '&from=' + fromLang \
            + '&to=' + toLang + '&appid=' + appid + '&salt=' + str(salt) + '&sign=' + sign
    try:
        h = httplib2.Http('.cache')
        response, content = h.request(myurl)
        if response.status == 200:
            response = json.loads(content.decode('utf-8'))  # loads将json数据加载为dict格式
            return response["trans_result"][0]['dst']
    except httplib2.ServerNotFoundError:
        return "error"


#获取每个城市的天气预报，为英文的
def gettext(url):
    try:
        r = requests.get(url)
        r.status_code
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        sec = soup.select('section[id="forecast-text"]')[0]
        return sec.text
    except:
        return ""


#每80个一行处理数据
def chanrow (txt):
    a = 0
    ss = ""
    for i in txt:
        a += 1
        ss += i
        if a % 112 == 0:
            ss += '\n'
    return ss

#处理每个城市，获得处理过中文数据（80一行）
def aalk(href):
    content = gettext(href)
    content = content.replace('\n', '')
    content = translate(content)
    content = chanrow(content)
    return content

#封装thread类，获取函数的返回值
class mythread(threading.Thread):
    def __init__(self, func, args=()):
        super(mythread, self).__init__()
        self.func = func
        self.args = args
    def run(self):
        self.result = self.func(self.args)
    def get_result(self):
        try:
            return self.result
        except :
            return None

#获取城市对应的天气预报信息
def get_city_wea(city):
    try:
        return who[city]
    except:
        return "NONE"

#获取英国整体天气情况
burl = "https://www.metoffice.gov.uk/"
rw = requests.get(burl)
bsoup = BeautifulSoup(rw.text, 'html.parser')
content = bsoup.select('div[class="accordion"]')[0].text
content = content.replace('\n', '')
content = translate(content)
content = chanrow(content)

#将所有城市及对应的天气预报组成字典
who = {}

#获取所有城市
citty = []

#爬取城市天气情况线程
t = []
with open('data.txt', 'wb') as f:
    f.write('英国整体天气情况'.encode('utf-8'))
    f.write('\n'.encode('utf-8'))
    f.write(content.encode('utf-8'))
    f.close()
uul = "https://www.metoffice.gov.uk/weather/forecast/uk"
rq = requests.get(uul)
csoup = BeautifulSoup(rq.text, 'html.parser')

#将所有城市爬取过程添加线程
link1 = csoup.select('ul[aria-label="Regions in England"] li')
for link in link1:
    city = link.a.text
    citty.append(city)
    href = 'https://www.metoffice.gov.uk/' + link.a.attrs['href']
    th = mythread(aalk, args=(href))
    th.start()
    t.append(th)
link2 = csoup.select('ul[aria-label="Regions in Scotland"] li')
for link in link2:
    city = link.a.text
    citty.append(city)
    href = 'https://www.metoffice.gov.uk/' + link.a.attrs['href']
    th = mythread(aalk, args=(href))
    th.start()
    t.append(th)
link3 = csoup.select('ul[aria-label="Regions in Northern Ireland"] li')
for link in link3:
    city = link.a.text
    citty.append(city)
    href = 'https://www.metoffice.gov.uk/' + link.a.attrs['href']
    th = mythread(aalk, args=(href))
    th.start()
    t.append(th)
link4 = csoup.select('ul[aria-label="Regions in Wales"] li')
for link in link4:
    city = link.a.text
    citty.append(city)
    href = 'https://www.metoffice.gov.uk/' + link.a.attrs['href']
    th = mythread(aalk, args=(href))
    th.start()
    t.append(th)
for i in t:
    i.join()

#将城市及对应的天气更新字典
for a, b in zip(citty, t):
    who[a] = b.get_result()

#将城市天气写入文件
with open('data.txt', 'ab') as f:
    for i in who:
        f.write('\n'.encode('utf-8'))
        f.write(translate(i).encode('utf-8'))
        f.write('\n'.encode('utf-8'))
        f.write(who[i].encode('utf-8'))
print("你想了解的英国城市名称（英文）")
print("该城市的天气预报信息为：")
city = input()
print(get_city_wea(city))
content = open('data.txt', 'rb').read()
sendemail(content)
