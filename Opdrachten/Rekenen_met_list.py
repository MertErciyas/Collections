listOne = ['1','2','3','4','5','6','7','8','9','10']
listTwo = ['2','4','6','8','10','12','14','16','18','20']

# This will add
def addAndDisplayList (listOne, listTwo):
    results= []
    for i in range (len(listOne)):
        results.append(int(listOne[i]) + int(listTwo[i]))
    return results

print("--------------")

for i in range(len(listOne)):
    print(f'{listOne[i]:>2} + {listTwo[i]:>2} = {addAndDisplayList(listOne, listTwo)[i]}')

print("--------------")

# This will substract
def substractAndDisplayLists (listOne, listTwo):
    results2= []
    for i in range (len(listOne)):
        results2.append(int(listOne[i]) - int(listTwo[i]))
    return results2

for i in range(len(listOne)):
    print(f'{listOne[i]:>2} - {listTwo[i]:>2} = {substractAndDisplayLists(listOne, listTwo)[i]}')

print("--------------")

# This will make it multiply
def multiplyAndDisplayLists (listOne, listTwo):
    results3= []
    for i in range (len(listOne)):
        results3.append(int(listOne[i]) * int(listTwo[i]))
    return results3

for i in range(len(listOne)):
    print(f'{listOne[i]:>2} * {listTwo[i]:>2} = {multiplyAndDisplayLists(listOne, listTwo)[i]}')

print("--------------")

def divideAndDisplayLists (listOne, list2):
    results4= []
    for i in range (len(listOne)):
        results4.append(int(listOne[i]) / int(listTwo[i]))
    return results4

for i in range(len(listOne)):
    print(f'{listOne[i]:>2} / {listTwo[i]:.2} = {divideAndDisplayLists(listOne, listTwo)[i]}')

print("--------------")