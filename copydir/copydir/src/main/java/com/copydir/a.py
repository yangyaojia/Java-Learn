import requests
import os


def URL( a ):
    return "https://api.bilibili.com/x/relation/stat?vmid=" + a.__str__()


def URL2( a ):
    return "https://api.bilibili.com/x/web-interface/card?mid=" + a.__str__()

headers = {
    'Host': 'api.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
}
# id = 1824890
# url = URL2(id)
# info = requests.get(url, headers = headers).json()
# follower = info["data"]["follower"]
# print(id, follower)

# https://api.bilibili.com/x/relation/stat?vmid=1824890000&jsonp=jsonp
# https://api.bilibili.com/x/web-interface/card?mid=3
ans = []
for i in range(1, 700000000):
    id = i
    url = URL2(id)
    info = requests.get(url, headers = headers).json()
    follower = info["data"]["follower"]
    print(id, follower)
    if(follower >= 1910000):
        ans.append((id, follower))
    