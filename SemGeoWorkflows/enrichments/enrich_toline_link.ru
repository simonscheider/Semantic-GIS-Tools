

# Typing gis:toLine
INSERT 
{ 
#GRAPH ?g{
#?out a ada:ObjectDataSet. 
?oute ada:hasSupport ?object. 
?object a ada:Object.
?in a gis:Raster. 
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
?node a gis:toLine;
gis:inputdata ?in;
wf:output ?out.
?in ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.  ?inm  a gis:Existence; wf:of ?object. #Are data blank nodes present? Then reuse them
?out ada:hasElement ?oute. 
#OPTIONAL
}
#}
#Test
#SELECT ?class
#WHERE {GRAPH ?g{
#?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.  ?inm wf:of ?object. 
#?out ada:hasElement ?oute . ?oute ada:hasSupport ?object.
#?object a ?class
#}}
