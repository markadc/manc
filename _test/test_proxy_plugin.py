from manc import Spider
from manc.plugins import SpiderPlugin


class ProxyPlugin(SpiderPlugin):
    def process_request(self, request):
        proxy = 'http://127.0.0.1:1082'
        request.proxies = {"http": proxy, "https": proxy}
        request.name = "cMan"

    def process_response(self, response):
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
