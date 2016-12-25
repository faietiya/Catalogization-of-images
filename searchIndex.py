import os
import pickle
import json
import cv2
import numpy as np
import scipy as ss
import scipy.stats as st
import matplotlib.pyplot as plt
import sys
import makeIndex as me

def indexSearch(out):
 with open('index','r') as f:
  ind = json.load(f)
  print(ind)
  print("======================This was our dictionary, thanks.=========================")
  needed = sys.argv[1] 
  options = {
   'photo': 0,
   'scheme': 0,
   'face': 12,
   'faceFrontal': 1,
   'faceProfile': 2,
   'mouth': 3,
   'smile': 4,
   'eye': 5,
   'body': 6
  }
  
  print ('needed',needed)
  for key, value in options.items():
   if key == needed:
    print (key, value)
    indexOfElement = value
    print ('indexOfElement',indexOfElement)
    break
   
   
  b = 'a'
  for key, value in ind.items():
   b = b +'b'
   stroka = value
   aa = 0
   print ('stroka',stroka)
   if indexOfElement == 0:
    i = stroka [0]
    print ('index',stroka.index(i),'znachElement',i)
    if needed == 'scheme' and i == 0:
     aa = 1
     #img = cv2.imread(key,4)
     me.detectType(key,out)
    if needed == 'photo' and i == 1:
     aa = 1
     #img = cv2.imread(key,4)
     me.detectType(key,out)
     
   if indexOfElement == 1:
    i = stroka [1]
    print ('index',stroka.index(i),'znachElement',i)
    if needed == 'faceFrontal' and i == 1:
     aa = 1
     me.detectFaceFrontal(key,out)
     #img = cv2.imread(key,4)
   
     
   if indexOfElement == 2:
    i = stroka [2]
    print ('index',stroka.index(i),'znachElement',i)
    if needed == 'faceProfile' and i == 1:
     aa = 1
     #img = cv2.imread(key,4)   
     me.detectFaceProfile(key,out)  
     
   if indexOfElement == 12:
    i = stroka [1]
    ii = stroka [2]
    print ('index',stroka.index(i),'znachElement',i)
    print ('index',stroka.index(ii),'znachElement',ii)
    if needed == 'face' and ( i == 1 or ii == 2 ):
     aa = 1
     #img = cv2.imread(key,4) 
     me.detectFaceProfile(key,out) 
     me.detectFaceFrontal(key,out)   
   
   if indexOfElement == 3:
    i = stroka [3]
    print ('index',stroka.index(i),'znachElement',i)
    if needed == 'mouth' and i == 1:
     aa = 1
     #img = cv2.imread(key,4) 
     me.detectMouth(key,out)     
   
   if indexOfElement == 4:
    i = stroka [4]
    print ('index',stroka.index(i),'znachElement',i)
    if needed == 'smile' and i == 1:
     aa = 1
     #img = cv2.imread(key,4) 
     me.detectMouth(key,out)     
   
   if indexOfElement == 5:
    i = stroka [5]
    print ('index',stroka.index(i),'znachElement',i)
    if needed == 'eye' and i == 1:
     aa = 1
     #img = cv2.imread(key,4)  
     me.detectEye(key,out)    
   
   if indexOfElement == 6:
    i = stroka [6]
    print ('index',stroka.index(i),'znachElement',i)
    if needed == 'body' and i == 1:
     aa = 1
     #img = cv2.imread(key,4)  
     me.detectBody(key,out) 

   #if aa == 1:
    #cv2.imshow('I found!',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows() 
#==============================================================================
if __name__=="__main__":
 if len (sys.argv) > 1:
  out = 1
  indexSearch(out)  
 else:
  print ('You do it wrong. Needed an argument.')
