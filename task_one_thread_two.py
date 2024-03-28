from pathlib import Path
from threading import Thread
import os
import shutil


x = input('Enter folder:')
y = input('Enter target folder:')
path = Path(x)

folders_list = [path]

#CREATING NEW FOLDERS
def folder_creater(outer_folder, new_folder):
    loaction = outer_folder+"\\"+new_folder
    return loaction

#DEFININNG TARGET TOLDER
if os.path.isdir(y):
    target_folder = y
else:
    target_folder = folder_creater(x, "dist")
    os.mkdir(target_folder)


# ПЕРЕЧЕНЬ СВЕХ ПАПОК      - фор айтем ин тут отпралять на перечень файлов, который вернет файлы в папке и результат в файлхендлер
def folders_finder(path_folder):
    for item in path_folder.iterdir():
        if os.path.isdir(item):
            folders_list.append(item)
            folders_finder(item)

#ПЕРЕЧЕНЬ ФАЙЛОВ ВО ВСЕХ ПАПКАХ
def files_finder(path):
    fileslist = []
    for item in path.iterdir():
        if os.path.isfile(item):
            fileslist.append(item)
    return fileslist

#CREATING NEW FOLDERS AND COPY FILES
def filehandler(folder):
    for file_location in files_finder(folder):
        file_extension = os.path.splitext(file_location)[1][1:]
        folder_to_copy = folder_creater(target_folder, file_extension)
        if not os.path.isdir(folder_to_copy):
            os.mkdir(folder_to_copy)
        shutil.copy(file_location, folder_to_copy)


if __name__ == '__main__':
    folders_finder(path)

    for folder in folders_list:
        thread = Thread(target=filehandler, args=(folder,))
        thread.start()