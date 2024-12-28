from manc import Request, Response
from manc.errs import ResponseCodeError
from manc.tools import make_ua


class SpiderPlugin:
    """爬虫扩展，处理请求和响应"""

    def process_request(self, request: Request):
        pass

    def process_response(self, response: Response) -> Response:
        return response


class UserAgentPlugin(SpiderPlugin):
    """请求扩展，为每一次的请求分配随机UA"""

    def process_request(self, request: Request):
        request.headers = request.headers or {}
        request.headers.setdefault('User-Agent', make_ua())


class StatusCodePlugin(SpiderPlugin):
    """响应扩展，检查每一次的响应，响应的状态码不在范围内则抛出异常"""

    def __init__(self, pass_codes: list = None):
        self.pass_codes = pass_codes or [200]

    def process_response(self, response: Response):
        if response.status_code not in self.pass_codes:
            raise ResponseCodeError("{} not in {}".format(response.status_code, self.pass_codes))
        return response
