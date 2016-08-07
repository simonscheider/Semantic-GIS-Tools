

# Propagate ends and starts to path

#Test query:
ASK {
?p a gis:Path;gis:hasStart ?s; gis:hasEnd ?e.
FILTER(!isblank(?s))
FILTER(!isblank(?e))
}
#}