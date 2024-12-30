import os

folders_list = input("Please provide list of folders with spaces in between: ").split()
# print(folders_list)

for folder in folders_list:
    # print(folder)
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name. It looks like this folder does not exist: " + folder )
        # break
        continue
    except PermissionError:
        print("YOu don't have permission for this folder: " + folder)
        continue
    print("======== Listing the files under the directory - " + folder)
    # print(files)
    for file in files:

        print(file)
    