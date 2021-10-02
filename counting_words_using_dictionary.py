# Creating a program to count the words occurs in a sentence#
dict={}

str="Hello! Hello! good morning. How are you Are you fine"
list=str.split()
print("This is my list:")
print(list)
for word in list:
     if word not in dict:
         dict[word]=1
     else:
         dict[word]=dict[word]+1

print(dict)         
