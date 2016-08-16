
# Propagate ends and starts to path
INSERT {
?path gis:hasStart ?sourceds.
?path gis:hasEnd ?sinkds.
} WHERE {
?path ^wf:of ?ex; a gis:Path.
?ex a gis:Existence.
?ds ada:hasElement ?ine. ?ine ada:hasMeasure ?ex.
?costpathoperation wf:output ?ds; gis:source ?source; gis:linkraster ?linkraster.
?costdistanceoperation wf:output ?linkraster; gis:sink ?sink.
?source ada:hasElement ?sourcee. ?sourcee ada:hasMeasure ?sourcem. ?sourcem a gis:Existence; wf:of ?sourceds.
?sink ada:hasElement ?sinke. ?sinke ada:hasMeasure ?sinkm. ?sinkm  a gis:Existence; wf:of ?sinkds.
}

#Test query:
#SELECT * 
#WHERE {graph ?g{
#?p a gis:Path;gis:hasStart ?s; gis:hasEnd ?e.
#FILTER(!isblank(?s))
#FILTER(!isblank(?e))
#}
#}