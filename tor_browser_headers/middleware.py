import random

from .model import HTTPHeaderType
from .headers import tor_browser_headers_list


class TorBrowserHeadersMiddleware:
    """
    Class used as a Scrapy downloader middleware to set HTTP headers of Tor Browser to outgoing requests.
    """

    def __init__(self, crawler):
        self.types = crawler.settings.getlist('TOR_BROWSER_HEADERS__TYPES', list(HTTPHeaderType))
        self.per_proxy = crawler.settings.getbool('TOR_BROWSER_HEADERS__CONSTANT_HEADERS_FOR_PROXY', False)
        self.proxy2headers = {}

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        # choose which headers to use
        if self.per_proxy:
            proxy = request.meta.get('proxy')
            if proxy not in self.proxy2headers:
                self.proxy2headers[proxy] = random.choice(tor_browser_headers_list)
                spider.logger.debug('Tor-Browser headers assigned to the Proxy {}: {}'
                                    .format(proxy, self.proxy2headers[proxy]))
            torBrowserHeaders = self.proxy2headers[proxy]
        else:
            torBrowserHeaders = random.choice(tor_browser_headers_list)

        # set headers
        for header in torBrowserHeaders.headers:
            if header.type in self.types:
                request.headers.setdefault(header.name, header.value)
