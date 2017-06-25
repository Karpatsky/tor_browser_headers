from setuptools import setup

setup(
    name='tor-browser-headers',
    version='1.0.0',
    description='Collection of HTTP headers (including User-Agent) of different versions of Tor Browser.' +
                'Scrapy middleware that picks up random headers.',
    long_description=open('README.rst').read(),
    keywords='tor tor-browser http-headers user-agent scrapy proxy web-scraping',
    license='New BSD License',
    author="Victor Mezrin",
    author_email='victor@mezrin.com',
    url='https://github.com/mezrin/tor_browser_headers',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=['tor_browser_headers'],
    install_requires=[]
)
