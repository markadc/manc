from manc.plugins import UserAgentPlugin
from manc.spider import BaseSpider, Spider

url = 'https://blog.csdn.net/MarkAdc'

# 1. 基础爬虫
s1 = BaseSpider()
r1 = s1.goto(url)  # 响应对象可以直接使用Xpath、CSS
print(type(r1))
print(r1.request.headers)
print(r1.xpath("//title/text()").get())
print()

# 2. 基础爬虫 + ua插件
s2 = BaseSpider()
s2.add_plugins([UserAgentPlugin()])
r2 = s2.goto(url)  # 请求带了UA
print(type(r2))
print(r2.request.headers)
print(r2.xpath("//title/text()").get())
print()

# 3. 标准爬虫，等价于 基础爬虫 + ua插件
s3 = Spider()
