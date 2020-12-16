# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:24:35 2019

@author: Ryan Gamilo
"""

import os
import re
import time

os.startfile("C:\\Program Files (x86)\\Audacity\\audacity.exe")
time.sleep(10)

import recording_test as session

def MP3Conversion(path):
    session.do("Import2: Filename=" + "\"" + path + "\"")
    session.do("Select: Track=0")
    #session.do("\"Macro_MP3 Conversion\"")
    session.do("SelTrackStartToEnd")
    session.do("Normalize: ApplyGain=\"1\" PeakLevel=\"0\" RemoveDcOffset=\"1\" StereoIndependent=\"0\"")
    session.do("Amplify: AllowClipping=\"0\" Ratio=\"1.41254\"")
    session.do("ExportMp3")
    session.do("RemoveTracks")

inPath = "C:\\Users\\Ryan Gamilo\\Music\\Spotify"
expPath = inPath + "\\macro-output"
outPath = inPath + "\\cleaned"

#print(inPath)

while True:
    inList = [i for i in os.listdir(inPath) if re.search(".*mp3", i)]
    inDict = {}
    
    x = 0
    for i in inList:
        if i not in os.listdir(outPath):
            inDict[x] = {"name":i, "path": inPath + "\\" + i}
        x += 1
    
    print("You have " + str(len(inDict)) + " new songs.")
    if len(inDict) != 0:
        x = 1
        for key in inDict:
            print ("Now Converting: " + inDict[key]["name"] + "(" + str(x) + " of " + str(len(inDict)) + ")")
            MP3Conversion(inDict[key]["path"])
            x += 1
            
        for i in os.listdir(expPath):
            os.replace(expPath + "\\" + i, outPath + "\\" +i)
     
    time.sleep(5)





