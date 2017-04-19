#-------------------------------------------------------------------------------
# Name:         uniformity level
# Purpose:      The function UniformityLevel() calculates a shannon entropy based
#               uniformity measure (max-standardized entropy) over a list of attributes
#               (given by ArcGIS fields), multiplied by the mean to account for
#               the level. Can be used to assess economic clusters when applied
#               to regions with location quotients of related economic sectors.
#               The measure is high for uniformly distributed attributes
#               with a high mean value, and 0 for highly specialized regions
#               (with a single nonzero value) or for regions with only 0 values.
#               Script can be used in ArcGIS FieldCalculator.
#
# Author:      Simon Scheider
#
# Created:     11/10/2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np


def remove_values_from_list(the_list, val):
        while val in the_list:
            the_list.remove(val)
def remove_values_from_list2(the_list, val):
        l = []
        for i in range(len(the_list)):
            if val !=the_list[i]:
                l.append(the_list[i])
        return l

#This function computes Shannon entropy for an array of float numbers (which do not need to add up to 1), where each number gets normalized by the sume of values
def entropyn(probs):
    #print probs
    probs = remove_values_from_list2(probs,0.0)
    #print probs
    if (not probs == []):
        normalized = ( (probs/np.sum(probs)))
        #print stand
        ent = - np.sum(normalized * np.log(normalized))
        return abs(ent)
    else:
        return 0

#This function standardizes entropy by the maximum entropy using array size
def standardize(n, size):
    max_entropy = np.log(size)
    return (n/max_entropy)

def simpsonIndex(p):
    p = p/np.sum(p)
    return np.sum(p*p)



#This function computes the product of standardized entropy and mean of an array (uniformity level)
def entropy_measure(p):
    size = len(p)
    #print "size: "+str(size)
    e = entropyn(p)
    #print e
    stand_ent = standardize(e,size)
    #print stand_ent
    if (not p == []):
         return stand_ent * np.mean(p)
    else:
         return 0

#Method used for calculating a new (ArcGIS) Field of uniformity values (can receive min 2 and up to 5 field names: !Fieldname1!, ...)
#Note: the ArcGIS field needs to be FLOAT and have precision 5 and scale (=decimal places) 3
def UniformityLevel(fst, snd, trd="", fourth="", fifth=""):
    d = [fst, snd, trd, fourth, fifth]
    remove_values_from_list(d,'')
    #print d
    #Result is a float with precision 5 and 3 decimal places
    return round(entropy_measure(d),3)



#print UniformityLevel(43.433931, 0.0, 0.0, 0.0,0.0)
#testarray
##d = [[15.0, 1.5, 1.5, 1.5, 1.5],
##    [1.5, 1.1,0.8, 0.3, 0.1],
## [0.0, 0.0, 0.0, 0.0,0.0],
## [5.0, 0.0, 0.0, 0.0,0.0],
## [5.0, 5.0, 0.0, 0.0,0.0],
## [5.0, 5.0, 5.0, 0.0,0.0],
## [5.0, 5.0, 5.0, 5.0, 0.0],
## [5.0, 5.0, 5.0, 5.0, 5.0],
## [0.0, 0.0, 17.946806, 8.351337]
## ]
##for i in d:
##    print simpsonIndex(i), standardize(entropyn(i),len(i))


 #Plot these examples
##import matplotlib as mp
##import matplotlib.pyplot as plt
##for i in d:
##    epsilon = 1e-7
##    i = [x+epsilon for x in i]
##    plt.bar(range(len(i)),i,color="blue")
##    plt.subplot(111).set_ylim(0, np.amax(i)*1.2 if np.amax(i)>2 else 2)
##    plt.show()
##
##for i in d:
##    print i
##    print "m: " +str(entropy_measure(i)),"stand_e: " +str(standardize(entropyn(i),len(i))),"e: " +str(entropyn(i)), "max_e: " +str(np.log(len(i))), "mean: " +str(np.mean(i))


