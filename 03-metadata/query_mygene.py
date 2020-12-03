import os
from biothings_client import get_client


def process_mygene_record(data):
	result = {}
	for k, v in data.items():
		if k in ['HGNC', 'entrezgene', 'name', 'symbol', 'other_names', 'genomic_pos']:
			if k == 'other_names' and isinstance(v, str):
				result[k] = [v]
			else:
				result[k] = v
	return result


def print_header():
	header = ['id', 'name', 'symbol', 'dbxref', 'synonyms', 'chr', 'start', 'end', 'strand']
	print('\t'.join(header))


def print_result(k, r):
	rec = [
		k, r['name'], r['symbol'],
		'|'.join([f"HGNC:{r['HGNC']}", f"NCBIGene:{r['entrezgene']}"]), '|'.join(r['other_names']),
		r['genomic_pos']['chr'], str(r['genomic_pos']['start']), str(r['genomic_pos']['end']), str(r['genomic_pos']['strand'])
	]
	print('\t'.join(rec))


mg = get_client('gene')
genes = set()

with open('ENSEMBL/mapping.tsv') as FH:
	for line in FH:
		if line.startswith('protein'):
			continue
		element = line.split('\t')
		genes.add(element[1])

print_header()

for g in genes:
	d = mg.getgene(g)
	r = process_mygene_record(d)
	print_result(g, r)
