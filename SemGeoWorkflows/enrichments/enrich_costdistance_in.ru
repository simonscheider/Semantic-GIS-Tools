


# Typing gis:CostDistance
#Set input
INSERT 
{ 
#GRAPH ?g{
?cs2  ada:hasElement _:cse. _:cse ada:hasMeasure _:csm. #Are data blank nodes present? Then reuse them
?sink2 ada:hasElement _:sinke. _:sinke ada:hasMeasure _:sinkm.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:CostDistance;
gis:costsurface ?cs2;
gis:sink ?sink2.
FILTER NOT EXISTS{?cs2  ada:hasElement ?cse. ?cse ada:hasMeasure ?csm. #Are data blank nodes present? Then reuse them
?sink2 ada:hasElement ?sinke. ?sinke ada:hasMeasure ?sinkm.} #Are data blank nodes present? Then reuse them
}
#}
}







