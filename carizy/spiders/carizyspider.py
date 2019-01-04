# -*- CODING: PTYHON V2 -*-
from carizy.items import CarizyItem
from scrapy import Request
import scrapy

class CarizyspiderSpider(scrapy.Spider):
    name = 'carizyspider'
    #start_urls = ['http://www.carizy.com/voiture-occasion?page={i}'

    allowed_domains = ['carizy.com']
    custom_settings = {
    'LOG_FILE': 'logs/carizy.log',
    'LOG_LEVEL':'ERROR'
	}

    def start_requests(self):
    	start_url = "http://www.carizy.com/voiture-occasion?page={i}"
    	for i in range(0,66):
    		yield Request(start_url.format(i=i), self.parse)

    def parse(self, response):
        print('PROCESSING...' + response.url)

        for annonce in response.xpath("//div[contains(@class,'col-lg-8 col-md-8 col-sm-8 col-xs-7')]"):
            item = CarizyItem()
            try:
            	item['TITLE'] = annonce.css('h2.title-model::text').extract_first()
            except:
            	print('ERROR TITLE PARSE...' + response.url)
            try:
            	item['ANNONCE_LINK'] = response.urljoin(annonce.css('a::attr(href)').extract_first())
	    except:
	    	print('ERROR ANNONCE LINK PARSE...' + response.url)

	    yield item