# 说明

- 一款可以接入自定义扩展的爬虫

## 示例

- 简单演示

```python
from manc.plugins import UserAgentPlugin
from manc.spider import BaseSpider

url = 'https://blog.csdn.net/MarkAdc'

# 1. 基础爬虫
s1 = BaseSpider()
r1 = s1.goto(url)  # 响应对象可以直接使用Xpath、CSS
print(type(r1))
print(r1.request.headers)
print(r1.xpath("//title/text()").get())
print()

# 2. 标准爬虫，等价于 基础爬虫 + ua插件
s2 = BaseSpider()
s2.add_plugins([UserAgentPlugin()])
r2 = s2.goto(url)  # 请求带了UA
print(type(r2))
print(r2.request.headers)
print(r2.xpath("//title/text()").get())
print()

```

- 自定义扩展演示

```python
from manc import Spider
from manc.plugins import SpiderPlugin


class ProxyPlugin(SpiderPlugin):
    def deal_request(self, request):
        proxy = 'http://127.0.0.1:1082'
        request.proxies = {"http": proxy, "https": proxy}
        request.name = "cMan"

    def deal_response(self, response):
        return response


s = Spider()
s.add_plugin(ProxyPlugin())

url = 'http://www.baidu.com'
r = s.goto(url)
print(type(r), type(r.request))
print(r.request.name)
print(r.request.headers)
print(r.request.proxies)
print(r.get_one("//title/text()"))
print(r.get_all("//title/text()"))

```