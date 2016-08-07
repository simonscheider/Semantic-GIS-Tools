

# Typing gis:EuclideanDistance


#Insert output
INSERT 
{ #GRAPH ?g{
?out a gis:Raster; ada:hasElement [ada:hasMeasure [ a gis:EuclDistance; wf:of ?in ; wf:of _:sf]]. _:sf a gis:SField. 
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:EuclideanDistance;
wf:output ?out;
gis:inputdata ?in.
}
#}
}
