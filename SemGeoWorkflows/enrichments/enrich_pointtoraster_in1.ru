


# Typing gis:PointtoRaster
#Set inputs
INSERT
{ 
#GRAPH ?g{
?in2 ada:hasElement _:ine. _:ine ada:hasMeasure _:inm.  _:inm a gis:Quality. # This reuses data blank nodes if present
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PointtoRaster;
gis:inputdata ?in2.
FILTER NOT EXISTS {?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.} #Are data blank nodes present? Then reuse them
}
#}
}







