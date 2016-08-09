
# Typing gis:CostPath
INSERT 
{ 
#GRAPH ?g{
?in ada:hasElement [ada:hasMeasure _:inm].
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:CostPath;
wf:input ?in.
FILTER NOT EXISTS {?in ada:hasElement ?ine. ?ine ada:hasMeasure ?inm}
}
#}
}





