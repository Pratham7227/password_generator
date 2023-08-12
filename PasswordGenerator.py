import random
def alphanumeric(list,rangeOfPassword):
    tempList=[]
    strx=""
    charIteration=rangeOfPassword
    intIteration=rangeOfPassword
    cobineIteration=rangeOfPassword
    while(charIteration>0):
        oneRanodmChar=random.choice(list)
        tempList.append(oneRanodmChar)
        charIteration-=1

    while(intIteration>0):
        oneRanodmInt=random.randrange(1,9)
        tempList.append(oneRanodmInt)
        intIteration-=1

    while(cobineIteration>0):
        combineLetter=random.choice(tempList)
        strx=strx+str(combineLetter)
        cobineIteration-=1

    return  strx

def alphanumericSymbols(list,symbols,rangeOfPassword):
    tempList=[]
    strx=""
    charIteration=rangeOfPassword
    intIteration=rangeOfPassword
    cobineIteration=rangeOfPassword
    symbolsIteration=rangeOfPassword
    while(charIteration>0):
        oneRanodmChar=random.choice(list)
        tempList.append(oneRanodmChar)
        charIteration-=1

    while(intIteration>0):
        oneRanodmInt=random.randrange(1,9)
        tempList.append(oneRanodmInt)
        intIteration-=1

    while(symbolsIteration>0):
        oneSymobol=random.choice(symbols)
        tempList.append(oneSymobol)
        symbolsIteration-=1
    while(cobineIteration>0):
        combineLetter=random.choice(tempList)
        strx=strx+str(combineLetter)
        cobineIteration-=1
    return  strx

symbols=['~','`','!','@','#','$','%',"^","&","*","(",")","?"]
list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("select you choice")
userInput=int(input("1.Password is alphanumeric or 2.Password is alphanumeric + symbols {1,2}: "))
rangeOfPassword=int(input("Enter range of password *length should be greater than 5 or less than 20*:"))
if userInput==1:
    Ans=alphanumeric(list,rangeOfPassword)
    print(Ans)
else:
    print(alphanumericSymbols(list,symbols,rangeOfPassword))

