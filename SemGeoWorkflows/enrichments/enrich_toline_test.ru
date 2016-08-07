PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX  xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX  xml: <http://www.w3.org/XML/1998/namespace>
PREFIX  wf: <http://geographicknowledge.de/vocab/Workflow.rdf#>
PREFIX  gis: <http://geographicknowledge.de/vocab/GISConcepts.rdf#>
PREFIX  ada: <http://geographicknowledge.de/vocab/AnalysisData.rdf#>

# Typing gis:toLine

#Test
ASK {
#GRAPH ?g{
#?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.  ?inm wf:of ?object. 
#?out ada:hasElement ?oute . ?oute ada:hasSupport ?object.
#?object a ?class.
?a a gis:toLine;
gis:inputdata ?in2;
wf:output ?out.
}
#}