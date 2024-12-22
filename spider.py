from manc import Request, Response
from manc.plugins import SpiderPlugin, UserAgentPlugin


class BaseSpider:
    plugins: list[SpiderPlugin] = []

    def on_request(self, request: Request):
        for plugin in self.plugins:
            plugin.deal_request(request)

    def on_response(self, response: Response):
        for plugin in self.plugins:
            response = plugin.deal_response(response)
        return response

    def add_plugin(self, plugin: SpiderPlugin):
        self.plugins.append(plugin)

    def add_plugins(self, plugins: list[SpiderPlugin]):
        for plugin in plugins:
            self.add_plugin(plugin)

    def goto(self, url: str, headers: dict = None, params: dict = None, data: dict | str = None, json: dict = None, proxies: dict = None, timeout: int | float = 5, **kwargs):
        if data is None and json is None:
            request = Request(url, headers=headers, params=params, proxies=proxies, timeout=timeout, **kwargs)
        else:
            request = Request(url, headers=headers, params=params, data=data, json=json, proxies=proxies, timeout=timeout, **kwargs)
        self.on_request(request)
        response = self.on_response(request.do())
        request.__dict__.update(response.request.__dict__)
        response.request = request
        return response

    def get(self, url: str, headers: dict = None, params: dict = None, proxies: dict = None, timeout: int | float = 5, **kwargs):
        req = Request(url, headers=headers, params=params, proxies=proxies, timeout=timeout, **kwargs)
        return self.perform(req)

    def post(self, url: str, headers: dict = None, params: dict = None, data: dict | str = None, json: dict = None, proxies: dict = None, timeout: int | float = 5, **kwargs):
        req = Request(url, headers=headers, params=params, data=data, json=json, proxies=proxies, timeout=timeout, **kwargs)
        return self.perform(req)

    def perform(self, request: Request):
        self.on_request(request)
        response = request.do()
        response = self.on_response(response)
        request.__dict__.update(response.request.__dict__)
        response.request = request
        return response


class Spider(BaseSpider):
    plugins: list[SpiderPlugin] = [UserAgentPlugin()]
