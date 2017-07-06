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


class Adriannapapell(BasePortiaSpider):
    name = "www.adriannapapell.com"
    allowed_domains = [u'www.adriannapapell.com']
    start_urls = [u'http://www.adriannapapell.com/']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'/platinum'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'#pdpMain',
                [
                    Field(
                        u'Dress_Image',
                        '.product-col-1 > .product-thumbnails > .swiper-container > .nav > .selected > .thumbnail-link > .productthumbnail::attr(src)',
                        []),
                    Field(
                        u'Dress_Name',
                        '.product-col-2 > .product-name *::text',
                        []),
                    Field(
                        u'sizes',
                        '.product-col-2 > div > .product-variations > ul > .Size > .value > .swatches *::text',
                        []),
                    Field(
                        u'Dress_Description',
                        '.product-col-2 > div > .product-description *::text',
                        [])])]]
