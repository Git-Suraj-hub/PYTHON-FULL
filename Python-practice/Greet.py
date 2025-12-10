import time
import pyttsx3
engine = pyttsx3.init()

timestamp = time.strftime('%H:%M:%S')
hour = time.strftime('%H')
minute = time.strftime('%M')
second = time.strftime('%S')
engine.say(f"{hour} bajke {minute} minute")
engine.runAndWait()
print(timestamp);
if hour>="1" and timestamp<="11:59:59":
    engine.say("good MOrning Suraj")
    engine.runAndWait()
elif hour>="12" and timestamp <= "16:59:59":
    engine.say("good afternoon")
    engine.runAndWait()
else:
    engine.say("good evening Suraj")
    engine.runAndWait()
