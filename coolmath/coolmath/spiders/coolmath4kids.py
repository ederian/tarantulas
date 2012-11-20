from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from coolmath.items import CoolmathItem


class Coolmath4kids(BaseSpider):
	name = 'coolmath4kids'
	#~ allowed_domains = ['coolmath4kids.com']
	start_urls = ['http://www.coolmath4kids.com']

	tha_list = []
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		# get all links from from page
		pages = hxs.select('//*/a/@href').extract()

		# Filter out links leading away from start_urls
		for page in pages[:]:
			if page[:7] == 'http://':
				pages.remove(page)
		for page in pages:
			if page[:2] == '..':
				url = 'http://www.coolmath4kids.com' + page.replace('../','/')
			else:
				url = response.url[:-10] + page
			url = str(response).replace('<200 ','').replace('>','') + '/' + page
			yield Request(url, callback = self.parse_page)


	def parse_page(self, response):
		hxs = HtmlXPathSelector(response)
		item = CoolmathItem()
		item['link'] = response.url
		item['title'] = hxs.select('/html/head/title/text()').extract()
		pages = hxs.select('//*/a/@href').extract()
		for page in pages:
			if page[:2] == '..':
				url = 'http://www.coolmath4kids.com' + page.replace('../','/')
			else:
				url = response.url[:-10] + page
			if url not in self.tha_list:
				yield Request(url, callback = self.parse)
			self.tha_list.append(url)

SPIDER = Coolmath4kids()
