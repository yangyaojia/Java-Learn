import requests
import random
import time
from contextlib import closing
import os
import moviepy.editor as mv




class Download(object):

    def __init__(self,name,url,path,unit,headers = None):
        self.info = "【%s】 %s %.2f%%  %.2f %s / %.2f %s"
        self.name = name
        self.url = url
        self.path = path
        self.unit = unit
        self.status = "正在召唤 (*′∇`*) "
        self.count = 0
        self.total = 0
        self.per = 0
        self.unit_size = 1024*1024 if (unit == "mb" or unit == "MB") else  1024
        self.headers = headers
    
    def __get_info(self):
        _info = self.info % (self.name, self.status, self.count/self.total*100,
                             self.count/self.unit_size,
                             self.unit, self.total/self.unit_size, self.unit)
        return _info
        
    def __refresh(self,count = 0, flag = 1):
        self.count += count
        
        end_str = "\r" if self.count < self.total else "\n"

        if self.count >= self.total : 
            self.status = "召唤成功！ ヾ(*´▽‘*)ﾉ" 
            end_str = "\n"
        else :
            end_str = "\r"
            
        if self.count < self.total or flag:
            print(self.__get_info(),end = end_str)
        
    def download(self):
        with closing(requests.get(self.url, headers = self.headers, stream = True)) as r:
            self.total = int(r.headers["Content-Length"])
            t0 = time.time()

            with open(self.path, "wb") as f:
                for data in r.iter_content(chunk_size = 512):
                    f.write(data)
                    count = len(data)
                    if time.time() - t0 > 0.5 or self.count + count >= self.total:
                        self.__refresh(count = count,flag = 1)
                        t0 = time.time()
                    else :
                        self.__refresh(count = count,flag = 0)



class Bangumi_Episode(object):

    def __init__(self, aid, dip, eps = 1, path = None, combine = True) :
        self.aid = str(aid)
        self.dip = dip
        self.path = path
        self.combine = combine
        self.eps = eps
    
    
    def URL_Interface(self):
        return "https://api.bilibili.com/x/web-interface/view?bvid=" + str(self.aid)
    def URL_Playurl(self):
        return "https://api.bilibili.com/x/player/playurl?bvid=" + str(self.aid) + "&cid=" + str(self.cid) + "&qn=" + str(self.dip)
    def get_Info(self):
        headers = {
            'Host': 'api.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': '''SESSDATA=63af9575%2C1611797911%2C79e96*81''',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        url = self.URL_Interface()
        self.info = requests.get(url, headers = headers).json()
        self.title = self.info['data']['title']
        self.desc = self.info['data']['desc']
    
    def get_downloadurl(self):
        headers = {
            'Host': 'api.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': '''SESSDATA=63af9575%2C1611797911%2C79e96*81''',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        self.cid = self.info['data']['pages'][self.eps-1]['cid']
        url = self.URL_Playurl()
        self.url_info = requests.get(url, headers = headers).json()
        self.urls = []
        for i,j in zip(self.url_info['data']['durl'],range(1,len(self.url_info['data']['durl'])+1)):
            self.urls.append([j,i['url']])
    def URL_download(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.bilibili.com/bangumi/play/ep4137",
            "Origin": "https://www.bilibili.com",
            "Connection": "keep-alive",
            "Range" : "bytes=0-",
            "Cookie": """SESSDATA=63af9575%2C1611797911%2C79e96*81"""
        }


        if not os.path.exists(self.path + self.title):
            os.makedirs(self.path + self.title)

        print("\n" + self.title)
        # print(self.info['data']['pages'][self.eps-1],self.eps,self.cid)
        
            
        print("【 共%d个part哟，正在吟诵～～～】"%len(self.urls))
        for i in range(len(self.urls)):
            name = "part" + str(self.urls[i][0]) + ".flv"
            path = self.path + self.title + "/" + name
            k = Download(name, self.urls[i][1], path, "MB", headers = headers)
            k.download()
            self.urls[i].append(path)
        
    def clips_combine(self):
        v = [mv.VideoFileClip(self.urls[i][2]) for i in range(len(self.urls))]
        V =  mv.concatenate_videoclips(v)
        V.write_videofile(self.path + self.title + ".mp4",codec = 'h264',audio = True) #,audio_codec = "libfdk_aac")
        V.close()
        for i in v:
            i.close()
        # libfdk_aac
        for i in self.urls:
            os.remove(i[2])
        os.removedirs(self.path + self.title)

    def Download(self):
            self.get_Info()
            self.get_downloadurl()
            self.URL_download()
            if self.combine :
                self.clips_combine()
    
    
    @staticmethod
    def bilibili():

        A = Bangumi_Episode(None,None)

        QN = {"A":16, "B":32, "C":64, "D":80, "E":112}
        av = ''
        av = input("请告诉我你要下载的视频的BV号吧！: BV")
        while not av.isalnum():
            av = input("你在说什么，我听不懂？请告诉我正确的BV号吧！: BV")
        av = av.strip()
        A.aid = av
        A.get_Info()

        qn = str(input("\n你想下载哪一个版本的呢？\nA : 360P\nB : 480P\n"+
            "C : 720P\nD : 1080P\nE : 1080P+\n请选择你想要的那一个吧！(输入A,B,C,D,E): "))
        qn = QN[qn.upper()]
        A.dip = qn

        path = input("\n想要下载到当前文件夹下吗？【Y/N】: ")
        if path.upper() ==  'N':
            path = input("\n告诉我你要下载到哪吧：")
            path.replace("\\","/")
            if path[-1] != "/":
                path =path + "/"
        else :
            path = "./"
        A.path = path

        combine = input("\n要合并还是分流？(合并要召唤更久 >.<)【Y/N】: ")
        combine = bool(combine.upper()=="Y")
        A.combine = combine
        


        if len(A.info['data']['pages']) == 1:
            
            print("\n嗯哼，你的任务我收到了，那么现在开始下载！")
            A.get_downloadurl()
            A.URL_download()
            if A.combine :
                A.clips_combine()

            print("\n【下载成功！ *★,°*:.☆\(￣▽￣)/$:*.°★* 】")
            print('\n"开始享受吧！"')

        else:
            epss = []
            opt = input("\n这个视频貌似分p呀，要把它们全部下载吗？【1～%d】\nA.我只要其中一个！\nB.我全都要！\nC.我要这几个！\n做出你的选择吧！【A,B,C】: "%len(A.info['data']['pages']))
            title = A.title
            if opt.upper() == 'A':
                eps = int(input("\n你要哪一个？【01～%d】:"%len(A.info['data']['pages'])))
                epss.append(eps)
            elif opt.upper() == "B":
                epss = [i for i in range(1,len(A.info['data']['pages'])+1)]
            elif opt.upper() == "C":
                epss = input("\n你要哪几个呢？(请用英文逗号隔开数字！): ")
                epss = list(eval("[ " + epss + " ]"))
            
            print("\n嗯哼，你的任务我收到了，那么现在开始下载！")

            for eps in epss:

                A.eps = eps
                A.title = title + "  %02d" % eps
                A.get_downloadurl()
                A.URL_download()
                if A.combine :
                    A.clips_combine()

            print("\n【下载成功！ *★,°*:.☆\(￣▽￣)/$:*.°★* 】")
            print('\n"开始享受吧！"')

if __name__ == '__main__':
    print("""
    ----------------------
     B站下载姬 - 正经版      
       Ver 2.71 Alpha    
     本软件仅供交流学习,  
        请勿用于盈利。   
    ----------------------
    """)
    Bangumi_Episode.bilibili()
    input("按任意键结束下载.......")
    

'''
https://api.bilibili.com/pgc/player/web/playurl?avid=15315365&cid=24929781&qn=32

'''