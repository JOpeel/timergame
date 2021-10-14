import random
import threading as t

randomstring = []
string = ""

for i in range(20):
    randomstring.append(chr(random.randint(97,122)))

for x in randomstring:
    string += x

print(string)
print("")
userinput = input("enter string:")

if userinput==string:
    print("congrats")
else:
    print("incorrect")
