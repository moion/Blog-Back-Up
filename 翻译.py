import requests
import random
import hashlib
import urllib
from PIL import Image
import pytesseract
from urllib.parse import quote


language = {
    '自动检测': 'auto',
    '中文': 'zh',
    '英语': 'en',
    '粤语': 'yue',
    '文言文': 'wyw',
    '日语': 'jp',
    '韩语': 'kor',
    '法语': 'fra',
    '西班牙语': 'spa',
    '泰语': 'th',
    '阿拉伯语': 'ara',
    '俄语': 'ru',
    '葡萄牙语': 'pt',
    '德语': 'de',
    '意大利语': 'it',
    '希腊语': 'el',
    '荷兰语': 'nl',
    '波兰语': 'pl',
    '保加利亚语': 'bul',
    '爱沙尼亚语': 'est',
    '丹麦语': 'dan',
    '芬兰语': 'fin',
    '捷克语': 'cs',
    '罗马尼亚语': 'rom',
    '斯洛文尼亚语': 'slo',
    '瑞典语': 'swe ',
    '匈牙利语': 'hu',
    '繁体中文': 'cht',
    '越南语': 'vie'
}

appid = '20190426000291981'             # API
secretKey = 'sJldvBzBI78Pg3aK6_l4'      # 密钥


def get_text(path):
    text = pytesseract.image_to_string(Image.open(path))
    return text


def get_an(x):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like G'
                            'ecko) Chrome/73.0.3664.3 Safari/537.36'}
    t = requests.get(x, headers=header, timeout=2)

    return t


if __name__ == '__main__':
    i = 'yes'
    while(i == 'yes'):
        wh = input("翻译为->语言")
        wh = language[wh]
        an = input("翻译文字or图片(w or i)：")
        if an == 'i':
            pa = input("请输入图片文件路径：")
            q = get_text(path=pa).replace('\n', ' ')
        else:
            q = input("请输入内容：")

        httpClient = None
        url = '/api/trans/vip/translate'
        fromLang = 'auto'
        toLang = wh
        salt = random.randint(32768, 65536)

        sign = appid + q + str(salt) + secretKey
        m1 = hashlib.md5()
        m1.update(sign.encode("utf8"))
        sign = m1.hexdigest()
        myurl = 'http://api.fanyi.baidu.com' + url + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

        c = get_an(myurl).json()
        #print(c)
        print("--->>>  ")
        print("  "+c['trans_result'][0]['dst'])
        print("  ---<<<")
        i = input("是否继续翻译(yes/no):")
