from decimal import Decimal

with open("./rosalind_gc.txt","r") as f:
	lines = f.readlines()

data = {}
for line in lines:
	if line[0] == ">":
		name = line.split(">")[1].strip()
	else:
		try:
			data[name] += line.strip()
		except:
			data[name] = line.strip()

def gc(seq):
	gc_count = seq.count("G") + seq.count("C")
	return float(gc_count)/float(len(seq))*100

gc_data = {}
for name,seq in data.iteritems():
	gc_data[name] = gc(seq)

max_name = max(gc_data,key=gc_data.get)
print max_name
print str(Decimal(gc_data[max_name]).quantize(Decimal('0.001')))+"%"