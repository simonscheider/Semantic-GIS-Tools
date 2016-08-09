

# Typing gis:toLine
INSERT 
{ 
#GRAPH ?g{
?out ada:hasElement _:oute. _:oute ada:hasMeasure _:line. _:line a gis:Line
}
WHERE{
?node a gis:toLine;
wf:output ?out.
FILTER NOT EXISTS {?out ada:hasElement ?oute. ?oute ada:hasMeasure ?outm. ?outm a gis:Line.
} 
}

