import os
import shutil



if os.path.exists('C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder'):
    print("We're good to go!")
else:
    print("ERROR")

items = os.listdir("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder")
print(items)

img = 0
dox = 0
vid = 0
other = 0

if not os.path.exists("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Images"):
    os.mkdir("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Images")
    print("GOT DONE")
else:
    print("NOT GOT DONE")

if not os.path.exists("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Documents"):
    os.mkdir("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Documents")
    print("GOT DONE")
else:
    print("NOT GOT DONE")

if not os.path.exists("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Videos"):
    os.mkdir("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Videos")
    print("GOT DONE")
else:
    print("NOT GOT DONE")

if not os.path.exists("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Others"):
    os.mkdir("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Others")
    print("GOT DONE")
else:
    print("NOT GOT DONE")

for item in items:
    if item == "Images" or "Documents" or "Videos" or "Others" or os.path.isdir() == True:
        continue
    else:
        if item.endswith(".jpg",".jpeg",".png",".gif"):
            shutil.move("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Images")
            img += 1
            print(item,"moved to images")
        elif item.endswith(".pdf",".docx",".txt",".pptx"):
            shutil.move("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Documents")
            dox += 1
            print(item,"moved to documents")
        elif item.endswith(".mp4",".mov",".avi"):
            shutil.move("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Videos")
            vid += 1
            print(item,"moved to videos")
        else:
            shutil.move("C:/Users/STUDENT/Desktop/TEST_MANARANG_MARIUS/test_folder/Others")
            other += 1
            print(item,"moved to others")