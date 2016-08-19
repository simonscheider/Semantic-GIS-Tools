

# Typing gis:CostDistance


#Set output
INSERT 
{ 
#GRAPH ?g{
?out a gis:Raster. ?outm  a gis:Link ; wf:of ?sink2; wf:of ?csm.
?cs2 a gis:Raster. ?csm a gis:Cost.
?sink2 a gis:Raster. ?sinkm a gis:Existence; wf:of _:object. _:object a gis:ObjectDataSet.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:CostDistance;
wf:output ?out;
gis:costsurface ?cs2;
gis:sink ?sink2.
?cs2  ada:hasElement ?cse. ?cse ada:hasMeasure ?csm. #Are data blank nodes present? Then reuse them
?sink2 ada:hasElement ?sinke. ?sinke ada:hasMeasure ?sinkm. #Are data blank nodes present? Then reuse them
?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm.
} #Are data blank nodes present? Then reuse them

#}
}





