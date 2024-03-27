from pathlib import Path
import os
import shutil


x = input('Enter folder:')
y = input('Enter target folder:')
path = Path(x)

fileslist = []
folders_list = []

#CREATING NEW FOLDERS
def folder_creater(outer_folder, new_folder):
    loaction = outer_folder+"\\"+new_folder
    os.mkdir(loaction)
    return loaction

#ПЕРЕЧЕНЬ ФАЙЛОВ В КОНКРЕТНОЙ ПАПКЕ
def files_finder(path):

    for item in path.iterdir():
        if os.path.isfile(item):
            fileslist.append(item)
            print(item)

#DEFININNG TARGET TOLDER
target_folder = folder_creater(x, "dist")


# ПЕРЕЧЕНЬ СВЕХ ПАПОК
folders_list.append(path)

def folders_finder(path_folder):
    for item in path_folder.iterdir():
        if os.path.isdir(item):
            folders_list.append(item)
            folders_finder(item)

folders_finder(path)

for i in folders_list:
    files_finder(i)


#НАХОЖДЕНИЕ РАСШИРЕНИЯ КОНКРЕТНОГО ФАЙЛА
file_extension = os.path.splitext(fileslist[0])[1][1:]
# file_extension = os.path.splitext(fileslist[0])
# print(file_extension[1][1:])
print(file_extension)


#CREATING NEW FOLDERS
def folder_creater(outer_folder, new_folder):
    loaction = outer_folder+"\\"+new_folder
    os.mkdir(loaction)
    return loaction




#CREATING NEW DIES AND COPY FILES
def filehandler(file_location):
    file_extension = os.path.splitext(file_location)[1][1:]
    folder_to_copy = f'{target_folder}\{file_extension}'
    if not os.path.isdir(folder_to_copy):
        folder_to_copy = folder_creater(target_folder, file_extension)
    shutil.copy(file_location, folder_to_copy)

filehandler(fileslist[0])
