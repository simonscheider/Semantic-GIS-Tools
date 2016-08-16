
# Typing gis:PointtoRaster
#Set inputs

#Set output
INSERT 
{ 
#GRAPH ?g{
?out a gis:Raster; ada:hasElement [ada:hasMeasure [a gis:Existence; wf:of ?in2; a gis:QQuality; gis:ofprop ?inm]].
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
?node a gis:PointtoRaster;
wf:output ?out;
gis:inputdata ?in2.
?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm. ?inm a ada:Quality. #Are data blank nodes present? Then reuse them
FILTER NOT EXISTS{?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm}
#}
}






