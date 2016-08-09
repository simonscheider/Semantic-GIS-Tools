

# Typing gis:toLine
INSERT 
{ 
?in ada:hasElement _:ine. _:ine ada:hasMeasure _:inm. _:inm  a gis:Existence; wf:of _:object.
}
WHERE{
?node a gis:toLine;
gis:inputdata ?in.
FILTER NOT EXISTS {?in ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.
}
}

