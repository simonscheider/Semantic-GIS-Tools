

# Typing gis:PointtoRaster
#Set inputs
INSERT 
{ 
#GRAPH ?g{ 
?ine ada:hasSupport _:inr. _:inr a gis:Point.
?in2 a gis:PointDataSet.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PointtoRaster;
gis:inputdata ?in2.
?in2 ada:hasElement ?ine.
FILTER NOT EXISTS{?ine ada:hasSupport ?ins. ?ins a gis:Point. }#Are data blank nodes present? Then reuse them
}
#}
}







