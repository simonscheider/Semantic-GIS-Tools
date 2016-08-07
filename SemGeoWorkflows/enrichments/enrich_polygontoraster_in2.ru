

# Typing gis:PolygontoRaster

#Set Input


INSERT 
{ 
#GRAPH ?g{ 
?ine ada:hasSupport _:inr. _:inr a gis:Region.
?in2 a gis:RegionDataSet.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PolygontoRaster;
gis:inputdata ?in2.
?in2 ada:hasElement ?ine.
FILTER NOT EXISTS{?ine ada:hasSupport ?ins. ?ins a gis:Region. }#Are data blank nodes present? Then reuse them
}
#}
}






