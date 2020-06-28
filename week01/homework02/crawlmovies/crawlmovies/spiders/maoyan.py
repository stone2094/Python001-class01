# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from crawlmovies.items import CrawlercateyesItem
from fake_useragent import UserAgent
import requests

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3']
    '''
    s = requests.Session()

    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    form_data = {
    'ck':'',
    'name':'18642827832',
    'password':'',
    'remember':'false',
    'ticket':''
    }

    response = s.post(login_url, data = form_data, headers = headers)
    '''
    def __init__(self):

        ua = UserAgent(verify_ssl=False)
        cookies ='uuid_n_v=v1; uuid=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; _csrf=32877a02a8d04b39e3f222e6b4252e292c0973a18db32cd60d8b7d80615581a7; _lxsdk_cuid=172f3f8be8ac8-08fdf560b8b4c8-4b5469-13c680-172f3f8be8ac8; _lxsdk=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593322824,1593325788,1593326784,1593329244; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593329643; __mta=210704298.1593231064909.1593329612118.1593329643898.10; mojo-uuid=3533b1aaa282adefb81243b93761bc8c; _lxsdk_s=172f9d295ab-797-515-18d%7C2900928695%7C11; mojo-trace-id=6; mojo-session-id={"id":"f2a1ad2fe8089f04afc747818abf15fe","time":1593329228886}'
        #referers = 'https://maoyan.com/'
        self.header = {'cookies':str(cookies),'user-agent':ua.random}

    def start_requests(self):
        url='http://maoyan.com/films?showType=3'
        #url='file:///Users/chen/OneDriver/geektime/demo/1.html'
        #ua = UserAgent(verify_ssl=False)
        ##user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        #cookies ='uuid_n_v=v1; uuid=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; _csrf=32877a02a8d04b39e3f222e6b4252e292c0973a18db32cd60d8b7d80615581a7; _lxsdk_cuid=172f3f8be8ac8-08fdf560b8b4c8-4b5469-13c680-172f3f8be8ac8; _lxsdk=37ADCBB0B82C11EA85DD839D6F814C7A07C97AE801FF4DC8BD8250A845B873E6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593305449,1593308972,1593310036,1593318776; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593321055; __mta=210704298.1593231064909.1593312846816.1593321056335.7; mojo-uuid=3533b1aaa282adefb81243b93761bc8c; _lxsdk_s=172f955df82-3c1-251-34b%7C2900928695%7C4; mojo-trace-id=2; mojo-session-id={"id":"e2246e6cacb3c12d44a9b30afd5c2f25","time":1593321055374}'
        ##referers = 'https://maoyan.com/'
        
        #header = {'cookies':str(cookies),'user-agent':ua.random}

        return [scrapy.Request(url=url, callback=self.parse, headers=self.header, dont_filter=False)]
        
    def parse(self, response):
        #url
        b_url = 'http://maoyan.com'
        print('response.url:',response.url)
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
