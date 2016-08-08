


# Typing gis:CostDistance
#Set input
INSERT 
{ 
#GRAPH ?g{
?sink2 ada:hasElement _:sinke. _:sinke ada:hasMeasure _:sinkm.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:CostDistance;
gis:sink ?sink2.
FILTER NOT EXISTS{
?sink2 ada:hasElement ?sinke. ?sinke ada:hasMeasure ?sinkm.} #Are data blank nodes present? Then reuse them
}
#}
}







