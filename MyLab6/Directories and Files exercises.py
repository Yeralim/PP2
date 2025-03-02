#ex1

import os

path = r"C:\Users\Admin\OneDrive\Рабочий стол\папка_example"  

if not os.path.exists(path):  
    print("Указанный путь не существует")
else:
    print("directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    
    print("\nfiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nall directories, files:")
    for item in os.listdir(path):
        print(item)


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
path = r"C:\Users\Admin\OneDrive\Рабочий стол\папка_example"
def checker(path):
    if os.path.exists(path):
        print("Name of file: ", os.path.basename(path))
        print("name of directory: ", os.path.dirname(path))
        return "success"
    
print(checker(path))


#ex4

import os
with open("sometext.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))



#ex5

def writesome(list_of_elements):
    with open("sometext.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome([12345, 6789, "apple","banana",34,34])

#ex6

import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("hello world")

if __name__ == "__main__":
    generate_files()


#ex7

def copier():
    string = str(input("Enter the name of file: "))
    with open(string) as file:
        data = file.read()
    file.close()
    copy_path = ""
    for i in range(len(string)):
        if string[i]=='.':
            copy_path+='_1'
        copy_path+=string[i]
    with open(copy_path, "+w") as file_copy:
        file_copy.write(data)
    file.close()
    
    return 0

copier()


#ex8
import os
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path,os.W_OK):
            try:
                os.remove(file_path)
                print(f"file {file_path} delete") 
            except Exception as e:
                print("Error")
                
                
        else:
            print("You do not have write access")
    else:
        print(f"File '{file_path}' does not exist.")
            
        


path_delete=str(input("path_delere_file:"))

delete_file(path_delete)