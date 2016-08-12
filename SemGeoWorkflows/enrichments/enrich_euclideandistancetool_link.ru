
# Typing gis:EuclideanDistance


#Insert output
INSERT 
{ #GRAPH ?g{
?outm a gis:EuclDistance; wf:of ?in ; wf:of _:sf. 
_:sf a gis:SField. 
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:EuclideanDistanceTool;
wf:output ?out;
gis:inputdata ?in.
?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm.
}
#}
}
