# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from crawlmovies.items import CrawlercateyesItem
from fake_useragent import UserAgent
import requests

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://passport.meituan.com/account/unitivelogin?']

    '''
    def __init__(self):

        self.ua = UserAgent(verify_ssl=False)
        self.headers = {
            'User-Agent' : self.ua.Firefox,
            'Referer' : 'https://passport.meituan.com/account/unitivelogin?'
            }

        self.login_url = 'https://passport.meituan.com/account/unitivelogin?'
        #form data
        self.form_data = {
            "countrycode":"86",
            "email":"18642827832",
            "password":"Spring2014!",
            "origin":"account-login",
            #"csrf":"JnLRL194-eZiJsF5PwsJZd46YraguhNBOaPk",
            "requestCode":"",
            "responseCode":"",
            #"h5Fingerprint":"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",
            "device_name":"",
            "device_type":"Firefox",
            "device_os":"Mac",
            "sdkType":"pc"
        }

        self.se = requests.Session()
        pre_login = 'https://passport.meituan.com/account/unitivelogin?'
        pre_resp = self.se.get(pre_login, headers=self.headers)

        response = self.se.post(self.login_url, data=self.form_data, headers=self.headers, cookies=self.se.cookies)
        #print(response.text)
        print("---------------------------------------")
        print(self.se.cookies)

    def start_requests(self):
        url='http://maoyan.com/films?showType=3'
        #cookies ='uuid_n_v=v1; uuid=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; _csrf=32877a02a8d04b39e3f222e6b4252e292c0973a18db32cd60d8b7d80615581a7; _lxsdk_cuid=172f3f8be8ac8-08fdf560b8b4c8-4b5469-13c680-172f3f8be8ac8; _lxsdk=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593305449,1593308972,1593310036,1593318776; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593321055; __mta=210704298.1593231064909.1593312846816.1593321056335.7; mojo-uuid=3533b1aaa282adefb81243b93761bc8c; _lxsdk_s=172f955df82-3c1-251-34b%7C2900928695%7C4; mojo-trace-id=2; mojo-session-id={"id":"e2246e6cacb3c12d44a9b30afd5c2f25","time":1593321055374}'
        ##referers = 'https://maoyan.com/'
        header = {
            'Cookies' : str(self.se.cookies),
            'User-Agent' : self.ua.Firefox
            }
        print('----starting request----')
        return [scrapy.Request(url=url, callback=self.parse, headers=header)]
    '''
    def __init__(self):

        ua = UserAgent(verify_ssl=False)
        cookies ='uuid_n_v=v1; uuid=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; _csrf=32877a02a8d04b39e3f222e6b4252e292c0973a18db32cd60d8b7d80615581a7; _lxsdk_cuid=172f3f8be8ac8-08fdf560b8b4c8-4b5469-13c680-172f3f8be8ac8; _lxsdk=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593911782,1593950967,1593951682,1593953019; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593953946; __mta=210704298.1593231064909.1593321142354.1593953946484.8; mojo-uuid=3533b1aaa282adefb81243b93761bc8c; _lxsdk_s=1731ee14f08-ce7-afe-843%7C%7C24; mojo-trace-id=15; mojo-session-id={"id":"52c5fbd84ad14a38b3e9c7a3abc42660","time":1593950949210}'
        #referers = 'https://maoyan.com/'
        self.header = {'cookies':str(cookies),'user-agent':ua.random}

    def start_requests(self):
        url='http://maoyan.com/films?showType=3'

        return [scrapy.Request(url=url, callback=self.parse, headers=self.header, dont_filter=False)]
         
    def parse(self, response):
        #url
        b_url = 'http://maoyan.com'
        print('----response.url----',response.url)
        ind = 0

        #movie position 
        movies = Selector(text=response.text, type="html").xpath('//div[@class="movie-item-hover"]')
        for movie in movies:
            title = movie.xpath('./a//div[@class="movie-hover-title"][1]/span[@class="name "]/text()')
            link = movie.xpath('./a/@href')
            item = CrawlercateyesItem()
            print(len(title.extract()))

            #covered movie with score and noscore
            if len(title.extract()) >= 1:
                item['moviename'] = title.extract()[0]
            else:
                titlenoscore = movie.xpath('./a//div[@class="movie-hover-title"][1]/span[@class="name noscore"]/text()')
                item['moviename'] = titlenoscore.extract()[0]
            

            item['movielink'] = link.extract()[0]
            
            ind = ind + 1
            #for 10 movies
            if ind <=10:
                yield scrapy.Request(url=b_url+str(link.extract()[0]), meta={'item': item}, callback=self.parse2, headers=self.header)
                #yield scrapy.Request(url=b_url+str(link.extract()[0]), meta={'item': item}, callback=self.parse2)
            else:
                break

        #enter into detail of the movie
    def parse2(self, response):
        item = response.meta['item']
        #print(response.text)
        releasedate = ''
        moviedetail = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul')
        print(moviedetail)
        for mdl in moviedetail:
            print(mdl.xpath('./li[1]'))
            #get moive type
            for indtype in mdl.xpath('./li[1]'):
                types = indtype.xpath('./a/text()').extract()
                #movietypes = movietypes + str(indtype.xpath('./a/text()').extract()[0])
            
            #get release date
            releasedate = moviedetail.xpath('./li[3]/text()').extract()[0]
        
        
        print(releasedate)
        #combine the elements of the list of movie type
        item['movietype'] = ''.join(types)
        item['releasedate'] = releasedate
        print('init:',item)
        yield item