import time
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    time.sleep(3600)
    speaker.speak("Please Drink Water And Some Break")