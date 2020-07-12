import pymysql
import configparser 
import os
 
class connectMySQL(object):
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
        configpath = os.path.join(root_dir, "homework02/config.ini")
        print(configpath)

    def get_cursor(self):
        return self.conn.cursor()
 
    def querydb(self,sql):
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
        #close connection
        #self.conn.close()


if __name__ == '__main__':
 
    querystring = 'select * from test.position_list'
    t_insertstring = 'insert into position_list(city_name,averagelowsalary,averagehighsalary) values (%s,%s,%s)'
    insertstring = 'insert into position_list(city_name,averagelowsalary,averagehighsalary) values ("beijing","15k")'
    db_profile = '/Users/q/project/Python001-class01/week03/homework02/config.ini'
    data = ('beijing','15k')
    t = connectMySQL(db_profile)
    #t_insertomovie = t.run(insertstring)
    t_insertomovie = t.querydb(insertstring)
    t_insertomovie_date = t.run(t_insertstring,data)
    t_movielist = t.querydb(querystring)
    print(t_movielist)
    t.conn.close()