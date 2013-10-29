#!/usr/bin/python

recipeNameList = []
timeDataList = []
tempDataList = []
steamTypeDataList = []
steamPercentDataList = []
fanSpeedDataList = []
fanReverseDataList = []
fanReverseTimeDataList = []
ventDataList = []



coreProbePullTemp = "{1500,1500,1500,1500,1500,1500,1500,1500,1500,1500}"
coreProbeCookAndHold = []
coreProbeCook = []
fanDelayTime = []
ventDelayTime = []
timeMode = []



DEFAULT = ['0,','0,','0,','0']


def grabData():

   fopen = open("EepRcpDefault.c", 'r')

   recipeTimeFlag = 0
   recipeTempFlag = 0
   recipeSteamTypeFlag = 0
   recipeSteamPercentFlag = 0
   recipeFanSpeedFlag = 0
   recipeFanReverseFlag = 0
   recipeFanReverseTimeFlag = 0
   recipeVentFlag = 0

   for lines in fopen:
      if lines.find("EEP_RCP_TIME") > 0:
         recipeTimeFlag = 1
      elif lines.find("EEP_RCP_TEMP") > 0:
         recipeTempFlag = 1
         recipeTimeFlag = 0
      elif lines.find("EEP_RCP_STEAM_TYPE") > 0:
         recipeTempFlag = 0
         recipeSteamTypeFlag = 1
      elif lines.find("EEP_RCP_STEAM_PERCENTAGE") > 0:
         recipeSteamTypeFlag = 0
         recipeSteamPercentFlag = 1
      elif lines.find("EEP_RCP_FAN_SPEED") > 0:
         recipeSteamPercentFlag = 0
         recipeFanSpeedFlag = 1
      elif lines.find("EEP_RCP_FAN_REVERSE") > 0:
         recipeFanSpeedFlag = 0
         recipeFanReverseFlag = 1
      elif lines.find("EEP_RCP_FAN_REVAERSE_TIME") > 0:
         recipeFanReverseFlag = 0
         recipeFanReverseTimeFlag = 1
      elif lines.find("EEP_RCP_VENT") > 0:
         recipeFanReverseTimeFlag = 0
         recipeVentFlag = 1
      else:
         if recipeTimeFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               timeDataList.append(lines[:commentLoc].split() + DEFAULT)
         elif recipeTempFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               tempDataList.append(lines[:commentLoc].split() + DEFAULT)
         elif recipeSteamTypeFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               steamTypeDataList.append(lines[:commentLoc].split() + DEFAULT)
         elif recipeSteamPercentFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               steamPercentDataList.append(lines[:commentLoc].split() + DEFAULT)
         elif recipeFanSpeedFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               fanSpeedDataList.append(lines[:commentLoc].split() + DEFAULT)
         elif recipeFanReverseFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               fanReverseDataList.append(lines[:commentLoc].split() + DEFAULT)
         elif recipeFanReverseTimeFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               fanReverseTimeDataList.append(lines[:commentLoc].split() + DEFAULT)
         elif recipeVentFlag == 1:
            commentLoc = lines.find('//') 
            if commentLoc > 0:
               #print (lines[:commentLoc].split() + DEFAULT)
               ventDataList.append(lines[:commentLoc].split() + DEFAULT)
         else:
            pass

   print ("Time List " + str(len(timeDataList)))
   print ("Temp List " + str(len(tempDataList)))
   print ("Steam Type List " + str(len(steamTypeDataList)))
   print ("Steam Percent List " + str(len(steamPercentDataList)))
   print ("Fan Speed List " + str(len(fanSpeedDataList)))
   print ("Fan Reverse List " + str(len(fanReverseDataList)))
   print ("Fan Reverse Time List " + str(len(fanReverseTimeDataList)))
   print ("Vent List " + str(len(ventDataList)))

   fopen.close()

def newRecipeParameters():
   fopen = open("newRecipeTable", 'w')

   spacing = 80
   TAB = "   "

   emptyValueString = "{0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },"


   fopen.write("const EEP_RECIPE EEP_DEFAULT_RCP[] = { \n")

   for x in range(0, 100):
      # Recipe Name
      fopen.write( "//" + recipeNameList[x] + '\n')
      fopen.write( "{\n")
      #fopen.write("\t// \t0\t1\t2\t3\t4\t5\t6\t7\t8\t9 \n")
      L1 = (TAB + "TRUE,")
      Tab = ( (spacing - len(L1) ) * " "  )
      fopen.write(L1 + Tab + "//Active\n")

      L2 = (TAB +  "{"+ "\"" + recipeNameList[x].rstrip() + "\"" + "}," )
      Tab = ( (spacing - len(L2) ) * " "  )
      fopen.write(L2 + Tab + "//Name\n")

      L3 = (TAB + "{\"\"},")
      Tab = ( (spacing - len(L3) ) * " "  )
      fopen.write(L3 + Tab + "//Recipe Image Name\n")

      L4 = (TAB + "1,")
      Tab = ( (spacing - len(L4) ) * " "  )
      fopen.write(L4 + Tab + "//Category\n")

      L5 = (TAB + emptyValueString )
      Tab = ( (spacing - len(L5) ) * " "  )
      fopen.write(L5 + Tab + "//Core Probe Cook\n")

      L6 = (TAB +  emptyValueString )
      Tab = ( (spacing - len(L6) ) * " "  )
      fopen.write(L6 + Tab + "//Core Probe Cook & Hold\n")

      L7 = (TAB +  coreProbePullTemp )
      Tab = ( (spacing - len(L7) ) * " "  )
      fopen.write(L7 + Tab + "//Core Probe Pull Temp\n")

      L8 = (TAB +  "{" +  ''.join(timeDataList[x] )  + "}," )
      Tab = ( (spacing - len(L8) ) * " "  )
      fopen.write(L8 + Tab + "//Cook Time\n")

      L9 = (TAB +  "{" +  ''.join(tempDataList[x] )  + "}," )
      Tab = ( (spacing - len(L9) ) * " "  )
      fopen.write(L9 + Tab + "//Cook Temp\n")

      L10 = (TAB +  "{" +  ''.join(steamTypeDataList[x] )  + "}," )
      Tab = ( (spacing - len(L10) ) * " "  )
      fopen.write(L10 + Tab + "//Steam Type\n")

      L11 = (TAB +  "{" +  ''.join(steamPercentDataList[x] )  + "}," )
      Tab = ( (spacing - len(L11) ) * " "  )
      fopen.write(L11 + Tab + "//Steam Percentage\n")

      L12 = (TAB +  "{" +  ''.join(fanSpeedDataList[x] )  + "}," )
      Tab = ( (spacing - len(L12) ) * " "  )
      fopen.write(L12 + Tab + "//Fan Speed\n")

      L13 = (TAB +  "{" +  ''.join(fanReverseDataList[x] )  + "}," )
      Tab = ( (spacing - len(L13) ) * " "  )
      fopen.write(L13 + Tab + "//Fan Reverse\n")

      L14 = (TAB +  "{" +  ''.join(fanReverseTimeDataList[x] )  + "}," )
      Tab = ( (spacing - len(L14) ) * " "  )
      fopen.write(L14 + Tab + "//Fan Reverse Time\n")

      L15 = (TAB + emptyValueString)
      Tab = ( (spacing - len(L15) ) * " "  )
      fopen.write(L15 + Tab + "//Fan Delay Time\n")

      L16 = (TAB +  "{" +  ''.join(ventDataList[x] )  + "}," )
      Tab = ( (spacing - len(L16) ) * " "  )
      fopen.write(L16 + Tab + "//Vent\n")

      L17 = (TAB + emptyValueString)
      Tab = ( (spacing - len(L17) ) * " "  )
      fopen.write(L17 + Tab + "//Vent Delay\n")

      L18 = (TAB + emptyValueString)
      Tab = ( (spacing - len(L18) ) * " "  )
      fopen.write(L18 + Tab + "//Time Mode\n")

      L19 = (TAB + emptyValueString)
      Tab = ( (spacing - len(L19) ) * " "  )
      fopen.write(L19 + Tab + "//Sensitivity Level\n")

      ALARM = "{0, 0, 0},"

      L20 = (TAB + ALARM)
      Tab = ( (spacing - len(L20) ) * " "  )
      fopen.write(L20 + Tab + "//Alarm Time\n")

      L21 = (TAB + ALARM)
      Tab = ( (spacing - len(L21) ) * " "  )
      fopen.write(L21 + Tab + "//Alarm Cancel\n")

      ALARM = "{{\"\"}, {\"\"}, {\"\"}},"

      L22 = (TAB + ALARM)
      Tab = ( (spacing - len(L22) ) * " "  )
      fopen.write(L22 + Tab + "//Alarm Name\n")

      L22 = (TAB + "0,")
      Tab = ( (spacing - len(L22) ) * " "  )
      fopen.write(L22 + Tab + "//Hold Time\n")

      L22 = (TAB + "0,")
      Tab = ( (spacing - len(L22) ) * " "  )
      fopen.write(L22 + Tab + "//Hold Temperature\n")

      L22 = (TAB + "0,")
      Tab = ( (spacing - len(L22) ) * " "  )
      fopen.write(L22 + Tab + "//Hold Fan Speed\n")


      fopen.write("}, \n")
      fopen.write("\n")

   #print (emptyValueString)
   fopen.write("}; \n")
   fopen.close()

def recipeName():
   fopen = open("recipename")

   for lines in fopen:
      quoteLoc = lines.find('"')
      #print (lines[:quoteLoc])
      recipeNameList.append( (lines[:quoteLoc]) )
   fopen.close()

   print ("Recipe List " + str(len(recipeNameList)))

recipeName()
grabData()
newRecipeParameters()

