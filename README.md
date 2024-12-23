# 说明

- 一款可以接入自定义扩展的爬虫

## 示例

### 简单演示

```python
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

```

### 自定义扩展演示

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

## 实战演示

### 爬取抖音

- 爬取直播间是否在直播

```python
import re

from manc import Spider

s = Spider()


def is_living(live_url):
    r1 = s.get(live_url, cookies={"__ac_nonce": "..."})
    match_list = re.findall(r'"roomId\\":\\"(\d+)\\",', r1.text)
    room_id = match_list[0]
    ttwid = r1.cookies.get('ttwid')

    live_id = live_url.split('/')[-1]
    url = "https://live.douyin.com/webcast/room/web/enter/"
    params = {
        "aid": "6383",
        "app_name": "douyin_web",
        "live_id": "1",
        "device_platform": "web",
        "language": "zh-CN",
        "enter_from": "page_refresh",
        "cookie_enabled": "true",
        "screen_width": "1920",
        "screen_height": "1080",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Edge",
        "browser_version": "131.0.0.0",
        "web_rid": live_id,
        "room_id_str": room_id,
        "enter_source": "",
        "is_need_double_stream": "false",
        "insert_task_id": "",
        "live_reason": "",
    }
    r2 = s.get(url, params=params, cookies={"ttwid": ttwid})
    jsonData = r2.json()
    room_status = jsonData["data"]["room_status"]
    return True if room_status == 0 else False


if __name__ == '__main__':
    url = "https://live.douyin.com/646454278948"  # 抖音【与辉同行】直播间
    status = is_living(url)
    print(status)
```