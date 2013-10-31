#!/usr/bin/env python

'''
   Find SD card and try and format it using fdisk
   Usage:
     1. Plug in SD card. 
     2. Run: sudo python2 formatSD.py 
'''

import os
import subprocess

def findSD():

   try:
      os.remove("dmesgOutput")
      os.remove("sdINFO")
      os.remove("fdiskLOG")
   except:
      pass

   # Find ze SD card
   #os.system("blkid" >> dmesgOutput")
	
   #using subprocess
   dmesgOutput = subprocess.check_output("blkid")
   devs = dmesgOutput.split("\n")
   del devs[-1]
   i = 0

   print("Available Disks:")
   while i < len(devs):
      tmp = devs[i]
      devs[i] = tmp[0:8]
      i+=1

   devs = list(set(devs))
   print("Which device is your SD card? (careful)")
   for idx, dev in enumerate(devs):
      print(str(idx+1) + ". " + dev)
         
   num = raw_input()
   if num.isdigit():
      device = devs[int(num)-1]
   else:
      return

   device = device[0:8]
   sectorSize = subprocess.check_output(["blockdev","--getsize",device]) 
   print("device info read for device: "+device+".")
   createPartion(int(sectorSize), device)
   pass

def createPartion(size, deviceName):

   fixed = int(size) / 4
   # This may be ugly...
   FIRST_PARTITION =    "( echo o; echo n; echo p; echo 1; echo; " + "echo " + str(fixed) + ";" + "echo t; echo b;"
   SECOND_PARTITION =   " echo n; echo p; echo 2;" + "echo " + str(fixed + 1) + ";" + "echo " + str(fixed * 2) + ";"
   THIRD_PARTITION =    " echo n; echo p; echo 3;" + "echo " + str(fixed * 2 + 1) + ";" + "echo " + str(fixed * 3) + ";"
   FOURTH_PARTITION =   " echo n; echo p;" + "echo " + str(fixed * 3 + 1) + ";" + "echo " + str(int(size) - 1) + ";" + "echo w;)"
   os.system( ( FIRST_PARTITION + SECOND_PARTITION + THIRD_PARTITION + FOURTH_PARTITION) + " | fdisk " + deviceName )

   os.system( "mkfs.vfat " + deviceName + "1")
   os.system( "mkfs.ext4 " + deviceName + "2")
   os.system( "mkfs.ext4 " + deviceName + "3")
   os.system( "mkfs.ext4 " + deviceName + "4")

   pass


findSD()
