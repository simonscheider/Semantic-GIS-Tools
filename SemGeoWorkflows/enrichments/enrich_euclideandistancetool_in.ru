

#Set Input
INSERT 
{ #GRAPH ?g{ 
?in a ada:DataSet; ada:hasElement [ada:hasSupport [ a ada:Object]; ada:hasMeasure [a ada:Spatial]].
#}
}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:EuclideanDistanceTool;
gis:inputdata ?in.
FILTER NOT EXISTS{?in ada:hasElement ?ine . ?ine ada:hasSupport ?ins. ?ine ada:hasMeasure ?inm }#Are data blank nodes present? Then reuse them
}
#}
}

