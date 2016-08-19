
# Typing gis:CostPath
INSERT 
{ 
#GRAPH ?g{
?out a gis:Raster. ?outm a gis:Existence ;  wf:of [ a gis:Path].
?link2 a gis:Raster. ?linkm a gis:Link.
?source2 a gis:Raster. ?sourcem a gis:Existence; wf:of [ a gis:ObjectDataSet].
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
?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm.
?source2 ada:hasElement ?source. ?source ada:hasMeasure ?sourcem.
?link2 ada:hasElement ?linke. ?linke ada:hasMeasure ?linkm.
}
#}
}





