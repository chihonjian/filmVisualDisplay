import requests
import re


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}


#获取top10票房数据
def get_top10_boxOffice():
    url_top10 = "http://www.boxofficecn.com/the-red-box-office"
    html_top10 = requests.get(url_top10,headers=headers)

    re_top10 = r'<td class="column-2">(.*?（\d.\d）).*?</td><td class="column-3">(.*?)</td><td class="column-4">(.*?)</td>'
    data_re = re.findall(re_top10,html_top10.text)

    return data_re

#获取2021年票房
def get_2021_top10_boxOffice():
    url = "https://www.snhtdc.com.cn/articles/17176.html"

    html = requests.get(url,headers=headers)
    html.encoding = 'utf-8'

    r = '《(.*?)》(.*?)亿元'
    datas = list(re.findall(r,html.text))[1:]

    for item in range(len(datas)):
        datas[item] = list(datas[item])
        if(len(datas[item][0])>20):

            s = r".*?>(.*?)<.*?"
            temp = re.findall(s,datas[item][0])

            datas[item][0] = temp[0]

    return datas


#获取历年每部电影
def movie_datas_year():
    data = []
    for item in range(2016,2021):
        url = "http://www.boxofficecn.com/boxoffice" + str(item)
        r = r'<tr align="left">\n<td>.*?</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n</tr>'
        html = requests.get(url,headers=headers)
        re_datas = re.findall(r,html.text)
        data += re_datas

    return data


if __name__ == '__main__':
    movie_datas_year()

