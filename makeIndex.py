import os
import pickle
import json
import cv2
import numpy as np
import scipy as ss
import scipy.stats as st
import matplotlib.pyplot as plt



def detectFaceFrontal(key,out):
 face_cascade = cv2.CascadeClassifier('/home/kk/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
 img = cv2.imread(key,4)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 faceFrontal = 0
 title = 'face'

 for (x,y,w,h) in faces:
  if faces != [] : 
   faceFrontal = 1
   title = 'This is face frontal'
   print ('Face frontal!', key)
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 if out == 1:  
  cv2.imshow(title,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  cv2.imwrite(key + '_frontal_face.jpg',img) 
 return faceFrontal
                
#===============================================================================
def detectFaceProfile(key,out):
 face_cascade = cv2.CascadeClassifier('/home/kk/opencv/data/haarcascades/haarcascade_profileface.xml')
 img = cv2.imread(key,4)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(gray, 1.1, 3)
 faceProfile = 0
 title = 'face'
 
 for (x,y,w,h) in faces:
  if faces != [] : 
   faceProfile = 1
   title = 'This is profile face'
   print ('Face profile!', key)
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

 if out == 1:  
  cv2.imshow(title,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  cv2.imwrite(key + '_profile.jpg',img) 
 return faceProfile
                
#===============================================================================

def detectEye(key,out):
 eye = 0
 eye_cascade = cv2.CascadeClassifier('/home/kk/opencv/data/haarcascades/haarcascade_eye.xml')
 #for top,dirs,files in os.walk('/home/kk/Desktop/test/Images/faces/'):
  #print(top, dirs, files)
  #for nm in files:
   #key   = os.path.join(top,nm)
   #img = cv2.imread("/%s/%s" % (top, nm),3)
 img = cv2.imread(key,3)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 eyes = eye_cascade.detectMultiScale(gray)
 for (x,y,w,h) in eyes:
  if eyes != [] : 
   eye = 1
   img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   print ('Eye!', key)
 title = 'eye'
 if out == 1:  
  cv2.imshow(title,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  cv2.imwrite(key + '_eye.jpg',img) 
 return eye
                
#===============================================================================
def detectMouth(key,out):

 mouth_cascade = cv2.CascadeClassifier('/home/kk/opencv/data/haarcascades/Mouth.xml')
 img = cv2.imread(key,3)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 mouths = mouth_cascade.detectMultiScale(gray, 1.3, 5)
 mouth = 0
 
 for (x,y,w,h) in mouths:
  if mouths != [] : 
   mouth = 1
   print ('Mouth!', key)
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   
 title = 'mouth'
 if out == 1:  
  cv2.imshow(title,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  cv2.imwrite(key + '_mouth.jpg',img) 
 return mouth
                
#===============================================================================
def detectSmile(key,out):
 smile_cascade = cv2.CascadeClassifier('/home/kk/opencv/data/haarcascades/haarcascade_smile.xml')
 img = cv2.imread(key,3)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 smiles = smile_cascade.detectMultiScale(gray, 1.3, 5)
 smile = 0
 for (x,y,w,h) in smiles:
  if smiles != [] : 
   smile = 1
   print ('Smile!', key)
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 title = 'smile'
 if out == 1:  
  cv2.imshow(title,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  cv2.imwrite(key + '_smile.jpg',img) 
 return smile
                
#===============================================================================

def detectBody(key,out):
 body_cascade = cv2.CascadeClassifier('/home/kk/opencv/data/haarcascades/haarcascade_fullbody.xml')
 img = cv2.imread(key,3)
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 bodies = body_cascade.detectMultiScale(gray, 1.1, 3)
 body = 0
 for (x,y,w,h) in bodies:
  if bodies != [] : 
   body = 1
   print ('Body!', key)
   img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   title = 'body'  
 if out == 1:  
  cv2.imshow(title,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  cv2.imwrite(key + '_body.jpg',img)  
 return body

#===============================================================================

def detectType(key,out):
 typ = None
 img = cv2.imread(key,4)

 hiss = plt.hist(img.ravel(),256,[0,256])
 if out == 1:
  plt.show()


 dataOfHistogram = list(hiss)
 print (dataOfHistogram)
 #c.count(0)
 yCoordinats = dataOfHistogram[0]
 print (yCoordinats)
 answer = 0
 maxElement = max(yCoordinats)
 print ('maxElement: ',maxElement)
 porog = maxElement/1000
 i = 0
 for element in yCoordinats:
  print (i,':',yCoordinats[i])
  if (yCoordinats[i] < porog):
   answer = answer + 1
  i = i + 1

 print ('Count:',answer)
 if (answer<150):
  typ = 1
  title = 'This is photo'
 else:
  typ = 0
  title = 'This is scheme'
 if out == 1:  
  cv2.imshow(title,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows() 
  cv2.imwrite(key + '_type.jpg',img) 
 return typ

#===============================================================================
         
def makeDict():
 imgDict = dict() 
 for top,dirs,files in os.walk('/home/kk/Desktop/tests/'):
 #print(top, dirs, files)
  for nm in files:
   key   = os.path.join(top,nm)
   #print (key)
   types = detectType(key,out)
   if (types == 1):
    faceFrontal = detectFaceFrontal(key,out)
    faceProfile = detectFaceProfile(key,out)
    mouth = detectMouth(key,out)
    smile = detectSmile(key,out)
    eye = detectEye(key,out)
    body = detectBody(key,out)
   else:
    faceFrontal  = 0
    faceProfile  = 0
    mouth = 0
    smile = 0
    eye = 0
    body = 0
   imgDict.update({key:(types,faceFrontal,faceProfile,mouth,smile,eye,body)})
  print ('=========================== Our cool dictionary: ===================================')
  print (imgDict)
  with open('index','w') as f:
   json.dump(imgDict,f)


    
if __name__=="__main__":
 out = 0
 makeDict()

else:
 out = 1
