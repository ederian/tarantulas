#~ from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from coolmath.items import CoolmathItem

#~ to run spider: scrapy crawl coolmath4kids -o test.json -t json
class Coolmath2(CrawlSpider):
	name = 'coolmathSUX'
	#~ allowed_domains = ['coolmath4kids.com']
	start_urls = ['http://www.coolmath4kids.com']
	allowed_domains = ['coolmath4kids.com']
	rules = (
		Rule(SgmlLinkExtractor(allow=()), follow = True, callback = 'parse_page'),
		)

	def parse_page(self, response):
		hxs = HtmlXPathSelector(response)
		item = CoolmathItem()
		item['link'] = response.url
		item['title'] = hxs.select('/html/head/title/text()').extract()
		garbage = hxs.select('//*/font/text()').extract()
		gold = []
		for gar in garbage:
			gold.append(gar.replace('\n','').replace('\t','').replace('|','').strip())
		item['text'] = ' '.join(gold)
		return item

SPIDER = Coolmath2()

