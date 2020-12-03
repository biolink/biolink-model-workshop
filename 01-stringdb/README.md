# STRING DB example

## Getting the data

First, we fetch the data from STRING DB: https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz

For the sake of an example, we will be using just a small subset from the file:
```
protein1 protein2 combined_score
9606.ENSP00000000412 9606.ENSP00000225275 195
9606.ENSP00000000412 9606.ENSP00000299767 222
9606.ENSP00000000412 9606.ENSP00000416097 474
9606.ENSP00000000412 9606.ENSP00000363458 902
9606.ENSP00000000412 9606.ENSP00000354376 161
9606.ENSP00000000412 9606.ENSP00000303366 285
9606.ENSP00000000412 9606.ENSP00000369981 900
9606.ENSP00000000412 9606.ENSP00000218548 210
9606.ENSP00000000412 9606.ENSP00000418915 267
```


From the above we know the following,
- These are human ENSEMBL proteins
- There are 10 interacting proteins
- Each interaction is qualified with a score


For modeling the above data we will make the following assumptions,
- Each protein is a node in the graph
- Each interaction is an edge in the graph
- Each identifier can be prefixed with `ENSEMBL` to yield a compact URI
- 9606 means `NCBITaxon:9606`


## Mapping to Biolink Model

- Each protein is of type `biolink:Protein`
- Each interaction is of type `biolink:GeneToGeneAssociation`
- The predicate/relationship that link two protein nodes is `biolink:interacts_with`
- The relation that further qualifies the interaction is [RO:0002434](https://www.ebi.ac.uk/ols/ontologies/ro/properties?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FRO_0002434)
- The interaction score can be represented as a property on the edge


## Putting it all together

[nodes.tsv](nodes.tsv) represents all the nodes in a graph in a TSV format.

A snippet of nodes.tsv,

```
id	category	in_taxon
ENSEMBL:ENSP00000000412	biolink:Protein	NCBITaxon:9606
ENSEMBL:ENSP00000225275	biolink:Protein	NCBITaxon:9606
...
```

[edges.tsv](edges.tsv) represents all the edges in a graph in a TSV format.

A snippet of edges.tsv,

```
subject	predicate	object	relation	association_type	combined_score
ENSEMBL:ENSP00000000412	biolink:interacts_with	ENSEMBL:ENSP00000225275	RO:0002434	biolink:GeneToGeneAssociation	195
ENSEMBL:ENSP00000000412	biolink:interacts_with	ENSEMBL:ENSP00000299767	RO:0002434	biolink:GeneToGeneAssociation	222
...
```

