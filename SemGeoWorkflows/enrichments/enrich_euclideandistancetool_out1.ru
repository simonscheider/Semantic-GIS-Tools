

# Typing gis:EuclideanDistance


#Insert output
INSERT 
{ #GRAPH ?g{
?out a gis:Raster; ada:hasElement _:oute. _:oute ada:hasMeasure _:outm. 
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:EuclideanDistanceTool;
wf:output ?out.
FILTER NOT EXISTS{?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm}
}
#}
}
