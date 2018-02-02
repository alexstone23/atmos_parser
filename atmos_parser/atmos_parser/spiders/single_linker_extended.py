# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from ..items import AtmosParserSingleItemExtended
import re


class SingleLinkerSpider(CrawlSpider):
    name = 'single_linker_extended'
    allowed_domains = ['atmos.illinois.edu']
    start_urls = ['https://www.atmos.illinois.edu/cms/One.aspx?portalId=127458&pageId=151114']
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['full_name', 'titles', 'image_link', 'phone', 'email', 'website', 'education', 'biography']
    }

    def parse(self, response):
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
            items['phone'] = re.findall('([\S][\d][\S]??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', phone)
            items['education'] = r.xpath('//div[@id="education"]/ul/li/text()').extract()
            yield items