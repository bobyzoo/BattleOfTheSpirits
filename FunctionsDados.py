import random

def dado(numeroLados=20,numDados=1):
    result = []
    for c in range(numDados):
        result.append(random.randint(1,numeroLados))
    print(result)
    return result