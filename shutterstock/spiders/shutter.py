import scrapy
from shutterstock.items import ShutterstockItem
class BrickSetSpider(scrapy.Spider):
	name = "shutter"
	start_urls = ['https://www.shutterstock.com/search/selfie?page=1']
	
	def parse(self, response):
		EML_SELECTOR = 'div.search-content img'
		#yield {'my_test': response.css(EML_SELECTOR).extract_first()}

		for i in response.css(EML_SELECTOR):
			#yield {'my_test': i.css('img ::attr(src)').extract_first()}
			link = i.css('img ::attr(src)').extract_first()
			if str(link)[37:42] == 'photo':
				yield ShutterstockItem(file_urls=[link])

		next_page = 'ul.pagination li:nth-of-type(3) a ::attr(href)'
		#yield {'next_page': response.css(next_page).extract_first()}
		if response.css(next_page).extract_first():
			page = 'https://www.shutterstock.com' + response.css(next_page).extract_first()
			yield scrapy.Request(page, self.parse)




