# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Request
from ..items import AtmosParserSingleItem
import re


class SingleLinkerSpider(CrawlSpider):
    name = 'single_linker'
    allowed_domains = ['atmos.illinois.edu']
    start_urls = ['https://www.atmos.illinois.edu/cms/One.aspx?portalId=127458&pageId=151114']
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['full_name', 'phone', 'email', 'biography']
    }

    def parse(self, response):
        for r in response.xpath('//div[@id="page_content"]'):
            items = AtmosParserSingleItem()
            full_name = r.xpath('//div[@id="full_name"]/h1/text()').extract()
            biography = r.xpath('//div[@id="news_content_body"]').xpath('//div[@class="img-responsive"]//text()').extract()
            contact_div = r.xpath('//div[@id="contact_info"]')
            items['email'] = contact_div.xpath('//a[@id="email"]/text()').extract()
            items['full_name'] = full_name
            items['biography'] = biography
            phone = r.xpath('//div[@id="contact_info"]//text()').extract()
            phone = ''.join(phone)
            phone = re.findall('\D?(\d{0,3}?)\D{0,2}(\d{3})?\D{0,2}(\d{3})\D?(\d{4})', phone)
            try:
                items['phone'] = '-'.join(phone[0])
            except:
                items['phone'] = ''
            yield items