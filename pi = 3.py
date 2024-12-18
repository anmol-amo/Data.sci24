pi = 3.14
x = (int(pi))
print(x)

heltal = 5
y = float(heltal)
print(y)

resultat = round (0.1 + 0.2, 1) #Avrunda till 1 decimal
print (resultat)  #output 0.3

tal1 = 0.1
tal2 = 0.2
tal1 = int(tal1 * 10)
tal2 = int(tal2 * 10)
print(tal1 + tal2)
korrektsvar = (tal1 + tal2) / 10
print(korrektsvar)

x = "10"
y = "23"
summa = int(x) + int(y)
print(f"summan är: {summa}")

'''''
text = "python är roligt"
no_whitespace = text.strip
print(no_whitespace)
fantastico = no_whitespace.replace("roligt","fantastico")
print(fantastico)
UPPER = fantstico.upper()
print(UPPER)
'''
'''''
namn = input("vad heter du?: ")
age = input("hur gammal är du?: ")
print (f"hej,{namn}! du är {age} år gammal")
'''
'''''
try:
    x = int("hej")
except:
   print("Ett fel uppstod")
   '''

longList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(longList[0:5])

reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(reallyLongList[0:])
print(reallyLongList[4:])
print(reallyLongList[:14])
print(reallyLongList[3:14])
print(reallyLongList[-1:0])
# print(reallyLongList.reverse())


my_list = ["äpple", "banan", "körsbär"]

for fruit in my_list:
    if fruit != "körsbär":
      print("Jag gillar " + fruit)
    else:
      print("Jag gillar inte " + fruit)



reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

for index, number in enumerate(reallyLongList):
    print(index, number)

reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in reallyLongList:
    if number % 2 == 0:
        print(number)

for number in reallyLongList:
    if number % 2 != 0:
        print(number)