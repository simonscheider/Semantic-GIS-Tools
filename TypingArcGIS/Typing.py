#-------------------------------------------------------------------------------
# Name:        Typing
# Purpose:     This is a Python module for spatio-temporal information typing.
#              It contains a type schema together with methods for type unification
#              and subtyping.
#
# Author:      Simon Scheider
#
# Created:     29-04-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
import random


class Type:
    """This is a basic type class (supertype of all types)"""
    def __init__(self, typeName="Type"):
        self.name=typeName
        self.setType =self
        """This attribute (potentially) contains another type that is to be unified with the current one"""
        self.default = {}
    def __str__(self):
        return self.name
        """A string representation of this type"""
    def subType(self,thing):
        """This method compares whether the current type is a subtype of another. Per default, this is based on the subclass relation (but for different subtypes, this method is overwritten)"""
        b = False
        if (isinstance(thing,a)):
            #Everything is a subtype of a type variable 'a
            b = True
        else:
            #Subtypes are simply subclasses of class types
            b = issubclass(self.__class__,thing.__class__)
        #print str(self)+" subtype of "+str(thing)+" ? :"+str(b)
        return b
    def unify(self):
        """This method tries to unify the current type with the type that is set in its attribute 'setType' and returns the most specific type. Just prints a message about failure or success."""
        variables ={}
        #print "hallo..."+str(self.setType.subType(self))+str(self.subType(self.setType))
        if self.subType(self.setType):
            return self
        elif self.setType.subType(self):
            #print "substitute "+str(self) + "with "+str(self.setType)
            if self.setType.getvariables(self,variables):
                print "substitute "+str(self) + " with "+str(self.setType)
                return self.setType
            else:
                print str(self.__class__.__name__)+" type unification of "+str(self)+" with "+str(self.setType)+" failed because of inconsistent variables"
                return self
        else:
            return self

    def getvariables(self, other, vdict):
        """Method to substitute type variables with types. This method associates type variables contained in the type 'other' (needs to be a supertype of self) with the current type and stores type substitutes as key (=type variable from other) value (=type substitute from self) pairs in the dictionary vdict.
        If the type variable is already existent in vdict and points to a different type, then a syntactic contradiction is raised and returned as boolean value (i.e. type variables need to be consistently substituted)."""
        r = True
        if (isinstance(other,a) ): # is a type variable
           if vdict.get(other,self.default)==self.default: #type variable not yet discovered
                vdict[other]=self
           else: #type variable already discovered
                r = isinstance(vdict.get(other),self.__class__) #is the substitute of the same type as the current type?
        return r

    def setvariables(self,vdict):
        """Type variable substitution with concrete types."""
        pass


class a(Type):
    """A type variable. This class is used to generate empty (variable) types, which can be substituted by any other type."""
    def __init__(self, typeName="'a"):
        self.name="'"+random.choice(string.letters).lower()
        self.setType =self
        self.default = {}



class Referent(Type):
    """The type of referents"""
    def __init__(self, typeName="Referent"):
        self.name=typeName
        self.setType =self
        self.default = {}


class S(Referent):
    """The type of spatial referents"""
    def __init__(self, typeName="S"):
        self.name=typeName
        self.setType =self
        self.default = {}

class T(Referent):
    """The type of temporal referents"""
    def __init__(self, typeName="T"):
        self.name=typeName
        self.setType =self
        self.default = {}

class Q(Referent):
    """The type of quality referents"""
    def __init__(self, typeName="Q"):
        self.name=typeName
        self.setType =self
        self.default = {}

class D(Referent):
    """The type of discrete object referents"""
    def __init__(self, typeName="D"):
        self.name=typeName
        self.setType =self
        self.default = {}

class Bool(Referent):
    """The type of true/false values"""
    def __init__(self, typeName="Bool"):
        self.name=typeName
        self.setType =self
        self.default = {}


class Tuple(Type):
    """The tuple type constructor. This type is used to build n-ary tuples by recursion."""
    def __init__(self, fst, snd, typeName="Tuple"):
        self.name=typeName
        self.setType =self
        self.fst = fst
        """The head of the tuple"""
        self.snd = snd
        """The tail of the tuple"""
        self.default = {}
    def __str__(self):
        strr = ""
        strr+="("
        strr+= str(self.fst)
        strr+="*"
        strr+= str(self.snd)
        strr+=")"
        return strr
    def subType(self,thing):
        """A recursive Tuple version of subtype comparison (passes comparison on to lower levels)"""
        if (isinstance(thing,Tuple)):
            b = (self.fst.subType(thing.fst) and self.snd.subType(thing.snd))
        else:
            b = False
        return b
    def getvariables(self, other, vdict):
        """A recursive Tuple version of type variable substitute check (passes on to lower levels in the type tree)"""
        r = True
        if (isinstance(other,a) ):
           if vdict.get(other,self.default)==self.default:
                vdict[other]=self
           else:
                r = isinstance(vdict.get(other),Tuple)
        else:
             r = self.fst.getvariables(other.fst,vdict) and self.snd.getvariables(other.snd,vdict)
        return r

    def setvariables(self,vdict):
        """A recursive Tuple version of type variable substitution (passes on to lower levels in the type tree). """
        if (vdict.get(self.fst,self.default)!=self.default):
            self.fst = vdict[self.fst]
        elif (vdict.get(self.snd,self.default)!=self.default):
            self.snd = vdict[self.snd]
        else: # passing on to lower levels in the type tree
            self.fst.setvariables(vdict)
            self.snd.setvariables(vdict)



class Sett(Type):
    """The set type constructor"""
    def __init__(self, settype, typeName="Set"):
        self.name=typeName
        self.setType =self
        self.of = settype
        """Of links to the type of the elements of the type of set (e.g. "T" in "T Set")"""
        self.default = {}
    def __str__(self):
        strr = ""
        strr+= str(self.of)
        strr+="Set"
        return strr
    def subType(self,thing):
        """A recursive Set version of subtype check (passes on to lower levels)"""
        if (isinstance(thing,a)):
            b = True
        elif (isinstance(thing,Sett)):
            b = (self.of.subType(thing.of))
        else:
            b = False
        return b
    def getvariables(self, other, vdict):
        """A recursive Set version of type variable substitute check (passes on to lower levels)"""
        r = True
        if (isinstance(other,a)):
            if vdict.get(other,self.default)==self.default:
                vdict[other]=self
            else:
                r = isinstance(vdict.get(other),Sett)
        else:
            r = self.of.getvariables(other.of,vdict)
        return r
    def setvariables(self,vdict):
        """A recursive Set version of type variable substitution (passes on to lower levels)"""
        if (vdict.get(self.of,self.default)!=self.default):
            self.of = vdict.get(self.of)
        else:
            self.of.setvariables(vdict)



class Fun(Type):
    """The function type constructor"""
    def __init__(self, input, output, typeName="Fun"):
        self.name=typeName
        self.setType =self
        self.getIn = input
        """This is the input type of the function type. Note that function types are always unary, as n-ary functions are recursively defined (with a corresponding function as output."""
        self.getOut = output
        """This is the output type of the function type"""
        self.setIn = input
        self.default = {}
    def __str__(self):
        if  (isinstance(self.getIn,Fun)):
            ins = "("+str(self.getIn)+")"
        else:
            ins = str(self.getIn)
        strr = ""
        strr+= ins
        strr+= "=:"#This is supposed to be the function arrow (u"\u2192").encode("utf-8")
        strr+= str(self.getOut)
        return strr
    def subType(self,thing):
        if (isinstance(thing,a)):
            b = True
        elif (isinstance(thing,Fun)):#Are inputs and outputs subtypes of each other?
            b = (self.getIn.subType(thing.getIn) and self.getOut.subType(thing.getOut))
        else:
            b = False
        return b
    def unify(self):
        """A Fun version of type unification. It first tries to unify the function type with a set input ("setIn"). Then it tries to unify the function with a preset type (setType)"""
        variables = {}
        #This unifies the function type with an intended input
        if self.setIn.subType(self.getIn) and self.setIn.getvariables(self.getIn,variables):
            #print str(variables)
            print "substitute "+str(self.getIn) + " with "+str(self.setIn)
            self.setvariables(variables)
        elif (not self.getIn.subType(self.setIn)):
             print "function type unification of "+str(self)+" with input "+str(self.setIn)+" failed because of inconsistent variables"

        variables = {}
         #This unifies the function type as a whole with what is set in setType
        if self.subType(self.setType):
            return self
        elif self.setType.subType(self):
            if self.setType.getvariables(self,variables):
                print "substitute "+str(self) + " with "+str(self.setType)
                return self.setType
            else:
                print "function type unification of "+str(self)+" with "+str(self.setType)+" failed because of inconsistent variables"
                return self
        else:
            print "function type unification of "+str(self)+" with "+str(self.setType)+" failed because of incompatible types"
            return self
    def getvariables(self, other, vdict):
        """A recursive Fun version of type variable substitute check (passes on to lower levels)"""
        r = True
        if (isinstance(other,a)):
            if vdict.get(other,self.default)==self.default:
                vdict[other]=self
            else:
                r = isinstance(vdict.get(other),Fun)
        else:
            r = self.getIn.getvariables(other.getIn,vdict) and self.getOut.getvariables(other.getOut,vdict)
        return r
    def setvariables(self,vdict):
        """A recursive Fun version of type variable substitution (passes on to lower levels)"""
        if (vdict.get(self.getIn,self.default)!=self.default):
            self.getIn = vdict[self.getIn]
        else:
            self.getIn.setvariables(vdict)
        if (vdict.get(self.getOut,self.default)!=self.default):
            self.getOut = vdict[self.getOut]
        else:
            self.getOut.setvariables(vdict)



if __name__ == '__main__':
    test()

def test():
    #Testing the type schema
    field = Fun(Tuple(T(),S()),Q())
    pointset = Sett(Tuple(S(),Tuple(T(),Q())))
    ai = a("ae")
    abstractpointset = Sett(Tuple(a(),Tuple(a(),a())))
    abstractpointset2 = Sett(Tuple(ai,Tuple(ai,ai)))

    field2 = Fun(S(),Fun(T(),Q()))
    abstractfunction = Fun(a(),Fun(a(),a()))

    abstractfunction2 = Fun(ai,Fun(ai,ai))

    pointset2 = Sett(Tuple(Referent(),Tuple(Referent(),Referent())))

    function = Fun(S(),Fun(ai,ai))


    #printing
    print field
    print field2
    print pointset
    print pointset2
    print abstractfunction
    print abstractfunction2
    print abstractpointset
    print abstractpointset2

    #Testing for subtypes
    print field.subType(field)
    print field.subType(abstractfunction)
    print field2.subType(abstractfunction)
    #print field2.subType(abstractfunction2)

    #Testing type unification
    pointset2.setType=pointset
    abstractpointset.setType = pointset
    abstractpointset2.setType = pointset
    field2.setType = abstractfunction
    #This test fails, why?
    abstractfunction.setType = field2
    abstractfunction2.setType = field2
    #abstractfunction2.setIn =pointset
    function.setIn = Q()
    print "unify:" +str(field2.unify())
    print "unify:" +str(abstractfunction)+":" +str(abstractfunction.unify())
    print "unify: "+str(pointset2)+":" +str(pointset2.unify())
    print "unify: "+str(abstractfunction2)+":" +str(abstractfunction2.unify())
    print "unify: "+str(abstractpointset)+":" +str(abstractpointset.unify())
    print "unify: "+str(abstractpointset2)+":" +str(abstractpointset2.unify())
    print "unify: "+str(function)+":" +str(function.unify())


