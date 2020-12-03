# Build the Graph

Using the information from [01-stringdb](01-stringdb), [02-mapping](02-mapping), and [03-metadata](03-metadata), we can build a more self-describing graph where,

- Each gene is of type `biolink:Gene`
- Each protein is of type `biolink:Protein`
- Each interaction is of type `biolink:GeneToGeneAssociation`
- The predicate/relationship that link two protein nodes is `biolink:interacts_with`
- The relation that further qualifies the interaction is [RO:0002434](https://www.ebi.ac.uk/ols/ontologies/ro/properties?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_0002434)
- The interaction score can be represented as a property on the edge
- Each link between a gene and its protein can be represented via the `biolink:has_gene_product`
- The relation that further qualifies the link is [RO:0002205](https://www.ebi.ac.uk/ols/ontologies/ro/properties?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_0002205)
- Each gene node can have an `xref` property that holds its alternate NCBIGene identifier
- Each genomic location information is of type `biolink:GenomicSequenceLocalization`
- The predicate/relationship that links a genomic entity to a reference sequence is `biolink:has_sequence_location`
- The relation that further qualifies the link is `faldo:location`
- The location information can be represented as properties on the edge



[graph_nodes.tsv](graph_nodes.tsv) represents all the nodes in the final graph in a TSV format.

A snippet of nodes.tsv,

nodes.tsv
```
id	category	name	symbol	xref	synonym	in_taxon
ENSEMBL:ENSG00000003056	biolink:Gene	mannose-6-phosphate receptor, cation dependent	M6PR	HGNC:6752|NCBIGene:4074	46-kDa mannose 6-phosphate receptor|CD Man-6-P receptor|Mr 46,000 Man6PR|cation-dependent mannose-6-phosphate receptor|small mannose 6-phosphate receptor	NCBITaxon:9606
ENSEMBL:ENSG00000005381	biolink:Gene	myeloperoxidase	MPO	HGNC:7218|NCBIGene:4353	myeloperoxidase	NCBITaxon:9606
...
```


[graph_edges.tsv](graph_edges.tsv) represents all the nodes in the final graph in a TSV format.

edges.tsv
```
subject	predicate	object	relation	association_type	combined_score	start_interbase_coordinate	end_interbase_coordinate	strand
ENSEMBL:ENSG00000003056	biolink:interacts_with	ENSEMBL:ENSG00000005381	RO:0002434	biolink:GeneToGeneAssociation	195			
ENSEMBL:ENSG00000003056	biolink:interacts_with	ENSEMBL:ENSG00000166598	RO:0002434	biolink:GeneToGeneAssociation	222			
...
```

## Loading into Neo4j

One can easily load this graph into Neo4j using [KGX](https://github.com/biolink/kgx) with the following command,

```sh
kgx neo4j-upload --input-format tsv \
                    --uri http://localhost:7474 \
                    --username neo4j \
                    --password test \
                    graph_nodes.tsv graph_edges.tsv
```

> The above command assumes that you have a Neo4j running locally and is available at http://localhost:7474
