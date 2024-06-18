import time 
from notifypy import Notify
import random 


notification = Notify(
  default_notification_title="",
  default_application_name="",
  default_notification_icon=(r"Path to image.png"),
  default_notification_audio=(r"Path to sound.wav")
 )

def wincat():
  while True:

    notification.message = ""
    notification.send()
    time.sleep(300)
    print(wincat())

print(wincat())
