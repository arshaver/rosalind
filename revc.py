def rev_comp(seq):
	"""docstring for rev-comp"""
	output = ""
	comp = {"A":"T","C":"G","T":"A","G":"C"}
	for base in seq:
		output+=comp[base]
	return output[::-1]

print rev_comp("ATACTCGCCCAAGATTTCGCGCCTCCAATCATTCATCCACCGCTGTCGTTGCGTCCTTCGGGGACGATCACATCTGGGGAGTCCAAGCTGGAGGCGTGACCTGGTCGATGCGGGTGTAGCGCGCGGGAACGCGACATAGTATGACGTGTAGCCTAACGTGACAGAGACGGAAGAGGGTCGAGCGGCCGTAATGGAATTGAAGCCTCGGCATAGTACAGAGATTTTGTTGCGCTTATTAGGCCGGTAGCAACGCATGATCCGTTTGAAGCCCTGCAACCCCGTTCTTTTTTATGTATTGAAGCCATTGATTATAGATGGTCTATTGGCGAGAACACGACAAGGCCAAGTTGAATTTATCGACTGTTTTAATCTCTCCTCCTTATGACTAGCATCAGACATGCTGTTCGCCTGCAGTCCACTAGTCCTGGTGCTAAGGCACGAGGGAATTGTGGAACCACGGACGTAAGCATCTCCAACTTGCAAATAGTCGAATCACACGAATGAAGGGATTAGGGCGTATTAGCCCCAGGGATCCTGTGACAAGAAGTCCCCTTACGATGAAATACGATTAGAGTGTTGTCGGTTCCTCAAGAATGATGGTTCTATACCGCATGAATGTCAGAGTTCACGATTCGACCTCGGCAACGGGTGTTCACGACGTGCATAATTCTTTTATTACGGACTGATAGTAGTTTCATTATCGCGGGCGCGACTTGCAACGTAATCCTACCTCATTAGGGAGATCCGGACCTCTCACTCACCTGTTGCTATCTGTCTAAGGAGTAGAGCAAAGGCGAGAACCCTATCTGTCGACCGCCCTTCACCTCTAAAGGCAGCTCGTAGACTTCCTATAGCCGG")