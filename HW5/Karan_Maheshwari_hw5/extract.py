from lxml import etree
from lxml import html
from bs4 import BeautifulSoup
import json
from pyld import jsonld
import os
import sys

inputdir = sys.argv[1]
output_filename = sys.argv[2]

indexes = json.load(open(inputdir+"/index.json", "r+"))
final = []
for page in os.listdir(inputdir):

	if "json" in page:
		continue

	tree = html.fromstring(open(inputdir+"/"+page, "r+").read())

	tree = tree.xpath('//meta[@property]')

	context = {"@vocab": "http://ogp.me/ns/","og": "http://ogp.me/ns#"}

	d = {"@id":indexes[page]}

	for t in tree:
		if "og" in t.xpath('@property')[0]:
			if "type" in t.xpath('@property')[0]:
				d["@type"] = "http://ogp.me/ns#"+t.xpath('@content')[0]
			else:
				d[t.xpath('@property')[0]] = t.xpath('@content')[0]


	final.append(jsonld.compact(d, context))

f = open(output_filename, "w+")

f.write(json.dumps(final))

