from manc import Request, Response
from manc.plugins import SpiderPlugin, UserAgentPlugin


class BaseSpider:
    plugins: list[SpiderPlugin] = []

    def on_request(self, request: Request):
        """请求之前"""
        for plugin in self.plugins:
            plugin.deal_request(request)

    def on_response(self, response: Response):
        """响应之后"""
        for plugin in self.plugins:
            response = plugin.deal_response(response)
        return response

    def add_plugin(self, plugin: SpiderPlugin):
        """加入扩展"""
        self.plugins.append(plugin)

    def add_plugins(self, plugins: list[SpiderPlugin]):
        """加入多个扩展"""
        for plugin in plugins:
            self.add_plugin(plugin)

    def goto(self, url: str, headers: dict = None, params: dict = None, data: dict | str = None, json: dict = None, proxies: dict = None, timeout: int | float = 5, **kwargs):
        """GET or POST"""
        same = dict(headers=headers, params=params, proxies=proxies, timeout=timeout, **kwargs)
        req = Request(url, **same) if data is None and json is None else Request(url, data=data, json=json, **same)
        return self.perform(req)

    def get(self, url: str, headers: dict = None, params: dict = None, proxies: dict = None, timeout=5, **kwargs):
        """GET"""
        req = Request(url, headers=headers, params=params, proxies=proxies, timeout=timeout, **kwargs)
        return self.perform(req)

    def post(self, url: str, headers: dict = None, params: dict = None, data: dict | str = None, json: dict = None, proxies: dict = None, timeout=5, **kwargs):
        """POST"""
        req = Request(url, headers=headers, params=params, data=data, json=json, proxies=proxies, timeout=timeout, **kwargs)
        return self.perform(req)

    def perform(self, request: Request):
        """处理请求，返回响应"""
        self.on_request(request)
        response = request.do()
        response = self.on_response(response)
        request.__dict__.update(response.request.__dict__)
        response.request = request
        return response


class Spider(BaseSpider):
    plugins: list[SpiderPlugin] = [UserAgentPlugin()]
