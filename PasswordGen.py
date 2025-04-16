## password generator 
#3 from microsoft Create strong passwords
# 1. at least 12 characters 
# 2. uppercase letters, lowercase letters, numbers, and symbol
# Not a word that can be found in a dictionary or the name of a person, character, product, or organization.

## all enlgish words https://www.kaggle.com/datasets/lennartluik/all-english-words-csv
import random
 
 
arraywords = ['a','c','d','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','u','r','s','t','u','v','x','y','z','!','@','$','%','^','&','*']
x = random.randrange(0,56,1)

print(arraywords[x])
password = []

y = 0

while y <= 14: 
    x = random.randrange(0,56,1)
    password.append(arraywords[x])
    y+=1


passwordstring = "".join(password)
print(passwordstring)

## next steps create interface to ask how long you want the password 
## if you want common words 
## how many passwords. 