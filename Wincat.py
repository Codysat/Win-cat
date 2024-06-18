import time 
from notifypy import Notify
import random 


notification = Notify(
  default_notification_title="Desktop cat🐈",
  default_application_name="Win cat🐈",
  default_notification_icon=(r"C:\Users\user\Downloads\Win cat.png"),
  default_notification_audio=(r"C:\Users\user\Downloads\Win cat1.wav")
 )

def wincat():
  while True:

    notification.message = "ฅ•ω•ฅMEOOOOOWฅ•ω•ฅ"
    notification.send()
    time.sleep(300)
    print(wincat())

print(wincat())
