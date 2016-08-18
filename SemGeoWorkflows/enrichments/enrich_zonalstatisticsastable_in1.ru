PREFIX : <http://geographicknowledge.de/WorkflowExamples#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace>
PREFIX wf: <http://geographicknowledge.de/vocab/Workflow.rdf#>
PREFIX gis: <http://geographicknowledge.de/vocab/GISConcepts.rdf#>
PREFIX ada: <http://geographicknowledge.de/vocab/AnalysisData.rdf#>
# Typing gis:ZonalStatisticsAsTable

#Set input
INSERT {
	?in a gis:Raster.
		?ine ada:hasMeasure _:inm.		
	?zo a gis:SpatialDataSet. #a gis:ObjectDataSet; This is too restrictive I think
		?zoe ada:hasMeasure _:zom.
} WHERE {
	?node a gis:ZonalStatisticsAsTable;
		gis:inputraster ?in;
		gis:zones ?zo.
		?in ada:hasElement ?ine.
		?zo ada:hasElement ?zoe.
	FILTER NOT EXISTS {		
		?ine ada:hasMeasure ?inm.		
		?zoe ada:hasMeasure ?zom.
	}
}
