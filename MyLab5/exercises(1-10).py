import re
with open("1-10exercises.txt",encoding="utf-8") as f:
           data=f.read()
    
    
#matches a string that has an 'a' followed by zero or more 'b''s.


matches=re.findall("a.*?b",data)  #.*? finds closest b and .* finds last b
print("Exercise 1: ", matches)


#matches a string that has an 'a' followed by two to three 'b'.


matches=re.findall("ab{2,3}" , data)  #{} interval b's number is between 2 and 3
print("Exercise 2: ",matches)    


#find sequences of lowercase letters joined with a underscore.


matches=re.findall("[a-z]+_[a-z]+", data)    # + means one or moreee letters
print("Execise 3",matches)  #if it has no underscore or if it has uppercase letters it doesnot matches



#find the sequences of one upper case letter followed by lower case letters.

matches=re.findall("[A-Z][a-z]+", data) #starts with one uppercase and otehrs with lowercase
print("Execise 4",matches)  


#matches a string that has an 'a' followed by anything, ending in 'b'.

matches=re.findall("a.*b$", data, re.MULTILINE) #.* anything number letter, $ конец строки , MULTILINE ищет указанное правила во всех строках без него код будет искать только в конце
print("Execise 5",matches)  



#replace all occurrences of space, comma, or dot with a colon.
matches=re.sub("[., ]",";", data) # [elements which we find and change] , ; is element which we need to change
print("Execise 6",matches)  



#convert snake case string to camel case string.
matches=re.replace("_", " ").title().replace(" ", "")  #title makes every word first letter in uppercase
print("Execise 7",matches) 




#8split a string at uppercase letters.


    
print("Exercise 8")
print(re.findall("[A-Z][a-z]*", data))  #одна заглавная и * 0 или больше сторчных букв


#9
print("Exercise 9")
print(re.sub(r"([a-z])([A-Z])", r"\1 \2", data)) #ищет маленькую букву перед заглавной и добавляет пустое место

#10
print("Exercise 10")
matches = re.sub(r"([a-z])([A-Z])", r"\1_\2", data).lower()  #Ищет строчную букву, за которой идёт заглавная потом вставляет междуними '_' и переводит лоуеркейс
print(matches)