# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlmoviesPipeline:
        # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        #print('pipeline:',item)
        moviename = item['moviename']
        movietype = item['movietype']
        releasedate = item['releasedate']
        #print("**********************")
        #print(releasedate)
        output = f'|{moviename}|\t|{movietype}|\t|{releasedate}|\n\n'
        #print(output)
        with open('./movie_homeworko2.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
