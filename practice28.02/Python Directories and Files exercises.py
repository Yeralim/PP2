#ex1

import os

def list_directories_files(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return
    
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll Directories & Files:")
    for item in os.listdir(path):
        print(item)

path = input("Enter the path: ")
list_directories_files(path)


#ex2

import os

def check_path_access(path):
    print(f"Checking access for: {path}")
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = input("Enter the path to check: ")
check_path_access(path)


#ex3

import os

def check_path(path):
    if os.path.exists(path):
        print("Path exists!")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist!")

path = input("Enter the path: ")
check_path(path)


#ex4

def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found!")

filename = input("Enter the filename: ")
count_lines(filename)


#ex5

def write_list_to_file(filename, data_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(str(item) + '\n')
    print(f"List written to {filename}")

filename = "output.txt"
data = ["Apple", "Banana", "Cherry", "Date"]
write_list_to_file(filename, data)

