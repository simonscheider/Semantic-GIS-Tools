

#Propagates the provenance of properties (e.g. Fields) across local map algebra and conversions:


#Test:

#Select all datasets that are of (=represent) fields:
ASK{
?ds  ada:hasElement ?ine. ?ine ada:hasMeasure ?b .
?b wf:of ?somefield. 
?somefield a gis:SField.
}
