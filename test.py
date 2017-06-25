import random
from tor_browser_headers.headers import tor_browser_headers_list

torBrowserHeaders = random.choice(tor_browser_headers_list)
print('Version of Tor Browser: {}'.format(torBrowserHeaders.tor_browser_version))
for header in torBrowserHeaders.headers:
    print('\t{}: {}'.format(header.name, header.value))
