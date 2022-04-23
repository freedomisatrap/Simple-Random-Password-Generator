#Simple Random Password Generator App

#Importing the relevant modules
from random import randint 

#All uppercase password
password =""
for i in range(12):
    i = chr(randint(65,98))
    password =str(password)+i
print(password)   

#Upper and lowercase password
password =""
for i in range(5):
    i = chr(randint(65,98))
    for j in range (5):
        j=chr(randint(65,90)).lower()
    password =str(password)+i+j
print(password)   

password=""
for i in range(10):
    i=chr(randint(20,50))
    for j in range (10):
        j=chr(randint(1,19))
        for k in range(10):
            k=chr(randint(70,80))
password =str(password)+i+j+k
print(password)  