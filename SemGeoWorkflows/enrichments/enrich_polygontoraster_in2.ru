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
?ine ada:hasSupport _:inr. _:inr a gis:Region.
?in2 a gis:RegionDataSet.
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
{
?node a gis:PolygontoRaster;
gis:inputdata ?in2.
?in2 ada:hasElement ?ine.
FILTER NOT EXISTS{?ine ada:hasSupport ?ins. ?ins a gis:Region. }#Are data blank nodes present? Then reuse them
}
#}
}






