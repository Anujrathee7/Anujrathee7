import shutil
file_name = input("Please give the name of the source file:\n")

copy_file = input("Please give the name of the destination file:\n")

shutil.copy(file_name,copy_file)

print("File copied successfully!")