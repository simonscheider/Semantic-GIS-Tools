
# Typing gis:CostPath
INSERT 
{ 
#GRAPH ?g{
?out ada:hasElement [ada:hasMeasure _:outm].
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:CostPath;
wf:output ?out.
FILTER NOT EXISTS {?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm}
}
#}
}





