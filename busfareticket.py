import random

prices = {
    "ADULT": "£0.40",
    "CHILD": "£57.40",
    "TEEN": "£0.10"
}

def boxMaker(primary, padding, secondary):
    boxSize = "               "
    placeHolder = ""
    posHolder = ""
    wSpaceAvailable = len(boxSize) - len(placeHolder)

    characterArr = []
    characterArr = list(primary)


    placeHolder = boxSize[:len(primary)]
    for i in range(0,len(characterArr)):
        placeHolder = placeHolder.replace(" ",characterArr[i], 1)
  
    wSpaceAvailable = len(boxSize) - len(placeHolder) 

    if type(padding) == int:
        for i in range(0,padding):
            placeHolder += " "

    if primary in prices:
        secondary = prices[primary]

    if padding == "MAX" and not primary in prices:
        maxSecondary = len(secondary[:wSpaceAvailable])
        placeHolder += f"{posHolder:>{wSpaceAvailable-maxSecondary}}"

    if padding == "MAX" and primary in prices:

        maxSecondary = len(secondary)

        placeHolder += f"{posHolder:>{wSpaceAvailable-maxSecondary}}"

    placeHolder += secondary

    if len(placeHolder) > 15:
        placeHolder = placeHolder[:15]

    elif len(placeHolder) < 15:
        while len(placeHolder) < 15:
            placeHolder += " "
        
    placeHolder = placeHolder.replace(" ", "*")  
    return placeHolder



randLet = ['A','B','C','D','E','F','G','H','I','J','K']
ranSt = randLet[random.randint(0,10)] + str(random.randint(10,99))



age = int(input("whats your age? "))
if age < 12:
    rank = "CHILD"
elif age <18 and age >= 12:
    rank = "TEEN"
else: 
    rank = "ADULT"

output = ""

output = boxMaker("ROUTE", 1, ranSt)
print(output)
output = boxMaker("AVENUE", 1, "-KINGSWAY")
print(output)
output = boxMaker(rank, "MAX", "")
print(output)



