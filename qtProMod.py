#!/usr/bin/env python

'''
   Simple build script that modifies the qt project file for the correct library path. 
   Which will also rebuild the library code and the Qt application as well
'''

import os

PRO_FILENAME = "NextGenQt4"
PRO_EXT      = ".pro"
BAK_EXT      = ".bak"

LIB_VARIABLE = "LIBS +="
LIB_PARITAL_PATH = "/LVVC_Combi/OBJS_ForQT/*.o"

def modifyPRO():
   getCWD = os.getcwd()
   #print(getCWD)

   readPro = open(PRO_FILENAME + PRO_EXT, "r")
   writePro = open(PRO_FILENAME + BAK_EXT, "w")

   for lines in readPro:
      if lines.find(LIB_VARIABLE) == 0:
         #print (lines)
         newLibPath = getCWD + LIB_PARITAL_PATH
         writePro.write(LIB_VARIABLE + " " + newLibPath + "\n")
         print "Updated LIB path!"
      else:
         writePro.write(lines)

   readPro.close()
   writePro.close()

   os.rename(PRO_FILENAME + BAK_EXT, PRO_FILENAME + PRO_EXT)

   # Build the LVVC library
   os.chdir("LVVC_Combi/")
   os.system("make clean")
   os.system("make")
   # Build NextGenQt4
   os.chdir("..")
   os.system("qmake")
   os.system("make")
   
   h = "*" * 80
   print(h)
   print("NextGenQt4 is now configured correctly! Have A Nice Day")
   print(h)


modifyPRO()