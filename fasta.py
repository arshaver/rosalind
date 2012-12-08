def parse_fasta(filename):
	"""takes a file name with extension in the same directory as this file and returns a dict of name/seq pairs from a fasta doc"""
	with open("./"+filename,"r") as f:
		lines = f.readlines()
	fasta = {}
	for line in lines:
		if line[0] == ">":
			name = line.split(">")[1].strip()
		else:
			try:
				fasta[name] += line.strip()
			except:
				fasta[name] = line.strip()
	return fasta
