from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from carizy.spiders.carizy_spider_3_1_2019 import CarizySpider312019Spider

process = CrawlerProcess(get_project_settings())
process.crawl(CarizySpider312019Spider)
process.start()
