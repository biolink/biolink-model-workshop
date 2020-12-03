# Gene to Protein Information from NCBI

## Getting the data

We first fetch data on Ensembl genes from NCBI FTP: [ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2ensembl.gz](ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2ensembl.gz)

And from that we extract relevant records to create a mapping file:
```
protein	gene	dbxref
ENSP00000000412	ENSG00000003056	4074
ENSP00000225275	ENSG00000005381	4353
ENSP00000299767	ENSG00000166598	7184
ENSP00000416097	ENSG00000167110	2801
ENSP00000363458	ENSG00000157978	26119
ENSP00000354376	ENSG00000132698	57111
ENSP00000303366	ENSG00000169223	10960
ENSP00000369981	ENSG00000107295	6456
ENSP00000218548	ENSG00000075673	479
ENSP00000418915	ENSG00000147889	1029
```

From the above we know the following,
- Each protein has a correponding gene mapping
- Each entry in the dbxref column is referring to the NCBI gene identifier

For modeling the above data we will make the following assumptions,
- Each gene is a node in the graph
- Each protein is a node in the graph
- Each Ensembl identifier can be prefixed with `ENSEMBL` to yield a compact URI
- Each NCBI gene identifier can be prefixed with `NCBIGene` to yield a compact URI
- The link between a gene and its protein can be represented as an edge in the graph


## Mapping to Biolink Model

- Each gene is of type `biolink:Gene`
- Each protein is of type `biolink:Protein`
- Each link between a gene and its protein can be represented via the `biolink:has_gene_product`
- The relation that further qualifies the link is [RO:0002205](https://www.ebi.ac.uk/ols/ontologies/ro/properties?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_0002205)
- Each gene node can have an `xref` property that holds its alternate NCBIGene identifier


## Putting it all together

[nodes.tsv](nodes.tsv) represents all the nodes in a graph in a TSV format.

A snippet of nodes.tsv,

```
id	category	in_taxon
ENSEMBL:ENSG00000003056	biolink:Gene	NCBITaxon:9606
ENSEMBL:ENSG00000005381	biolink:Gene	NCBITaxon:9606
ENSEMBL:ENSP00000000412	biolink:Protein	NCBITaxon:9606
ENSEMBL:ENSP00000218548	biolink:Protein	NCBITaxon:9606
...
```

[edges.tsv](edges.tsv) represents all the edges in a graph in a TSV format.

A snippet of edges.tsv,

```
subject	predicate	object	relation	association_type	combined_score
ENSEMBL:ENSG00000003056	biolink:interacts_with	ENSEMBL:ENSG00000005381	RO:0002434	biolink:GeneToGeneAssociation	195
ENSEMBL:ENSG00000003056	biolink:interacts_with	ENSEMBL:ENSG00000166598	RO:0002434	biolink:GeneToGeneAssociation	222
ENSEMBL:ENSG00000003056	biolink:has_gene_product	ENSEMBL:ENSP00000000412	RO:0002205		
ENSEMBL:ENSG00000005381	biolink:has_gene_product	ENSEMBL:ENSP00000225275	RO:0002205	
...
```
