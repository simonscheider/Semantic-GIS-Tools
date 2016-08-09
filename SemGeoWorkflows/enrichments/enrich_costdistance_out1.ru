

# Typing gis:CostDistance


#Set output
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
?node a gis:CostDistance;
wf:output ?out.
FILTER NOT EXISTS{
?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm.} #Are data blank nodes present? Then reuse them
}
#}
}





