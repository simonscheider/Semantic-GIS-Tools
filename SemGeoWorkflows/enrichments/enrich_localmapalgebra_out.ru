

# Typing gis:LocalMapAlgebra


#Set output
INSERT
{ #GRAPH ?g{
?out a gis:Raster; ada:hasElement [ ada:hasMeasure [ a gis:QQuality ; gis:ofprop ?inm ]].
?in2 a gis:Raster.  ?inm a gis:Quality. # This reuses data blank nodes if present
#}
}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:LocalMapAlgebra;
wf:output ?out;
gis:inputdata ?in2.
?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm. #Are data blank nodes present? Then reuse them
}
#}
}








