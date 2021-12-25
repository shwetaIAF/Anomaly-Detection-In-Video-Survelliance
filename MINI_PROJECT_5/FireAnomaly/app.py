import  cv2 
import numpy as np
import playsound
import smtplib


fire_Reported = 0
Alarm_status = False
# Email_Status = True

#function def for playing alarm if fire detected
def play_audio():
    playsound.playsound("fire_alarm.mp3",True)

#Function def for sending WARNING Email
def send_email_function():
    recipientEmail = "nidhishahg2929@gmail.com"
    recipientEmail = recipientEmail.lower()

    try:
        TEXT = "[Warning] !!!\n Dear Building Manager\n Please check immediately your workplace\n 70-C Race Course Floor 5th \n Textile Complex Enterprise, Ddun 248001\nA Fire Accident has been reported at your organization.\nEmergency!!! You have to call 112 immediately.\nFire Alarm System\nPlease Don't Reply!"
        SUBJECT = "[WARNING!!] Fire Accident|Emergency"
        message = 'Subject: {}\n\n{}'.format(SUBJECT,TEXT)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("shwetagaur4698@gmail.com",'oxjgxfojvhjpftbi')
        server.sendmail('shwetagaur4698@gmail.com',recipientEmail,message)
        print("Alert!!! Email sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
        print(e)

# Open a sample video available in sample-videos
video = cv2.VideoCapture("fire1.mp4")
# video = cv2.VideoCapture(0)

#video = cv2.VideoCapture(0)
#if not vcap.isOpened():
#    print "File Cannot be Opened"


#Frame Analyzation starts here
while(True):
    # Capture frame-by-frame
    ret, frame = video.read()
    frame = cv2.resize(frame, (1000,600))
    blur = cv2.GaussianBlur(frame,(15,15),0) #blurred the video to remove extra noise except fire
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18,50,50]
    upper = [35,255,255]   #lower and upper pattern are representing the colour 
                                #the fire

#To convert frames into numerical values
    lower = np.array(lower,dtype='uint8') #colour 1 value in numerical value
    upper = np.array(upper,dtype='uint8') #color 2 value

    mask = cv2.inRange(hsv,lower,upper)
    #using mask detecting fire
    blur = cv2.bitwise_and(frame,hsv,mask=mask)

    #Measuring The Fire size so that it donot ring alarm if there is only dot detected
    fireSize = cv2.countNonZero(mask)
    if int(fireSize) > 1000:
        fire_Reported = fire_Reported + 1

        if fire_Reported >= 1: #=> fire detected
            if Alarm_status == False:
                send_email_function()
                play_audio()
                Alarm_status = True  
            # if Email_Status == False:
            #     send_email_function()
            #     Email_Status = True


    #print cap.isOpened(), ret
    if frame is not None:     #or we can say if ret == False
        # Display the resulting frame
        # cv2.imshow('Fire-Detection-Frame',blur)
        cv2.imshow('Fire-Detection-Frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print ("Frame is None");
        break

#Frame Analyzation ends here


# When everything done, release the capture
video.release()
cv2.destroyAllWindows()
print ("Video stop");


 ###############################YOUTUBE############################
# #pip install pafy
# #sudo pip install --upgrade youtube_dl
# import cv2, pafy

# url   = "https://www.youtube.com/watch______"
# video = pafy.new(url)
# best  = video.getbest(preftype="webm")
# #documentation: https://pypi.org/project/pafy/

# capture = cv2.VideoCapture(best.url)
# check, frame = capture.read()
# print (check, frame)

# cv2.imshow('frame',frame)
# cv2.waitKey(10)

# capture.release()
# cv2.destroyAllWindows()
 ###############################YOUTUBE############################

