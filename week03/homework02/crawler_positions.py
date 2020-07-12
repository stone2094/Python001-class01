import time
import requests
from fake_useragent import UserAgent
import lxml.etree
from scrapy.selector import Selector
from concurrent.futures import ThreadPoolExecutor
from mysql import connectMySQL

def requests_city(city):
    indx=100
    page=1
    ua = UserAgent(verify_ssl=False)

    headers = {
    'User-Agent' : ua.random,
    'Referer' : 'https://accounts.douban.com/passport/login_popup?login_source=anony'
    }

    # 登陆后可以进行后续的请求
    url2 = 'https://www.lagou.com/beijing-zhaopin/Python/'
    url = 'https://www.lagou.com/{city}-zhaopin/Python/{page}'
    url_tmp = url.format(url,city=city,page=page)
    headers = {
    'Host': 'www.lagou.com',
    'User-Agent': ua.random,
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.lagou.com/',
    'Connection': 'keep-alive',
    'Cookie': 'user_trace_token=20200706122341-49eb47b2-0744-4ccd-838d-90bf19bcf33a; _ga=GA1.2.1352212827.1594009422; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594009422,1594009706,1594215145; LGUID=20200706122342-c40d9efc-d260-433b-8da5-64bd6dc770ec; LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221732265640b2fb-000165f0fabfca-4b5469-1296000-1732265640c14b%22%2C%22%24device_id%22%3A%221732265640b2fb-000165f0fabfca-4b5469-1296000-1732265640c14b%22%7D; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=7ce8498719f6fa6dc860be29752c6b5bd601792153e640f17132dabc575eb7aa; JSESSIONID=ABAAABAABEIABCI083761EA4B29732C336293C1BCA1EBFB; WEBTJ-ID=20200708213224-1732ea09d244ac-0d2b5f0b427e5d8-4b5b66-1296000-1732ea09d26b5; _putrc=4B52C1B8C3D1F68F123F89F2B170EADC; LGRID=20200712190953-2d43508f-d735-434a-b910-4030757e713a; X_HTTP_TOKEN=d53949df12d0e8da391255495166ed7510d61b51d5; login=true; unick=%E5%BD%AD%E6%B5%A9; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594552194; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=44ef93755bf2d7278c63c60db46352b9; LGSID=20200712190727-c2f30652-cb7e-4021-ad54-bfc49ab4b540; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; _gid=GA1.2.1424507660.1594552049; SEARCH_ID=3103c6d18c3648f9b0c7480d598314a1',
    'TE': 'Trailers'
    }
    while indx > 0 :
        response2 = requests.get(url_tmp,headers = headers)
        #response3 = newsession.get(url3, headers = headers, cookies = s.cookies)
        print(response2.status_code)
        selector = lxml.etree.HTML(response2.text)
        print(selector)

        for position in Selector(text=response2.text, type="html").xpath('//li[@class=\'con_list_item default_list\']'):
        #for position in selector.xpath('//li[@class=\'con_list_item default_list\']'):
        #for position in selector.xpath('//ul[@class="item_con_list"]/li'):

            positionname = position.xpath('@data-positionname')[0].extract()
            salary = position.xpath('@data-salary')[0].extract()
            print(positionname)
            print(salary)
            
            #add position
            positioninfo = {'city':city, 'position':positionname, 'salary':salary}

            if replication_info(positioninfo):
                print('replication infomation!!')
            else:
                indx = indx - 1
                mylist.append(positioninfo)
            print(mylist)

        page = page + 1
        url_tmp = url.format(url,city=city,page=page)


def replication_info(positioninfo):

    city = positioninfo['city']
    position = positioninfo['position']
    salary = positioninfo['salary']

    replication_flag = False
    for existedposition in mylist:
        if existedposition['city'] == city and existedposition['position'] == position and existedposition['salary'] == salary:
            replication_flag = True
            break

    return replication_flag   

def average_salary(postionlist):
    count = 0
    try:
        for positioninfo in mylist:
            
            city = positioninfo['city']
            salary = positioninfo['salary']

            salaryinfo = salary.split('-')
            lowsalary=salaryinfo.split('k')[0]
            highsalary=salaryinfo.split('k')[0]

            for totalinfo in totallist:
                
                tcity = totalinfo['city']
                if city == tcity:
                    totalinfo['lowsalary']= totalinfo['lowsalary'] + lowsalary
                    totalinfo['highsalary']= totalinfo['highsalary'] + highsalary
                    totalinfo['count'] = totalinfo['count'] +1

                if totalinfo['city'] is None:
                    count = count + 1
                    totoalpostionlist = {'city':city, 'lowsalary':lowsalary, 'highsalary':highsalary,'count':count}
                    totallist.append(totoalpostionlist)

    except Exception as e:
        print(e)
    for totalinfo in totallist:
        tcity = totalinfo['city']
        averagelowsalary= totalinfo['lowsalary']/totalinfo['count']
        averagehighsalary= totalinfo['highsalary']/totalinfo['count']
        averagepostionlist = {'city':tcity,'averagelowsalary':averagelowsalary,'averagepostionlist':averagepostionlist}
        totalaveragelistllist.append(averagepostionlist)

    return totalaveragelistllist

def main():
    global mylist
    mylist=[]
    totallist=[]
    averagelist=[]
    
    
    citys = ['beijing','shanghai','guangzhou','shenzhen']

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(requests_city, citys)

    average_result = average_salary(mylist)

    t_insertstring = 'insert into position_list(city_name,averagelowsalary,averagehighsalary) values (%s,%s,%s)'
    db_profile = '/Users/q/project/Python001-class01/week03/homework02/config.ini'
    t = connectMySQL(db_profile)
    t.run(t_insertstring,average_result)

if __name__ == '__main__':
    main()
'''
背景： 在数据分析的完整流程中 (数据收集、存储、清洗、展示)，数据收集的多少对最终分析结果有着直接影响，因此需要对外网的数据进行收集并整理，用于支持后续的分析。

要求：改造基于 requests 爬虫，增加多线程功能，实现通过拉勾网，获取 北、上、广、深四地 python 工程师的平均薪水待遇，并将获取结果存入数据库。

    通过多线程实现 requests 库的多线程方式。
    获取北京、上海、广州、深圳四个地区，各地区 100 个 python 工程师职位的职位名称和薪资水平。
    相同地区、相同职位及相同待遇的职位需去重。
    将获取的内容存入数据库中。
'''