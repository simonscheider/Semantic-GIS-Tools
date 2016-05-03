#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simon
#
# Created:     11-03-2016
# Copyright:   (c) simon 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import mypy
import module1
mypy = "C:\Users\simon\AppData\Local\Programs\Python\Python35-32\Scripts\mypy"
program = "C:\Users\simon\Documents\GitHub\ArcGIS-Tools\module1.py"

#os.system("python "+mypy+ " "+program)

mypy.main(module1)

