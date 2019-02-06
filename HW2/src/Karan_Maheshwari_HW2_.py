import scrapy
import os

if os.path.exists(os.path.join(os.getcwd(), 'data')):
	pass
else:
	os.mkdir('data')

class CourseDescriptionSpider(scrapy.Spider):

	name = 'hw2Spider'
	start_urls = ['https://www.registrar.ucla.edu/Academics/Course-Descriptions']
	hostname = 'https://www.registrar.ucla.edu'

	def parse(self, response):
		rows = response.css('div.list-letter div.row')
		for row in rows:
			coursenames = row.css('ul tr li a::text').extract()
			links = row.css('ul tr li a::attr("href")').extract()
			for i in range(len(coursenames)):
				link = self.hostname + links[i]
				req = scrapy.Request(url = link, callback = self.parseCoursePage)
				req.meta['c_name'] = coursenames[i]
				yield req

	def parseCoursePage(self, response):
		f = open('data/'+response.meta['c_name'].replace('/',' ')+'.html','wb')
		f.write(response.body)
		f.close()