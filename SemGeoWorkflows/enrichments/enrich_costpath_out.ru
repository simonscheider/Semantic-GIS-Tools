
# Typing gis:CostPath
INSERT 
{ 
#GRAPH ?g{
?out a gis:Raster; ada:hasElement [ada:hasMeasure [ a gis:Existence ;  wf:of [ a gis:Path]]].
?link2 a gis:Raster. #?linkm a gis:Link.
?source2 a gis:Raster. #?object a ada:Object.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:CostPath;
wf:output ?out;
gis:source ?source2;
gis:linkraster ?link2.
#?source2  ada:hasElement ?se. ?se ada:hasMeasure ?sm. ?sm a gis:Existence; wf:of ?object. #Are data blank nodes present? Then reuse them
#?link2 ada:hasElement ?linke. ?linke ada:hasMeasure ?linkm. #Are data blank nodes present? Then reuse them
}
#}
}





