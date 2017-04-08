.. image:: https://badge.fury.io/py/torbrowser-headers.svg
     :target: http://badge.fury.io/py/torbrowser-headers
     :alt: PyPI version

.. image:: https://requires.io/github/mezrin/torbrowser-headers/requirements.svg?branch=master
     :target: https://requires.io/github/mezrin/torbrowser-headers/requirements/?branch=master
     :alt: Requirements Status

##################
torbrowser-headers
##################

Collection of HTTP headers (including User-Agent) of different versions of Tor Browser.
Scrapy middleware that picks up random headers.

#####
Usage
#####

::

    import random
    from tor_browser_headers.headers import tor_browser_headers_list

    torBrowserHeaders = random.choice(tor_browser_headers_list)
    print('Version of Tor Browser: {}'.format(torBrowserHeaders.tor_browser_version))
    for header in torBrowserHeaders.headers:
        print('\t{}: {}'.format(header.name, header.value))

####################
Scrapy configuration
####################

Enable middleware
-----------------

Turn off the built-in ``DefaultHeadersMiddleware`` and ``UserAgentMiddleware``, enable ``TorBrowserHeadersMiddleware``.

In Scrapy >=1.0:

::

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.useragent.DefaultHeadersMiddleware': None,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'torbrowser-headers.middleware.TorBrowserHeadersMiddleware': 500,
    }

In Scrapy <1.0:

::

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.DefaultHeadersMiddleware': None,
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'torbrowser-headers.middleware.TorBrowserHeadersMiddleware': 400,
    }

Configuring headers type (Optional)
-----------------------------------

By default, Scrapy middleware sets the default values for all HTTP headers,
so the request looks like it was made by the Tor Browser that was just installed.
But you can limit list of headers that should be modified.
Add lines in your ``settings.py``:

::

    from torbrowser-headers.model import HTTPHeaderType

    TOR_BROWSER_HEADERS__TYPES = [HTTPHeaderType.UserAgent,
                                  HTTPHeaderType.Accept,
                                  HTTPHeaderType.AcceptLanguage,
                                  HTTPHeaderType.AcceptEncoding,
                                  HTTPHeaderType.Connection]

Do not forget to enable ``DefaultHeadersMiddleware`` if you need only ``User-Agent``

Configure to use with `scrapy-proxies` (Optional)
-------------------------------------------------

To use with middlewares of random proxy such as `scrapy-proxies <https://github.com/aivarsk/scrapy-proxies>`_, you need:

1. set ``TOR_BROWSER_HEADERS__CONSTANT_HEADERS_FOR_PROXY`` to ``True`` to use headers of only one version of TorBrowser with a proxy

2. set priority of ``TorBrowserHeadersMiddleware`` to be greater than ``scrapy-proxies``, so that proxy is set before handle headers


.. |GitHub version| image:: https://badge.fury.io/gh/mezrin%2Ftorbrowser-headers.svg
   :target: http://badge.fury.io/gh/mezrin%2Ftorbrowser-headers
.. |Requirements Status| image:: https://requires.io/github/mezrin/torbrowser-headers/requirements.svg?branch=master
   :target: https://requires.io/github/mezrin/torbrowser-headers/requirements/?branch=master
