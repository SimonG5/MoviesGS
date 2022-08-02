import csv
import json

averageRatings = {}

with open('datasets/averageRatings.json') as d:
    averageRatings = json.load(d)

ratings = []

with open('datasets/ratings.dat', 'r', encoding="UTF8") as f:
    ratings = f.readlines()


rateCounter = 0
lastUserId = "1"
users = []
print(averageRatings["1"])
print(len(ratings))


for i in range(0, len(ratings)):

    if rateCounter > 0:
        rateCounter -= 1
        continue

    format = ratings[i].split("::")

    while(lastUserId == format[0]):
        rateCounter += 1
        if i + rateCounter == len(ratings):
            break
        format = ratings[i+rateCounter].split("::")

    lastUserId = format[0]
    temp = []

    for l in range(0, 1130):
        temp.append("-1")

    for j in range(i, i+rateCounter):
        format = ratings[j].split("::")
        temp[int(format[1]) - 1] = format[2].rstrip()

    for k in range(1, 1131):
        if temp[k-1] == "-1":
            temp[k-1] = averageRatings[str(k)].rstrip()

    users.append(temp)


for i in range(0, len(users)):
    print(len(users[i]))

with open("final.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(users)
