import sys
from collections import defaultdict

nodem = {}
s = -1
with open(sys.argv[1], 'r') as f:
    for line in f:
    	a,b,w = line.split("\t")[:3]
    	if a not in nodem:
    		s = s+1
    		nodem[a] = s
    	if b not in nodem:
    		s = s+1
    		nodem[b] = s

fp = open("gene_names.txt",'w')
for k,v in nodem.iteritems():
	fp.write(k+"\n")

fp.close()
