
# if a region is part of a region of an object, that is part of region of that object

INSERT { 
	?a ada:partOf ?b.
} WHERE {
	?a ada:partOf+ ?b.
	FILTER NOT EXISTS{
		?a ada:partOf ?b
	}
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

