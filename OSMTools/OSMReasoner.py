#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simon
#
# Created:     24-04-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import rdflib
g=rdflib.Graph()
g.load('http://dbpedia.org/resource/Utrecht')

#for s,p,o in g:
 # print s,p,o

import RDFClosure as rdfc

gg = rdfc.DeductiveClosure(rdfc.RDFS_Semantics).expand(g)