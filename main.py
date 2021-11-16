file = open("p022_names.txt","r")
names = file.read()
file.close()
nameList = []
currentName = ''
for char in names:
    if char == '"':
        continue
    elif char == ',':
        nameList.append(currentName)
        currentName = ''
    else:
        currentName += char
nameList.append(currentName)

nameList.sort()

nameScore = {}
points = {}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
for char in letters:
    i += 1
    points[char] = i
i = 0
for name in nameList:
    score = 0
    i += 1
    for char in name:
        score += points[char]
    nameScore[name] = score * i

pprint.pprint(nameScore)

totalScore = 0
for v in nameScore.values():
    totalScore += v
print(totalScore)
