

# Typing gis:PolygontoRaster

#Set Input
INSERT 
{ 
?in2 ada:hasElement _:ine. _:ine ada:hasMeasure _:inm. _:inm a ada:Quality.
}

#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PolygontoRaster;
gis:inputdata ?in2.
FILTER NOT EXISTS{?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm. }#Are data blank nodes present? Then reuse them
}
#}
}






