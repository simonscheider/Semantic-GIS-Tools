
# Typing gis:ExtractByMask

INSERT { 
	?outm gis:ofprop ?inm.
	?outs owl:sameAs ?ins. 	# outcell = raster cell
	 ?outs owl:sameAs ?ms . 	# outcell = mask cell
} WHERE {
	?node a gis:ExtractByMask;
		wf:output ?out;
		gis:inputraster ?ras;
		gis:rastermask ?mask.
	
	?ras ada:hasElement ?ine. 
	?ine ada:hasMeasure ?inm.
	?ine ada:hasSupport ?ins.
	
	?mask ada:hasElement ?me. 
	?me ada:hasMeasure ?mm.
	?me ada:hasSupport ?ms.
	
	?out ada:hasElement ?oute. 
	?oute ada:hasMeasure ?outm.
	?oute ada:hasSupport ?outs.
}
