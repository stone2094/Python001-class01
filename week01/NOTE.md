学习笔记
0.安装
 0.1 使用豆瓣源下载包 pip install xxx -i https://pypi.douban.com/simple
 0.2 安装全部依赖包 pip install -r requirements.txt

1.xpath语法的学习
 1.1 基本语法
 1.2 如何在浏览器中测试xpath的正确性
     在开发者界面的console中$x('//div[@class="movie-item-hover"]')
 1.3 

 相关链接：
   r1. Scrapy Xpath 官方学习文档： https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
   r2. Xpath 中文文档：
     https://www.w3school.com.cn/xpath/index.asp
   r3. Xpath 英文文档：
     https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf 

2.scrapy的学习
 2.1 start_request方法是可以自己定义request的请求方式，在第一周的作业中是用这个方法实现翻页的多次请求
 2.2 如果使用pipeline一定要在setting文件打开pipeline的设置
 2.3 
 
 相关链接：

3.yield的学习

  相关链接：
  2. yield 表达式官方文档：
    https://docs.python.org/zh-cn/3.7/reference/expressions.html#yieldexpr
  3. yield 语句官方文档
    https://docs.python.org/zh-cn/3.7/reference/simple_stmts.html#yield
  4. Python 推导式官方文档：
    https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html#list-comprehensions 

4.如何反爬
  4.1 增加user-agent
  4.2 增加cookie
    4.2.1 直接获取一个访客的cookie
    4.2.2 注册网站用户，用自己的用户登陆后可以在post（302）方法中拿到cookie
  4.3 如何判断自己的ip被服务器封了？
  4.4:
  相关链接：
    

5.异常处理
  5.1 异常类型

  相关链接：
   r1. pretty_errors 官方文档链接：
     https://pypi.org/project/pretty-errors/
   r2. try 语句官方文档：
     https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement
   r3. with 语句官方文档：
     https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement
   r4. with 语句上下文管理器官方文档：
     https://docs.python.org/zh-cn/3.7/reference/datamodel.html#with-statement-context-managers

其他：
  o1: extract使提取内容转换为Unicode字符串，返回数据类型为list
  	<ul class="list">
   	  <li>123</li>
   	  <li>abc</li>
  	</ul> 
  	xx.xpath("./ul[@class='list']/li").extract()
  	#output
  	#['123','abc]
  o2: Convert a List to String
     	list1 = ['a','b']
	''.join(list)
	#output
	#ab
