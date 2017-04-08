import enum


class HTTPHeaderType(enum.Enum):
    UserAgent = 0
    Accept = 1
    AcceptLanguage = 2
    AcceptEncoding = 3
    Connection = 4


class HTTPHeader:
    def __init__(self, header_type, header_name, header_value):
        self.type = header_type
        self.name = header_name
        self.value = header_value


class TorBrowserInitialHeaders:
    def __init__(self, tor_browser_version, headers):
        self.tor_browser_version = tor_browser_version
        self.headers = headers

    def __repr__(self):
        return '<{}({})>'.format(self.__class__.__name__,
                                 '; '.join('{}: {}'.format(h.name, h.value) for h in self.headers))
