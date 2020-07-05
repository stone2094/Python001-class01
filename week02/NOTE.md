学习笔记

Exception
  1.basic struction of exception 
    try: except: else: finally:
  2.where do you need to consider exception?
  3.how do you define the custom exception
  4.how do you see the exception information in the log?
  5.
Cookie
  1.

Mysql
 1.how to reset password of root user for mysql when I forgot it
   a.stop mysql server
   b.cd /usr/local/mysql/bin
   c.sudo su
   d../mysql_safe --skip-grant-tables
   e.restart mysql server
   #in another terminal
   f.enter mysql
   g.flush privileges;
   h.set password for 'root'@'localhost'=password('newpassword');
   i../mysql -u root -h localhost -p


Webdriver
 1.download browser execute file should not be the total same version. when my browser version is 83.0.4103.116 and the chromedriver version is 83.0.4103.39, the code works.
 2.mac need to set for browser driver security

 --download site
 https://chromedriver.storage.googleapis.com/index.html 

Question:
 if the user-agent is random, we use webdriver to login the website. How to match the uses-agent to browser?
