import os
import shutil
files = os.listdir()

Folders = {
    ".png" : "PNG FOLDER",
    ".jpg" : "JPG FOLDER",
    ".jpeg" : "JPEG FOLDER",
    ".webp" : "WEBP FOLDER",
    ".gif"  : "GIF FOLDER",
    ".mp4" : "MP4 FOLDER"   
}
for folder in Folders.values():
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Folder Sucessfully Created in Your Directory -----------> {os.getcwd()}")
    else:
        print(f"Folder Alreasy Exists In Your Dirctory ---------> {os.getcwd()}")

for file in files:
    extension = os.path.splitext(file)[1].lower()
    # print(extension)
    if extension in Folders:
        sourcePath = os.path.join(os.getcwd(),file)
        DestinationPath = Folders[extension]
        # print(sourcePath)
        # print(DestinationPath)
        
    try :
        shutil.move(sourcePath,DestinationPath)
        print(f"File Moved Succesfully From {file} to {Folders[extension]}")
    except Exception as e :
        print(f"Not Moved : {e}")