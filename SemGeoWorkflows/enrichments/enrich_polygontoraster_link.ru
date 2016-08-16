

# Typing gis:PolygontoRaster

#Set output
INSERT 
{ 
#GRAPH ?g{
?out a gis:Raster. ?outm a gis:Existence; wf:of ?in; a gis:QQuality; gis:ofprop ?inm. 
?outs ada:partof ?ins.
?inm wf:of _:gf. # This reuses data blank nodes if present
?inm a ada:Quality.
_:gf a gis:SField.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PolygontoRaster;
		wf:output ?out;
gis:inputdata ?in2.
?in2 ada:hasElement ?ine. 
?ine ada:hasMeasure ?inm. #Are data blank nodes present? Then reuse them
?ine ada:hasSupport ?ins.
?out ada:hasElement ?oute. 
?oute ada:hasMeasure ?outm.
?oute ada:hasSupport ?outs.
}
#}
}





