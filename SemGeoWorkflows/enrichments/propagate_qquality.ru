

#Propagates the provenance of properties (e.g. Fields) across local map algebra and conversions:
INSERT
{ 
#GRAPH ?g{
?b wf:of ?something
}
#}
#SELECT *
WHERE{
#GRAPH ?g{
?a wf:of ?something; (^gis:ofprop)+ ?b.
FILTER NOT EXISTS{?a gis:ofprop ?something}
}
#}

#Test:

#Select all datasets that are of (=represent) fields:
#Select ?ds 
#WHERE{
#GRAPH ?g{
#?ds  ada:hasElement ?ine. ?ine ada:hasMeasure ?b .
#?b wf:of ?somefield. 
#?somefield a gis:SField.
#}}

