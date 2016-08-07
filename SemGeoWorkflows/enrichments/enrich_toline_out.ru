

# Typing gis:toLine
INSERT 
{ 
#GRAPH ?g{
?out a gis:ObjectData; ada:hasElement _:oute.
_:oute ada:hasSupport ?object; 
ada:hasMeasure _:line . _:line a gis:Line.
?in2 a gis:Raster. 
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
?node a gis:toLine;
gis:inputdata ?in2;
wf:output ?out.
?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.  ?inm  a gis:Existence; wf:of ?object. #Are data blank nodes present? Then reuse them
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
