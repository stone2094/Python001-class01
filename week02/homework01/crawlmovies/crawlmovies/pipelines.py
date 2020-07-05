# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class CrawlmoviesPipeline:
        
    def process_item(self, item, spider):
        print('pipeline:',item)
        moviename = item['moviename']
        movietype = item['movietype']
        releasedate = item['releasedate']

        '''
        output = f'|{moviename}|\t|{movietype}|\t|{releasedate}|\n\n'       
        #print(output)
        save items into a csv file
        with open('./movie_homeworko2.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        '''
        data = (moviename,movietype,releasedate)
        #insert into mysql
        try:
            insertsql = 'insert into movie_list(movie_name,movie_type,release_date) values (%s,%s,%s)'
            db_profile = '/Users/q/project/Python001-class01/week02/homework01/crawlmovies/config.ini'
            dbconn = Mysqldb(db_profile)
            dbconn.run(insertsql,data)

        except Exception as e:
            print(e)

        return item

class Mysqldb:

    def  __init__(self,profile):

        config = configparser.ConfigParser()
        #config.read("Config.ini", encoding="utf-8")
        config.read(profile)
        
        host = config.get('mysql','host')
        port = int(config.get('mysql','port'))
        user = config.get('mysql','user')
        password = config.get('mysql','password')
        db = config.get('mysql','db')

        db_config = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'db': db
            }
            
        self.conn = pymysql.connect(**db_config)

        root_dir = os.path.dirname(os.path.abspath('.'))
        print(root_dir)
        configpath = os.path.join(root_dir, "homework01/crawlmovies/config.ini")
        print(configpath)

    def get_cursor(self):
        return self.conn.cursor()
 
    def query(self,sql):
        cursor = self.get_cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                 print(row)
                 return row

            self.conn.commit()
        except Exception as e:
            print('unexcept happened at the query sql',str(e))
            self.conn.rollback()
        #close connection
        #self.conn.close()

    def run(self,sql,data):
        # 游标建立的时候就开启了一个隐形的事物
        cursor = self.get_cursor()
        try:
            cursor.execute(sql,data)   
            self.conn.commit()
        except Exception as e:
            print('unexcept happened at the execute sql',str(e))
            self.conn.rollback()