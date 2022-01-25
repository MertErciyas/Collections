from random import randint

eminem = ['rood','orange','groen','blauw','geel','bruin']
eminemBag = []

def bagOfEminem(amountEminem):
    for i in range(amountEminem): 
        eminemBag.append(eminem[randint(0,len(eminem)-1)])
    print(*eminemBag,sep=', ')

ask = int(input("-------------------------------\nHow many Eminems would you like?\n-------------------------------\n"))
bagOfEminem(ask) 