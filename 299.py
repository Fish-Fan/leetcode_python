def getHint(secret: str, guess: str) -> str:
    secretMap = {}
    guessMap = {}

    bullCount = 0
    cowCount = 0
    for i, v in enumerate(secret):
        if v == guess[i]:
            bullCount += 1
        else:
            if secretMap.get(v) == None:
                secretMap[v] = 1
            else:
                secretMap[v] += 1
            guessChar = guess[i]
            if guessMap.get(guessChar) == None:
                guessMap[guessChar] = 1
            else:
                guessMap[guessChar] += 1

    for k, v in secretMap.items():
        if v <= guessMap.get(k):
            cowCount += v
        else:
            cowCount += guessMap.get(k)

    return str(bullCount) + 'A' + str(cowCount) + 'B'

if __name__ == '__main__':
    secret = '1123'
    guess = '0111'
    hint = getHint(secret, guess)