

# Typing gis:LocalMapAlgebra


#Set output links
INSERT
{ #GRAPH ?g{
?outm a gis:QQuality ; gis:ofprop ?inm .
?inm a gis:Quality.
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
?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm.
}
#}
}








