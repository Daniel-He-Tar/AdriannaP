from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Adrianaalier(BasePortiaSpider):
    name = "adrianaalier.com"
    allowed_domains = [u'adrianaalier.com']
    start_urls = [u'http://adrianaalier.com/']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'http://adrianaalier.com/en/coleccion-*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem, None, '', [Field(u'Container', '', []), Field(
        u'DressName', '', []), Field(u'DressPic', '', [])])]]
