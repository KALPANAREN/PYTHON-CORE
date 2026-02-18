import os
print(os.getcwd())

# create a new directory

new_dir = "PACKAGE2"
os.mkdir(new_dir)
print()

# listing files and directories

items = os.listdir('.')
print(items)

# joining paths

dir_name = 'PACKAGE'
file_name = 'example.txt'
relative_path = os.path.join(dir_name,file_name)
print(relative_path)
full_path = os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)

# check for path existence

file_name = 'example.txt'
if os.path.exists(file_name):
    print(True)