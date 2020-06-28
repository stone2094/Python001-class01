# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlmoviesPipeline:
        
    def process_item(self, item, spider):
        #print('pipeline:',item)
        moviename = item['moviename']
        movietype = item['movietype']
        releasedate = item['releasedate']

        output = f'|{moviename}|\t|{movietype}|\t|{releasedate}|\n\n'
        #print(output)
        #save items into a csv file
        with open('./movie_homeworko2.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
