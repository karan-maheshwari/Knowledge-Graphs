import rltk
import pandas as pd
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

ds1 = pd.read_csv(f1)
ds1['id'] = f1+":"+(ds1.index+2).astype(str)
ds2 = pd.read_csv(f2)
ds2['id'] = f2+":"+(ds2.index+2).astype(str)


class Record1(rltk.Record):

	@property
	def id(self):
		return self.raw_object['id']

	@property
	def address(self):
		return self.raw_object['Address']

	@property
	def phone(self):
		return self.raw_object['Phone']

	@property
	def cuisine(self):
		return self.raw_object['Cuisine']


class Record2(rltk.Record):

	@property
	def id(self):
		return self.raw_object['id']

	@property
	def address(self):
		return self.raw_object['Address']

	@property
	def phone(self):
		return self.raw_object['Phone']

	@property
	def cuisine(self):
		return self.raw_object['Cuisine']


ds1 = rltk.Dataset(reader=rltk.DataFrameReader(ds1), record_class=Record1, adapter=rltk.MemoryKeyValueAdapter())
ds2 = rltk.Dataset(reader=rltk.DataFrameReader(ds2), record_class=Record2, adapter=rltk.MemoryKeyValueAdapter())

'''bg = rltk.HashBlockGenerator()
blocks = bg.generate(bg.block(ds1, property_='cuisine'), bg.block(ds2, property_='cuisine'))
pairs = rltk.get_record_pairs(ds1, ds2, block=blocks)'''

pairs = rltk.get_record_pairs(ds1, ds2)

f = open('similarities.txt', 'w+')

for r1, r2 in pairs:

	a_d = rltk.levenshtein_similarity(r1.address, r2.address)
	p_d = rltk.jaro_winkler_similarity(r1.phone, r2.phone)
	c_d = rltk.jaro_winkler_similarity(r1.cuisine, r2.cuisine)
	f.write(r1.id+","+r2.id+","+str(a_d)+","+str(p_d)+","+str(c_d)+"\n")

f.close()
