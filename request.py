import requests

from manc.response import Response


class Request:
    """请求对象"""

    def __init__(self, url: str, method="GET", headers: dict = None, params: dict | str = None, data: dict = None, json: dict = None, proxies: dict = None, timeout: int | float = 5, **kwargs):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data
        self.json = json
        self.proxies = proxies
        self.timeout = timeout
        self.kwargs = kwargs

    def do(self):
        same = dict(headers=self.headers, params=self.params, proxies=self.proxies, timeout=self.timeout, **self.kwargs)
        if self.method == "GET":
            response = requests.get(self.url, **same)
        elif self.method == "POST":
            response = requests.post(self.url, data=self.data, json=self.json, **same)
        else:
            raise ValueError("Method must be GET or POST")
        return Response(response)
