


# Typing gis:CostDistance
#Set input
INSERT 
{ 
#GRAPH ?g{
?cs2  ada:hasElement _:cse. _:cse ada:hasMeasure _:csm. #Are data blank nodes present? Then reuse them
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:CostDistance;
gis:costsurface ?cs2.
FILTER NOT EXISTS{
?cs2  ada:hasElement ?cse. ?cse ada:hasMeasure ?csm.} #Are data blank nodes present? Then reuse them
}
#}
}







