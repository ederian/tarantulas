from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from coolmath.items import CoolmathItem

#~ to run spider: scrapy crawl coolmath4kids -o test.json -t json
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
		urls = []
		for page in pages:
			if page[:2] == '..':
				url = '/'.join(response.url.split('/')[:3]) + '/' + page.replace('../','')
				urls.append(url)
			else:
				if response.url == self.start_urls[0]:
					url = 'http://www.coolmath4kids.com/' + page
					urls.append(url)
				else:
					url = '/'.join(response.url.split('/')[:-1]) + '/' + page
					urls.append(url)
		for url in urls:
			if url not in self.tha_list:
				self.tha_list.append(url)
			yield Request(url, callback = self.parse)


	def parse_page(self, response):
		hxs = HtmlXPathSelector(response)
		item = CoolmathItem()
		item['link'] = response.url
		item['title'] = hxs.select('/html/head/title/text()').extract()
		item['text'] = hxs.select('//*/p/font/b/text()').extract()
		return item

SPIDER = Coolmath4kids()

