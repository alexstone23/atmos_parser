# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy import Request
from ..items import AtmosParserSingleItemExtended
import re


class PeopleParserSpider(CrawlSpider):
    name = 'people_parser'
    allowed_domains = ['atmos.illinois.edu']
    start_urls = ['https://www.atmos.illinois.edu/cms/One.aspx?portalId=127458&pageId=127468']
    extracted_links = []
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['full_name', 'titles', 'image_link', 'phone', 'email', 'website', 'education', 'biography']
    }

    def parse_items(self, response):
        for r in response.xpath('//div[@id="page_content"]'):
            items = AtmosParserSingleItemExtended()
            titles = r.xpath('//div[@id="titles"]/ul/li/text()').extract()
            items['titles'] = [t.replace(',', '').strip() for t in titles]
            try:
                items['image_link'] = r.xpath('//img[@id="photograph"]/@src').extract()[0]
            except:
                print('There is no photo in profile')
                pass
            full_name = r.xpath('//div[@id="full_name"]/h1/text()').extract()
            biography = r.xpath('//div[@id="news_content_body"]').xpath('//div[@class="img-responsive"]//text()').extract()
            contact_div = r.xpath('//div[@id="contact_info"]')
            items['email'] = contact_div.xpath('//a[@id="email"]/text()').extract()
            items['full_name'] = full_name
            items['biography'] = biography
            items['website'] = contact_div.xpath('//a[@id="website_link"]/@href').extract()
            phone = r.xpath('//div[@id="contact_info"]//text()').extract()
            phone = ''.join(phone)
            phone = re.findall('\D?(\d{0,3}?)\D{0,2}(\d{3})?\D{0,2}(\d{3})\D?(\d{4})', phone)
            try:
                items['phone'] = '-'.join(phone[0])
            except:
                items['phone'] = ''
            items['education'] = r.xpath('//div[@id="education"]/ul/li/text()').extract()
            yield items

    def parse(self, response):
        for r in response.xpath('//a[@class="link"]/@href').extract():
            yield Request(response.urljoin(r), callback=self.parse_items)
