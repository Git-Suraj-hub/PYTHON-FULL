import os 
import shutil
folder = os.listdir()
jpg = "JPG FOLDER"
png = "PNG FOLDER"
jpeg = "JPEG FOLDER"
webp = "WEBP FOLDER"
gif = "GIF FOLDER"
if not os.path.exists(png):
    os.mkdir(png)
    print(f"The {png} is Succefull Created")
else:
    print(f"The {png} Already Exist in Your Current Directory -------->  {os.getcwd()}")
if not os.path.exists(jpg):
    os.mkdir(jpg)
    print(f"The {jpg} is Succefull Created")
else:
    print(f"The {jpg} Already Exist in Your Current Directory -------->  {os.getcwd()}")
if not os.path.exists(jpeg):
    os.mkdir(jpeg)
    print(f"The {jpeg} is Succefull Created")

else:
    print(f"The {jpeg} Already Exist in Your Current Directory -------->  {os.getcwd()}")
if not os.path.exists(gif):
    os.mkdir(gif)
    print(f"The {gif} is Succefull Created")
else:
    print(f"The {gif} Already Exist in Your Current Directory -------->  {os.getcwd()}")
if not os.path.exists(webp):
    os.mkdir(webp)
    print(f"The {webp} is Succefull Created")
else:
    print(f"The {webp} Already Exist in Your Current Directory -------->  {os.getcwd()}")

files = os.listdir()
for i in files:
    if i.endswith(".png"):
        shutil.move(i,"PNG FOLDER")
        print(f"{i} is succesfully Moved in Png Directory")
    elif i.endswith(".gif"):
        shutil.move(i,"GIF FOLDER")
        print(f"{i} is succesfully Moved in Gif Directory")
    elif i.endswith(".jpeg"):
        shutil.move(i,"JPEG FOLDER")
        print(f"{i} is succesfully Moved in Jpeg Directory")
    elif i.endswith(".webp"):
        shutil.move(i,"WEBP FOLDER")
        print(f"{i} is succesfully Moved in WEBP Directory")
    elif i.endswith(".jpg"):
        shutil.move(i,"JPG FOLDER")
        print(f"{i} is succesfully Moved in JPG Directory")
        

print(files)