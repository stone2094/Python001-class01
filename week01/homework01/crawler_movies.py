import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
#from urlparse import urljoin
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
cookies ='uuid_n_v=v1; uuid=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; _csrf=32877a02a8d04b39e3f222e6b4252e292c0973a18db32cd60d8b7d80615581a7; _lxsdk_cuid=172f3f8be8ac8-08fdf560b8b4c8-4b5469-13c680-172f3f8be8ac8; _lxsdk_s=172f3f8be8b-39e-934-5c6%7C%7C2; _lxsdk=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593231065; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593231065; __mta=210704298.1593231064909.1593231064909.1593231064909.1; mojo-uuid=3533b1aaa282adefb81243b93761bc8c; mojo-trace-id=1; mojo-session-id={"id":"e0a79ad05c1f37e567601a5c0f95e241","time":1593231064986}'
header = {'Cookies':str(cookies),'User-agent':user_agent}

#upcomming movies, showtype=2
burl = 'https://maoyan.com'
enurl = 'https://maoyan.com/films?showType=3'

#请求入口链接地址
response = requests.get(enurl,headers=header)

bs_info = bs(response.text, 'html.parser')
indx = 0
mylist =  []
# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
    for atag in tags.find_all('a',):
        # 获取所有链接
        print(burl+atag.get('href'))
        # 获取电影名字
        print(atag.find('span',attrs={'class': 'name'}).text)
        filmname = atag.find('span',attrs={'class': 'name'}).text
        # 获取某个电影具体的链接
        filmtype=''
        releasetime=''
        # 请求某个电影的具体链接地址
        responsedetail = requests.get(burl+atag.get('href'),headers=header)
        bsdetail_info = bs(responsedetail.text, 'html.parser')

        for indfilm in bsdetail_info.find_all('div', attrs={'class': 'movie-brief-container'}):
            #标示循环次数
            indfilmded = 0
            for indfilmde in indfilm.find_all('li',attrs={'class': 'ellipsis'}):
                #如果是电影类型
                if indfilmded == 0:
                    for indtype in indfilmde.find_all('a',attrs={'class': 'text-link'}):
                        #print(indtype.text)
                        filmtype= filmtype+indtype.text
                    #print('movetype',filmtype)

                #如果是电影放映时间
                if indfilmded == 2:
                    releasetime = indfilmde.text
                    #print('Releasetime',releasetime)

                indfilmded = indfilmded + 1
        #print(movies)
        indx = indx +1
        #添加电影项
        mylist.append({'film':filmname,'type':filmtype,'releasetime':releasetime})

    if indx >= 10:
        break
#save movie message to csv
movie1 = pd.DataFrame(data = mylist)
movie1.to_csv('./movie_homework01.csv', encoding='utf8', index=False, header=False)