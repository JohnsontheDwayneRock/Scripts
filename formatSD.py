#!/usr/bin/env python

'''
   Find SD card and try and format it using fdisk
   
'''

import os

def findSD():

   try:
      os.remove("dmesgOutput")
      os.remove("sdINFO")
      os.remove("fdiskLOG")
   except:
      pass

   # Find ze SD card
   os.system("dmesg | tail >> dmesgOutput")

   dmesgRead = open("dmesgOutput", "r")

   possibleSDName = ""

   for lines in dmesgRead:
      if lines.find("sd") > 0:
         grabSD = lines.find("sd")
         infoSD = lines[grabSD:]
         grabLBraket = infoSD.find("[")
         grabRBraket = infoSD.find("]")
         possibleSDName = infoSD[grabLBraket + 1:grabRBraket]
         #print(possibleSDName)
         print ("Found an SD card!")
         break

   deviceName = "/dev/" + possibleSDName
   print ( deviceName )


   varIn = raw_input("Continue with formatting? (y/n): ")
   if varIn.lower() == "y":
      pass
   elif varIn.lower() == "n":
      return
   else:
      print("U BAD")
      return

   dmesgRead.close()

   #Get sd info so we can properly partition...
   #sdInfo = "echo p"
   os.system(("echo p") + "| fdisk " + "/dev/" + possibleSDName + " >> sdINFO")

   sdInfoRead = open("sdINFO", "r")

   for lines in sdInfoRead:
      info = "total"
      #print info
      if lines.find(info) > 0:
         #deviceLoc = lines.find(possibleSDName)
         #sizeInfo = lines[deviceLoc + 4:].split(',')
         sectorSize = lines.split()
	 print(sectorSize);
         createPartion(sectorSize[7], possibleSDName)
         break


   sdInfoRead.close()
   pass

def createPartion(size, deviceName):

   fixed = int(size) / 4
   # This may be ugly...
   FIRST_PARTITION =    "( echo o; echo n; echo p; echo 1; echo; " + "echo " + str(fixed) + ";" + "echo t; echo b;"
   SECOND_PARTITION =   " echo n; echo p; echo 2;" + "echo " + str(fixed + 1) + ";" + "echo " + str(fixed * 2) + ";"
   THIRD_PARTITION =    " echo n; echo p; echo 3;" + "echo " + str(fixed * 2 + 1) + ";" + "echo " + str(fixed * 3) + ";"
   FOURTH_PARTITION =   " echo n; echo p;" + "echo " + str(fixed * 3 + 1) + ";" + "echo " + str(int(size) - 1) + ";" + "echo w;)"
   os.system( ( FIRST_PARTITION + SECOND_PARTITION + THIRD_PARTITION + FOURTH_PARTITION) + " | fdisk " + "/dev/" + deviceName )

   os.system( "mkfs.vfat /dev/" + deviceName + "1")
   os.system( "mkfs.ext4 /dev/" + deviceName + "2")
   os.system( "mkfs.ext4 /dev/" + deviceName + "3")
   os.system( "mkfs.ext4 /dev/" + deviceName + "4")

   pass


#findSD()
createPartion(15523840,"sdb")
