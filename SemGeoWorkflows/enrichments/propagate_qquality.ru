
#Propagates the provenance of properties (e.g. Fields) across local map algebra and conversions:
INSERT { 
?b wf:of ?something
} WHERE {
?a wf:of ?something; (^gis:ofprop | owl:sameAs)+ ?b.
#?a wf:of ?something; (^gis:ofprop)+ ?b.
}

#Test:

#Select all datasets that are of (=represent) fields:
#Select ?ds 
#WHERE{
#GRAPH ?g{
#?ds  ada:hasElement ?ine. ?ine ada:hasMeasure ?b .
#?b wf:of ?somefield. 
#?somefield a gis:SField.
#}}

