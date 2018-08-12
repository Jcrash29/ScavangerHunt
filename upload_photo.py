#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
#import imp
#foo = imp.load_source('ScoreCalculator', 'Scavenger Hunt')
import sys
sys.path.append('Scavenger Hunt')
import ScoreCalculator
import os

InstagramAPI = InstagramAPI("Hunt@jcrash.com", "PassWord  HERE")    
InstagramAPI.login()  # login

#photo_path = 'photo.jpg'
#caption = "Sample photo TEST"
#InstagramAPI.uploadPhoto(photo_path, caption=caption)


exDir = os.getcwd()
LastUploadDate_file = exDir + '/LastUploadDate.txt'
exDir += '/Scavenger Hunt'

#print exDir

LastUploadTime = os.path.getmtime(LastUploadDate_file)
newPhotosDetected = False

for dir in os.listdir(exDir):
    #We can exclude any directories here.
    if(os.path.isfile(os.path.join(exDir,dir)) == False):
        #print exDir + '/' + dir + ':'
        location = exDir + '/' + dir
        for file in os.listdir(location):
            fileLocation = location + '/' + file
            fileTime =  os.path.getmtime(fileLocation)
            if fileTime > LastUploadTime:
                text =  file.split('.',1)[0] + ' Just earned another point uploading a picture of: ' + dir.split('-',1)[1] + ' #ScavengerHunt #CRASH #FindTheThing'
                print text
                InstagramAPI.uploadPhoto(fileLocation, caption=text)
                newPhotosDetected = True


if newPhotosDetected == True:
    with open (LastUploadDate_file, 'wr') as file:
        file.write(' ')
        ScoreCalculator.mainStuff(exDir)
        




