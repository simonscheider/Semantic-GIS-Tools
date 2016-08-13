#!/usr/bin/env python

"""
Tests of Semantic Workflows.

The script
1) loads RDF files in memory
2) runs semantic enrichments
3) runs tests
4) writes the final graph into a Turtle file.

The code is written in Python 2.7 and depends on:

* RDFLib (# pip install rdflib)
* RDFClosure (install manually from https://github.com/RDFLib/OWL-RL)

"""

__author__      = "Andrea Ballatore; Simon Scheider"
__copyright__   = ""

import os
import re
import sys
from sys import argv
import rdflib
import RDFClosure
from rdflib.namespace import RDFS, RDF
import glob
from sets import Set

class tools():
    toolenrichments = []
    tests =[]
    def __str__(self):
        return str(toolenrichments)

def file_to_str(fn):
    """
    Loads the content of a text file into a string
    @return a string
    """
    with open(fn, 'r') as f:
        content=f.read()
    return content

def n_triples( g, n=None ):
    """ Prints the number of triples in graph g """
    if n is None:
        print( 'Triples: '+str(len(g)) )
    else:
        print( 'Triples: +'+str(len(g)-n) )
    return len(g)

def run_inferences( g ):
    print('run_inferences')
    # expand deductive closure
    #RDFClosure.DeductiveClosure(RDFClosure.RDFS_Semantics).expand(g)
    RDFClosure.DeductiveClosure(RDFClosure.OWLRL_Semantics).expand(g)
    n_triples(g)
    return g

def load_ontologies( g ):
    print("load_ontologies")
    ontos = ["ontologies/Workflow.rdf","ontologies/GISConcepts.rdf","ontologies/AnalysisData.rdf"]
    for fn in ontos:
        print("  Load RDF file: "+fn)
        g.parse( fn )
    n_triples(g)
    return g

def enrich_workflow_tool( g, toolname, tool):
    """
    @param g RDF graph
    @param toolname name of GIS tool
    @param tool TODO?
    """
    n = n_triples(g)
    assert toolname
    assert g
    import glob
    inputs = glob.glob('enrichments/enrich_'+toolname+'_in*.ru')
    outputs = glob.glob('enrichments/enrich_'+toolname+'_out*.ru')
    links = glob.glob('enrichments/enrich_'+toolname+'_link*.ru')
    tests =glob.glob('enrichments/enrich_'+toolname+'_test*.ru')
    growin = 0
    growout = 0
    for fn in (inputs):
        print('Enrichment '+fn)
        g.update( file_to_str('rdf_prefixes.txt') + file_to_str(fn) )
        growin +=len(g)-n
        n= n_triples(g)
    for fn in (outputs):
        print('Enrichment '+fn)
        g.update( file_to_str('rdf_prefixes.txt') + file_to_str(fn) )
        growout =len(g)-n
        n = n_triples(g)
    for fn in (links):
        print('Enrichment '+fn)
        g.update( file_to_str('rdf_prefixes.txt') + file_to_str(fn) )
        growout =len(g)-n
        n = n_triples(g)
    test = None
    for i in tests:
        print('Run test '+i)
        res = g.query(file_to_str('rdf_prefixes.txt') + file_to_str(i))
        test = bool(res)
        #assert b
        print(bool(res))
    tools.toolenrichments.append([str(tool), toolname, growin, growout, test])
    return g

def enrich_workflow( g, propagation ):
    """
    @param g
    @param propagation name of propagation
    """
    n = n_triples(g)
    assert propagation
    props = glob.glob('enrichments/propagate_'+propagation+'.ru')
    tests = glob.glob('enrichments/propagate_'+propagation+'_test.ru')
    for fn in (props):
        print('propagation '+fn)
        g.update( file_to_str('rdf_prefixes.txt') + file_to_str(fn) )
        n_triples(g)
    for i in tests:
        print('Run propagation test '+i)
        res = g.query(file_to_str('rdf_prefixes.txt') + file_to_str(i))
        #assert b
        print(bool(res))
    return g

def test_workflow_lights( g ):
    """ Runs enrichments and tests for China night lights example workflow """
    print('> test_workflow_lights')

    wfname = 'http://geographicknowledge.de/WorkflowExamples#wf2'

    _dir = "workflows/workflow_lights/"
    for fn in [_dir+"workflow_lights.ttl"]:
        print("Load N3 file: "+fn)
        g.parse( fn, format='n3' )
        g = reifyWorkflow(fn, wfname) + g
    g = run_inferences( g )
    g = enrich_with_backtracking( g, wfname )
    
    #sys.exit(0) # DEBUG
    return g # DEBUG
    
    # DEBUG
    # run query
    #SELECT *
    q = '''
    
    CONSTRUCT { 
    ?in2 ada:hasElement _:ine. 
    _:ine ada:hasMeasure _:inm.
    _:inm a gis:Quality. 
    # This reuses data blank nodes if present
} WHERE{
    ?node a gis:Erase;
            gis:inputdata ?in2.
    FILTER NOT EXISTS {?in2 ada:hasElement ?ine. ?ine ada:hasMeasure ?inm.} 
    #Are data blank nodes present? Then reuse them
}

    
    '''
    print('\nQUERY')
    q = file_to_str('rdf_prefixes.txt') + q
    print(q)
    for r in g.query(q):
        print(r)
    
    sys.exit(0) # DEBUG
    
    return g

def checkTool(operation):
    """
    Checks whether enrichment rules are available for operation class
    @param operation a GIS operation
    """
    #The list of tools to be used for tool enrichment
    lcptools = [ 'euclideandistancetool', 'polygontoraster','localmapalgebra','pointtoraster','costdistance','costpath','toline']
    lightstools = ['erase']
    operation = (((str(operation)).rpartition('#'))[2]).lower() #this extracts the toolname from its URI
    if operation in lcptools or operation in lightstools:
        return operation
    else:
        return None

def reifyWorkflow(file, wfname):
    """
    Adds reifications necessary to make workflow wfname searchable
    @param file source file for workflow
    @param wfname URI that identifies workflow
     """
    edge = rdflib.URIRef('http://geographicknowledge.de/vocab/Workflow.rdf#edge')
    subject = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#subject')
    predicate = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate')
    object = rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#object')
    wf = rdflib.Graph()
    wfuri = rdflib.URIRef(wfname)
    wf.parse(file, format='n3')
    for s,p,o in wf:
        if(s!= wfuri):
            e = rdflib.BNode()
            wf.add((wfuri, edge, e))
            wf.add((e, subject, s))
            wf.add((e, predicate, p))
            wf.add((e, object, o))
    n_triples(wf)
    return wf

def enrich_with_backtracking( g, wfname ):
    """
    Run tool enrichments in the order of DFS backtracking through workflow graph
    """
    wg = getWorkflowGraph(g,wfname)
    wg = load_ontologies(wg)
    wg = run_inferences(wg)
    root = getRoot(wg)
    visited = Set([])
    # Run tool enrichments in the order of DFS backtracking through workflow graph
    print("Search through workflow and enrich!")
    DFSVisit(root, wg, visited, g)
    return g

def test_workflow_lcpath( g ):
    """
    Runs enrichments and tests for Least Cost Path example workflow
    """
    print('> test_workflow_lights')
    wfname = 'http://geographicknowledge.de/workflowLCP.rdf#lcpwf'
    _dir = "workflows/workflow_lcpath/"
    for fn in [_dir+"workflow_lcpath.ttl"]:
        print("Load N3 file: "+fn)
        g = reifyWorkflow(fn, wfname) + g
    g = run_inferences( g )
    g = enrich_with_backtracking(g, wfname)
    #Propagations are run in any order
    #list of propagations
    lcppropagations = ['qquality','path']
    for i in lcppropagations:
        g = enrich_workflow( g, i )
    g = run_inferences( g )
    return g

def graph_to_file( g, output_filepath = None ):
    """ Serializes graph g to an XML/RDF file """
    if not output_filepath:
        _outfn = 'output/workflows_output.rdf'
    else: _outfn = output_filepath
    g.serialize( _outfn )
    print("Written triples to " + _outfn)

#Methods for workflow DFS search
def getWorkflowGraph(g, wfname):
    """Extracts a separate workflow graph of a given (named) workflow"""
    print("extract workflow graph (for DFS): "+wfname)
    q = """ \n CONSTRUCT {?subject ?predicate ?object.}
       WHERE {
            ?wfname wf:edge ?edge.
            ?edge rdf:subject ?subject.
            ?edge rdf:predicate ?predicate.
            ?edge rdf:object ?object.
          FILTER (?wfname = <"""+wfname+""">)
       }"""
    q = file_to_str('rdf_prefixes.txt') + q
    #print q
    gwf = rdflib.Graph()
    qres = g.query(q)
    for i in qres:
        gwf.add(i)
    n_triples(gwf)
    return gwf


def getRoot(wg):
    """Gets the root in a (single) workflow graph"""
    start = ''
    output = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#output")
    for s,p,o in (wg.triples((None, output, None))):
        start = s
        break
    objects = getNeighbours(wg,start)
    while (len(objects)>0):
        start = objects[0]
        objects = getNeighbours(wg,start)
    print('Root: '+ start)
    return start

def DFSVisit(n, wg, visited, g):
    """
    Searches through workflow graph (wg) starting from n and enriches operation nodes
    in entire graph g in the order of backtracking
    """
    # colors this node in grey
    visited.add(n)
    #print ('Just visited: '+str(n))
    for v in getNeighbours(wg, n, forward=False):
        if (v not in visited):
            DFSVisit(v, wg, visited, g)
    #print ('Just Colored Black: '+str(n))
    #Now backtracking starts
    operation = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#Operation")
    #get the operation types of the current node, check available enrichments for them, then enrich
    if (n, RDF.type, operation) in wg:
        print('  DFS candidate op: '+n)
        for i in (wg.objects(subject=n, predicate=RDF.type)):
            op = checkTool(i)
            if (i != operation and op is not None):
                print('DFS op found: '+op)
                enrich_workflow_tool( g, op, n)

def getNeighbours(wg, n, forward=True):
    """Gets neighbors of nodes in a workflow graph, either forward (in the direction of the output(root)) or backward (in the direction of inputs)"""
    objects = []
    output = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#output")
    input = rdflib.URIRef("http://geographicknowledge.de/vocab/Workflow.rdf#input")
    if forward:
        for i in (wg.objects(subject=n, predicate=output)):
                objects.append(i)
        for i in (wg.subjects(predicate=input,object=n)):
                objects.append(i)
    else:
        for i in (wg.subjects(predicate=output,object=n)):
                objects.append(i)
        for i in (wg.objects(subject=n,predicate=input)):
                objects.append(i)
    return objects

def runCompetencyQueries(g):
    """Questions are posed in terms of SELECT queries, and results are written to standard output in a readable tabular format"""
    tests = glob.glob('output/competencyquestion*.rq')
    for i in tests:
        print('Run competency question '+i)
        str = (file_to_str(i))
        print str
        res = g.query(file_to_str('rdf_prefixes.txt') +'\n'+ file_to_str(i))
        #print len(res)
        for i in res:
            line = ''
            for j in i:
                line += ((prefixURI(j)) if (j!=None) else 'None')+' '
            print line

def prefixURI(str):
    """Prefixes URI strings"""
    pref = {}
    namere = r"\s[a-z]+:"
    urire = r":\s+<\S+>"
    pre = file_to_str('rdf_prefixes.txt')
    for l in pre.split('\n'):
        uri= ''
        ns = ''
        for m in re.findall(urire,l):
            uri = m[3:-1]
            break
        for m in re.findall(namere,l):
            ns = m[1:]
            break
        pref[uri] = ns
    #print pref.keys()
    for k in pref.keys():
        str = str.replace(k, pref[k])
        #print str
    return str

def main():
    # create inmemory store
    g = rdflib.ConjunctiveGraph()
    params = sys.argv[1:]

    g = load_ontologies( g )
    if 'lights' in params: g = test_workflow_lights( g )
    if 'lcpath' in params: g = test_workflow_lcpath( g )
    graph_to_file(g)

    print('Tool enrichments and tests:')
    print ("Final size: "+str(len(g)))

    order = ''
    print("Order of tool enrichments: ")
    for j in tools.toolenrichments:
        order += ' :'+((((str(j[0])).rpartition('#'))[2]).lower())+' '
    print(order)
    print("Tool Toolname input output Test: ")
    for i in sorted(tools.toolenrichments, key=lambda wf: wf[0]) :
        print i[0], i[1], i[2], i[3], i[4]
    
    #runCompetencyQueries(g)
    
    print('OK') # end of script

if __name__ == '__main__':
    main()
