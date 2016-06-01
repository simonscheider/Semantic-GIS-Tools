#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simon
#
# Created:     24-04-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
from rdflib import *
g=rdflib.Graph()
#g.load('http://linkedgeodata.org/data/triplify/node376142577?output=ttl', format='turtle')



sparql = SPARQLWrapper("http://linkedgeodata.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT *
    WHERE { ?x ?link ?y. FILTER(?x IN (<http://linkedgeodata.org/triplify/node376142577>, <http://linkedgeodata.org/triplify/node253128737>)). }
""")
print '\n\n*** JSON Example'
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
#print results

for result in results["results"]["bindings"]:
    #print result['x']['value'] +" "+result['link']['value'] +" "+result['y']['value']
    if result['y']['type'] == 'literal':
        y = Literal(result['y']['value'])
    else:
        y = URIRef(result['y']['value'])
    g.add((URIRef(result['x']['value']), URIRef(result['link']['value']),y))

for s,p,o in g:
  print s,p,o

#import RDFClosure as rdfc

#gg = rdfc.DeductiveClosure(rdfc.RDFS_Semantics).expand(g)