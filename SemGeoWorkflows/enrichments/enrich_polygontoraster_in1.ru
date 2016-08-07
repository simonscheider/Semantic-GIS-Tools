

# Typing gis:PolygontoRaster

#Set Input
INSERT 
{ 
#GRAPH ?g{ 
?in2 ada:hasElement _:ine. _:ine ada:hasMeasure _:inm. _:inm a gis:Quality.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PolygontoRaster;
gis:inputdata ?in2.
FILTER NOT EXISTS{?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm. ?inm a gis:Quality. }#Are data blank nodes present? Then reuse them
}
#}
}






