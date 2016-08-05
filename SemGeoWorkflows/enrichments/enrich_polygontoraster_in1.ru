PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX  xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace>
PREFIX wf: <http://geographicknowledge.de/vocab/Workflow.rdf#>
PREFIX  gis: <http://geographicknowledge.de/vocab/GISConcepts.rdf#>
PREFIX  ada: <http://geographicknowledge.de/vocab/AnalysisData.rdf#>

# Typing gis:PolygontoRaster

#Set Input
INSERT 
{ 
#GRAPH ?g{ 
?in2 ada:hasElement _:ine. _:ine ada:hasMeasure _:inm. _:inm a gis:Quality.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PolygontoRaster;
gis:inputdata ?in2.
FILTER NOT EXISTS{?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm. ?inm a gis:Quality. }#Are data blank nodes present? Then reuse them
}
#}
}






