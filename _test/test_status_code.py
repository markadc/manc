from manc import Spider
from manc.plugins import StatusCodePlugin

s = Spider()
s.add_plugin(StatusCodePlugin([500]))
url = "https://www.baidu.com"
r = s.goto(url)
print(r)
