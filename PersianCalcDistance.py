def getListOfWords(word, tokens):
    editDisArr = []
    for token in tokens:
        editDisArr.append(getEditDistance(word, token, len(word), len(token)))

    finalListOfWords = []
    counter = 0
    while counter < 10:
        index = editDisArr.index(min(editDisArr))
        finalListOfWords.append(tokens[index])
        editDisArr[index] = 500
        counter += 1

    return finalListOfWords

def getEditDistance(str1, str2, m, n):
    distance = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                distance[i][j] = j
            elif j == 0:
                distance[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(distance[i][j - 1], distance[i - 1][j], distance[i - 1][j - 1])
    return distance[m][n]

listOfTokens = []
listOfIncorrectWords = []

listOfTokensTmp = open("tokens.fa", "r", encoding="utf8")
listOfIncorrectWordsTmp = open("incorrect.fa", "r", encoding="utf8")

for str in listOfTokensTmp:
    listOfTokens.append(str.split('\n')[0])

for str in listOfIncorrectWordsTmp:
    listOfIncorrectWords.append(str.split('\n')[0])

result = open("94463104_Assignment3_Part2_FA.fa", "w+", encoding="utf-8")

for incorrectWord in listOfIncorrectWords:
    condidateWords = getListOfWords(incorrectWord, listOfTokens)
    result.write(incorrectWord + ': ')
    for condidateWord in condidateWords:
        result.write(condidateWord + ', ')
    result.write('\n')