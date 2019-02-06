from lxml import etree
import os
import json

directory = os.environ['CRAWLED_DIR']
filenames = os.listdir(directory)

if os.path.exists(os.path.join(os.getcwd(), 'results')):
	pass
else:
	os.mkdir('results')

for filename in filenames:
	file = open(directory+'/'+filename)
	root = etree.HTML(file.read())
	jsonfile = dict()
	subject = root.xpath(".//h1/span/text()")[0]
	jsonfile["subject"] = subject
	courses = root.xpath(".//div[contains(@class, 'media-body')]")
	coursesjsonfile = []
	for course in courses:
		coursejsonfile = dict()
		coursejsonfile["course number & title"] = course.xpath(".//h3/text()")[0]
		coursejsonfile["Number of units"] = course.xpath(".//p[1]/text()")[0]
		if len(course.xpath(".//p[2]/text()"))>0:
			coursejsonfile["Course description"] = course.xpath(".//p[2]/text()")[0]
		coursesjsonfile.append(coursejsonfile)
	jsonfile["courses"] = coursesjsonfile
	with open('results/'+filename.replace('.html','')+'.json', 'w+') as outfile:  
		json.dump(jsonfile, outfile)