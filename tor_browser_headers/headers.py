from .model import HTTPHeaderType, HTTPHeader, TorBrowserInitialHeaders

tor_browser_headers_list = [
    TorBrowserInitialHeaders(
        '6.5.1 (based on Mozilla Firefox 45.8.0)',
        [HTTPHeader(HTTPHeaderType.UserAgent, 'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0'),
         HTTPHeader(HTTPHeaderType.Accept, 'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
         HTTPHeader(HTTPHeaderType.AcceptLanguage, 'Accept-Language', 'en-US,en;q=0.5'),
         HTTPHeader(HTTPHeaderType.AcceptEncoding, 'Accept-Encoding', 'gzip, deflate'),
         HTTPHeader(HTTPHeaderType.Connection, 'Connection', 'keep-alive')])
]
