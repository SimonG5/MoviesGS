import csv
import json
from sklearn.impute import KNNImputer
import numpy as np

averageRatings = {}

with open('datasets/averageRatings.json') as d:
    averageRatings = json.load(d)

ratings = []

with open('datasets/ratings.dat', 'r', encoding="UTF8") as f:
    ratings = f.readlines()


rateCounter = 0
lastUserId = "1"
users = np.zeros(shape=(11431, 1130))


for i in range(0, len(ratings)):

    if rateCounter > 0:
        rateCounter -= 1
        continue

    print(i)

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

    user = 0

    for j in range(i, i+rateCounter):
        format = ratings[j].split("::")
        user = int(format[0]) - 1
        users[int(format[0]) - 1, int(format[1]) -
              1] = float(format[2].rstrip())
        temp[int(format[1]) - 1] = format[2].rstrip()

    for k in range(1, 1131):
        if temp[k-1] == "-1":
            users[user, k-1] = np.nan
            temp[k-1] = averageRatings[str(k)].rstrip()


imputer = KNNImputer(n_neighbors=10)
imputer.fit_transform(users)
print(users)


with open("final.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(users)
