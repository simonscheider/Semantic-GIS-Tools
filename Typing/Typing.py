#-------------------------------------------------------------------------------
# Name:        Typing
# Purpose:     This is a Python module for spatio-temporal information typing
#
# Author:      simon
#
# Created:     29-04-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


class Type:
    """This is a basic type object class"""
    def __init__(self, typeName="Type"):
        self.name=typeName
        self.type =self
    def __str__(self):
        return self.name
    def subType(self,thing):
        if (isinstance(thing,a)):
            b = True
        else:
            b = issubclass(self.__class__,thing.__class__)
        #print str(self)+" subtype of "+str(thing)+" ? :"+str(b)
        return b
    def getsubType(self,thing):
        if (isinstance(thing,a)):
            b = self
        elif issubclass(self.__class__,thing.__class__):
            b = self
        elif issubclass(thing.__class__,self.__class__):
            b = thing
        else:
            b = self
        return b
    def unify(self):
        if self.subType(self.type):
            return self
        elif self.type.subType(self):
            return self.type
        else:
            return self


class a(Type):
    def __init__(self, typeName="'a"):
        self.name=typeName
        self.type =self



class Referent(Type):
    def __init__(self, typeName="Referent"):
        self.name=typeName
        self.type =self


class S(Referent):
    def __init__(self, typeName="S"):
        self.name=typeName
        self.type =self

class T(Referent):
    def __init__(self, typeName="T"):
        self.name=typeName
        self.type =self

class Q(Referent):
    def __init__(self, typeName="Q"):
        self.name=typeName
        self.type =self

class D(Referent):
    def __init__(self, typeName="D"):
        self.name=typeName
        self.type =self

class Bool(Referent):
    def __init__(self, typeName="Bool"):
        self.name=typeName
        self.type =self


class Tuple(Type):
    def __init__(self, fst, snd, typeName="Tuple"):
        self.name=typeName
        self.type =self
        self.fst = fst
        self.snd = snd
    def __str__(self):
        strr = ""
        strr+="("
        strr+= str(self.fst)
        strr+="*"
        strr+= str(self.snd)
        strr+=")"
        return strr
    def subType(self,thing):
        if (isinstance(thing,Tuple)):
            b = (self.fst.subType(thing.fst) and self.snd.subType(thing.snd))
        else:
            b = False
        return b


class Set(Type):
    def __init__(self, settype, typeName="Set"):
        self.name=typeName
        self.type =self
        self.of = settype
    def __str__(self):
        strr = ""
        strr+= str(self.of)
        strr+="Set"
        return strr
    def subType(self,thing):
        if (isinstance(thing,Set)):
            b = (self.of.subType(thing.of))
        else:
            b = False
        return b

class Fun(Type):
    def __init__(self, input, output, typeName="Fun"):
        self.name=typeName
        self.type =self
        self.getIn = input
        self.getOut = output
        self.setIn = input
        self.setOut = input
    def __str__(self):
         strr = ""
         strr+= str(self.getIn)
         strr+= "=:"#(u"\u2192").encode("utf-8")
         strr+= str(self.getOut)
         return strr
    def subType(self,thing):
        if (isinstance(thing,Fun)):
            b = (self.getIn.subType(thing.getIn) and self.getOut.subType(thing.getOut))
        else:
            b = False
        return b
    def setsubType(self,thing):
        #if (isinstance(thing,Fun)):
        self.getIn.setsubType(thing.getIn)
        self.getOut.setsubType(thing.getOut)

    def unify(self):
        if self.setIn.subType(self.getIn):
            self.getIn =self.setIn
        if self.subType(self.type):
            return self
        elif self.type.subType(self):
            return self.type
        else:
            return self


#test types

field = Fun(Tuple(T(),S()),Q())
pointset = Set(Tuple(S(),Tuple(T(),Q())))

field2 = Fun(S(),Fun(T(),Q()))
abstractfunction = Fun(a(),Fun(a(),a()))
ai = a("ae")
abstractfunction2 = Fun(ai,Fun(ai,a()))

pointset2 = Set(Tuple(Referent(),Tuple(Referent(),Referent())))


#printing
print field
print field2
print pointset
print pointset2
print abstractfunction
print abstractfunction2

#Testing for subtypes
print field.subType(field)
print field.subType(abstractfunction)
print field2.subType(abstractfunction)

pointset2.type=pointset
field2.type = abstractfunction
abstractfunction.type = field2
print "unify:" +str(field2.unify())
print "unify:" +str(abstractfunction.unify())
print "unify"+str(pointset2)+":" +str(pointset2.unify())