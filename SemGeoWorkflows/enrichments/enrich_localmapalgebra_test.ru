#Quicktest


ASK {
#GRAPH ?g {
#?a rdf:type foaf:Agent.
#<http://geographicknowledge.de/workflowLCP.rdf#3> ?b ?c
?op a gis:LocalMapAlgebra;
gis:inputdata ?in2;
wf:output ?out.
?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.
?out a gis:Raster; ada:hasElement ?oute. ?oute ada:hasMeasure ?outm .?outm a gis:QQuality ; gis:ofprop ?inm.
#}
}