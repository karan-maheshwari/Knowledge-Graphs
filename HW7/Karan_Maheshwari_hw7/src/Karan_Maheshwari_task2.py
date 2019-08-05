f = open('similarities.txt', 'r+')

similar = []

for line in f:

	r1_id = line.split(",")[0]
	r2_id = line.split(",")[1]
	a_d = line.split(",")[2]
	p_d = line.split(",")[3]
	c_d = line.split(",")[4]

	if float(a_d)*0.6+float(p_d)*0.3+float(c_d)*0.1 >= 0.755:
		similar.append((r1_id, r2_id))

f.close()

f = open('output.txt', 'w+')

for row in similar:
	f.write(row[0]+"\t"+row[1]+"\n")

f.close()
