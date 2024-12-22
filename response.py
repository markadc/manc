from parsel import Selector
from requests import Response as Resp


class Response(Resp):
    """响应对象"""

    def __init__(self, response: Resp):
        super().__init__()
        self.__dict__.update(response.__dict__)
        self.selector = Selector(text=response.text)

    def __str__(self):
        return "<Response {}>".format(self.status_code)

    def xpath(self, query: str):
        sel = self.selector.xpath(query)
        return sel

    def css(self, query: str):
        sel = self.selector.css(query)
        return sel

    def get_one(self, query: str, default=None, strip=True):
        q = self.selector.xpath(query)
        v = q.get(default)
        if v is None:
            return v
        return v.strip() if strip else v

    def get_all(self, query: str, strip=True):
        vs = [v.strip() if strip else v for v in self.selector.xpath(query).getall()]
        return vs
