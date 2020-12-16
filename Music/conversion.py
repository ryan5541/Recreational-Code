# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:24:35 2019

@author: Ryan Gamilo
"""

import os
import re
import time
import datetime

os.startfile("D:\\Program Files (x86)\\Audacity\\audacity.exe")
time.sleep(10)

while True:
    try:
        import recording_test as session
    except:
        pass
    else:
        break

def MP3Conversion(path):
    session.do("Import2: Filename=" + "\"" + path + "\"")
    session.do("Select: Track=0")
    #session.do("\"Macro_MP3 Conversion\"")
    session.do("SelTrackStartToEnd")
    session.do("Normalize: ApplyGain=\"1\" PeakLevel=\"0\" RemoveDcOffset=\"1\" StereoIndependent=\"0\"")
    session.do("Amplify: AllowClipping=\"0\" Ratio=\"1.41254\"")
    session.do("ExportMp3")
    session.do("RemoveTracks")

#def mainloop():
inPath = "D:\\Users\\Ryan Gamilo\\Music\\Spotify"
expPath = inPath + "\\macro-output"
outPath = inPath + "\\cleaned"

#print(inPath)
date_obj = datetime.datetime

while True:
    current_time = date_obj.now()
    inList = [i for i in os.listdir(inPath) if re.search(".*mp3$", i)]
    inDict = {}
    
    x = 1
    for i in inList:
        if i not in os.listdir(outPath):
            inDict[x] = {"name":i, "path": inPath + "\\" + i}
            x += 1
    
    print("You have " + str(len(inDict)) + " new songs.(" + str(current_time)+")")
    if len(inDict) != 0:
        x = 1
        for key in inDict:
            os.rename(inPath + "\\" + inDict[key]["name"], inPath + "\\temp" + str(key) + ".mp3")
            print ("Now Converting: " + inDict[key]["name"] + "(" + str(x) + " of " + str(len(inDict)) + ")")
            MP3Conversion(inPath + "\\temp" + str(key) + ".mp3")
            os.rename(inPath + "\\temp" + str(key) + ".mp3", inPath + "\\" + inDict[key]["name"])
            os.rename(expPath + "\\temp" + str(key) + ".mp3", expPath + "\\" + inDict[key]["name"])
            os.replace(expPath + "\\" + inDict[key]["name"], outPath + "\\" + inDict[key]["name"])
            x += 1
     
    time.sleep(5)

#if __name__=="__main__":
#    mainloop()


