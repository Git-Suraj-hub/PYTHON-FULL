import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# print(speaker.__getattribute__)

List = ["RAHUL","SURAJ SINGH MEHTA","SURAJ KHANAL","VIBHANSHU UPADHAYA","NISHANT YADAV","HIMANSHU MEHTA"]

# # for i in List:
# #     speaker.Speak(f"Shoutout To {i}")


for t in List: 
    print(f"shoutout to {t}")
for name in List: 
    names = name.split()
    shoutout = f"Shoutout to {names[0]}" 
    speaker.Speak(shoutout) 
print("Shout out of all for guys")