# Gene metadata

## Getting the data

We fetch more information about each of our gene from [MyGene.info](https://mygene.info/) using the [biothings-client](https://pypi.org/project/biothings-client/).

> MyGene.info is an API that provides information about genes and other bioentities.
> 
> biothings-client is a Python library that makes it easy to query MyGene.info and parse the results from the API.

Following is an exerpt from the [gene_metadata.tsv](gene_metadata.tsv) file:
```
id	name	symbol	dbxref	synonyms	chr	start	end	strand
ENSG00000147889	cyclin dependent kinase inhibitor 2A	CDKN2A	HGNC:1787|NCBIGene:1029	CDK4 inhibitor p16-INK4|alternative reading frame|cell cycle negative regulator beta|cyclin-dependent kinase 4 inhibitor A|cyclin-dependent kinase inhibitor 2A|cyclin-dependent kinase inhibitor 2A (melanoma, p16, inhibits CDK4)|multiple tumor suppressor 1	9	21967753	21995301	-1
ENSG00000003056	mannose-6-phosphate receptor, cation dependent	M6PR	HGNC:6752|NCBIGene:4074	46-kDa mannose 6-phosphate receptor|CD Man-6-P receptor|Mr 46,000 Man6PR|cation-dependent mannose-6-phosphate receptor|small mannose 6-phosphate receptor	12	8940361	8949761	-1
ENSG00000167110	golgin A2	GOLGA2	HGNC:4425|NCBIGene:2801	130 kDa cis-Golgi matrix protein|GM130 autoantigen|Golgi matrix protein GM130|SY11 protein|golgi autoantigen, golgin subfamily a, 2|golgin subfamily A member 2|golgin-95	9	128255829	128275995	-1
...
```

From the above we get additional information about each of our gene, including its genomic location.

For the sake of representation we will make the following assumptions,
- Each gene is a node in the graph- Each gene is a node in the graph
- Each identifier can be prefixed with `ENSEMBL` to yield a compact URI
- Genomic location information can be represented as an edge in the graph


## Mapping to Biolink Model

- Each gene is of type `biolink:Gene`
- Each reference/chromosome is of type `biolink:GenomicEntity`
- Each genomic location information is of type `biolink:GenomicSequenceLocalization`
- The predicate/relationship that links a genomic entity to a reference sequence is `biolink:has_sequence_location`
- The relation that further qualifies the link is `faldo:location`
- The location information can be represented as properties on the edge


## Putting it all together

[nodes.tsv](nodes.tsv) represents all the nodes in a graph in a TSV format.

A snippet of nodes.tsv,

```
id	category	name	symbol	xref	synonym	in_taxon
ENSEMBL:ENSG00000003056	biolink:Gene	mannose-6-phosphate receptor, cation dependent	M6PR	HGNC:6752|NCBIGene:4074	46-kDa mannose 6-phosphate receptor|CD Man-6-P receptor|Mr 46,000 Man6PR|cation-dependent mannose-6-phosphate receptor|small mannose 6-phosphate receptor	NCBITaxon:9606
ENSEMBL:ENSG00000005381	biolink:Gene	myeloperoxidase	MPO	HGNC:7218|NCBIGene:4353	myeloperoxidase	NCBITaxon:9606
...
```

[edges.tsv](edges.tsv) represents all the edges in a graph in a TSV format.

A snippet of edges.tsv,

```
subject	predicate	object	relation	association_type	start_interbase_coordinate	end_interbase_coordinate	strand
ENSEMBL:ENSG00000003056	biolink:has_sequence_location	NUCCORE:NC_000012	biolink:GenomicSequenceLocalization	faldo:location	8940361	8949761	-1
ENSEMBL:ENSG00000005381	biolink:has_sequence_location	NUCCORE:NC_000017	biolink:GenomicSequenceLocalization	faldo:location	58269855	58280935	-1
...
```
