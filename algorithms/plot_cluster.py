import json
import sys

edges2 = []
edge_w = []
fn = sys.argv[1]

with open(sys.argv[1]) as f:
    g_dict = json.load(f)
    for k,v in g_dict.iteritems():
    	print k,len(v)


