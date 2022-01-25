import random

colors = ['orange', 'blue', 'green', 'brown', 'red']


def getEminemList(amount: int) -> list[str]:
    return [colors[random.randrange(0, len(colors))] for _ in range(amount)]
    getEminemList.sort(reverse=True)


def getEminemDict(amount: int) -> dict[str, int]:
    dictionary = {}

    for i in range(amount):
        randomIndex = random.randrange(0, len(colors))
        color = colors[randomIndex]

        if color in dictionary:
            dictionary[color] += 1
        else:
            dictionary[color] = 1

    return dictionary

def sortMMS(collection):
    return sorted(collection)
if __name__ == '__main__':
    print(getEminemList(int(input('How many Eminems\'s do you want?\n'))))
    print(getEminemDict(int(input('How many Eminems\'s do you want?\n')))) 