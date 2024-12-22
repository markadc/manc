from abc import abstractmethod, ABC

from manc.tools import make_ua


class SpiderPlugin(ABC):
    """爬虫扩展，抽象类"""

    @abstractmethod
    def deal_response(self, response):
        pass

    @abstractmethod
    def deal_request(self, request):
        pass


class UserAgentPlugin(SpiderPlugin):
    """请求插件，为每一次的请求分配随机UA"""

    def deal_request(self, request):
        request.headers = request.headers or {}
        request.headers.setdefault('User-Agent', make_ua())

    def deal_response(self, response):
        return response
