PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX  xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace>
PREFIX wf: <http://geographicknowledge.de/vocab/Workflow.rdf#>
PREFIX  gis: <http://geographicknowledge.de/vocab/GISConcepts.rdf#>
PREFIX  ada: <http://geographicknowledge.de/vocab/AnalysisData.rdf#>

# Typing gis:PolygontoRaster

#Set output
INSERT 
{ 
#GRAPH ?g{
?out a gis:Raster; ada:hasElement [ada:hasMeasure [a gis:Existence; wf:of ?in; a gis:QQuality; gis:ofprop ?inm]]. 
?inm wf:of _:gf. # This reuses data blank nodes if present
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
?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm. ?inm a gis:Quality. #Are data blank nodes present? Then reuse them
}
#}
}





