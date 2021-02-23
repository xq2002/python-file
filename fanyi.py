'''
import urllib.request
import urllib.parse
import json

def translation():
    while 1:
        print("-"*30)
        n = input("请选择：1 翻译 2 退出 ：")
        if n == '1':

            content = input("请输入要翻译的内容：")

            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

            data = {}

            data['i'] = content

            data['from'] = 'AUTO'

            data['to'] = 'AUTO'

            data['smartresult'] = 'dict'

            data['client']= 'fanyideskweb'

            data['salt']= '15790094838498'

            data['sign']= '9ab763875001c1949ae49d3c230ba19f'

            data['ts']= '1579009483849'

            data['bv']= '5a84f6fbcebd913f0a4e81b6ee54608'

            data['doctype']= 'json'

            data['version'] = '2.1'

            data['keyfrom'] = 'fanyi.web'

            data['action'] = 'FY_BY_CLICKBUTTION'

            data = urllib.parse.urlencode(data).encode('utf-8')

            response = urllib.request.urlopen(url, data)

            html = response.read().decode('utf-8')


            #print(json.loads(html))

            target =json.loads(html)

            for ra in target['translateResult'][0]:
                print(ra['tgt'], end=" ")

            #print("翻译结果:%s" % (target['translateResult'][0][0]['tgt']))

        elif n == '2':
            print("感谢使用！")
            break
        else:
            print("输入有误！")
if __name__=='__main__':
    translation()
'''

"""官方Python接入百度翻译API测试Demo（有所改动，官方DEMO有些过时，Python包有些变化）"""
import httplib2
import urllib
import random
import json
from hashlib import md5


def translate(text):
        appid = '20210216000698997'  # 你的appid
        secretKey = 'Q1Y0y5mRSdf4b0S_zgmv'  # 你的密钥

        httpClient = None
        myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        #q = 'A band of rain will clear eastwards, although slow to clear parts of south-east England, and particularly north-west Scotland where it will remain very windy. Mild with some sunshine to follow, but also heavy showers this afternoon.'  # 要翻译的词
        fromLang = 'en'  # 翻译源语言
        toLang = 'zh'  # 译文语言
        salt = random.randint(32768, 65536)

        # 签名
        sign = appid + text + str(salt) + secretKey
        m1 = md5()
        m1.update(sign.encode(encoding='utf-8'))
        sign = m1.hexdigest()
        # myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
        myurl = myurl + '?q=' + urllib.parse.quote(
            text) + '&from=' + fromLang + '&to=' + toLang + '&appid=' + appid + '&salt=' + str(salt) + '&sign=' + sign
        try:
            h = httplib2.Http('.cache')
            response, content = h.request(myurl)
            if response.status == 200:
                response = json.loads(content.decode('utf-8'))  # loads将json数据加载为dict格式
                return response["trans_result"][0]['dst']
        except httplib2.ServerNotFoundError:
            return "error"
            # print("Site is Down!")


