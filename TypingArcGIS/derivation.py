#-------------------------------------------------------------------------------
# Name:        Derivation
# Purpose:     Implements the idea of a typed spatio-temporal derivation graph.
#
# Author:      Simon Scheider
#
# Created:     30-04-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from Typing import *

class inst:
    """This is the basic class of type instances"""
    def __init__(self, type=a(), name="inst"):
        self.type = type
        self.succ = {}
        self.link = ""
        self.col= "w"
        if (name == "inst"):
            self.id ="".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
        else:
            self.id = name
    def __str__(self):
        return self.id+"::"+str(self.type)

class oprtn(inst):
    def __init__(self, fun, inputl, output, name="inst"):
        if not isinstance(fun,Fun):
            raise ValueError('Operations need to be functions!')
        self.type = fun
        self.succ = {}
        self.link = ""
        self.col= "w"
        self.input= inputl #The list of input instances
        self.multi = False
        if isinstance(self.input,list):
            self.multi = True
        self.output = output#The output instance
        if (name == "inst"):
            self.id ="".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
        else:
            self.id = name

class dgraph:
    """This is actually a tree of operators, stored in a dictionary with inputs as key. Therefore, there is always a defined predecessor operation of an output and a root in the tree."""
    def __init__(self):
        self.indict = {}
        self.outdict = {}

    def add(self,operation):
        if isinstance(operation,oprtn):
            #print isinstance(self.outdict,set)
            #print len(self.outdict)
            if (operation.output not in self.outdict.keys()):
                self.outdict[operation.output]=operation
                if (operation.multi):
                    for i in operation.input:
                        self.indict[i] = operation
                else:
                    self.indict[operation.input] = operation
            else:
                raise ValueError('No output can be output of two operations!')

        else:
            raise ValueError('Only Operations can be added!')

    def getPred(self,inp):
        return self.indict.get(inp)

    def getRoot(self):
        k =list(self.indict.keys())
        ok = self.indict.get(k[0])
        root ={}
        default = "no"
        while (self.indict.get(ok.output,default)!="no"):
            root = ok.output
            ok =self.indict.get(ok.output)
        return ok

    def TypeUnifyGraph(self):
        self.DFSVisit(self.getRoot())

    def DFSVisit(self, n):
        n.col = "g"
        for v in self.getneighbours(n):
            if v[0].col == "w":
                v[0].succ = n
                v[0].link = v[1]
                self.DFSVisit(v[0])
        n.col = "b"
        print n.col
        n.type.unify()
        self.propagateType(n,n.link,n.succ)

    def propagateType(self,n,link,succ):
        if link == "in":
            succ.type.setIn=n.type
        elif link == "out":
            succ.type.setType = n.type.getOut


    def getneighbours(self,n):
        list = []
        if isinstance(n,oprtn):
            if n.multi:
                for i in n.input:
                    list.append([i,"in"])
            else:
                list.append([n.input,"in"])
        if self.outdict.get(n, "no")!="no":
            list.append([self.outdict[n],"out"])
        return list






#def main():
i = inst(S())
out = inst()
t = inst(T())
out2 = inst()
out3 = inst()
ai = a()
o = oprtn(Fun(ai,Fun(T(),ai)),[i,out3],out)
o2 = oprtn(Fun(a(),Fun(Q(),Q())),[t,out], out2)
o3 = oprtn(Fun(a(),a()), t,out3)
g = dgraph()
g.add(o)
g.add(o2)
g.add(o3)
print g.getneighbours(o2)
print str(g.getRoot())
g.TypeUnifyGraph()
    #print i
    #print o


#if __name__ == '__main__':
    #main()
