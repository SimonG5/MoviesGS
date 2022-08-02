import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

rawMapping = []
mapping = {}

with open('datasets/movies.dat', 'r', encoding="UTF8") as f:
    rawMapping = f.readlines()

for line in rawMapping:
    format = line.split("::")
    mapping[format[0]] = format[1].rstrip()

ratings = []

with open('datasets/ratings.dat', 'r', encoding="UTF8") as f:
    ratings = f.readlines()

origin = "891"
target = "1"
dataOuter = []


for i in range(0, 1131):
    target = str(i+1)
    print(target)
    firstRatings = []
    secondRatings = []
    if target != origin:
        for j in range(0, len(ratings)):
            format = ratings[j].split("::")
            if format[1] == origin:
                for k in range(j+1, len(ratings)):
                    formatTwo = ratings[k].split("::")
                    if format[0] != formatTwo[0]:
                        break
                    if formatTwo[1] == target:
                        firstRatings.append(float(format[2].rstrip()))
                        secondRatings.append(float(formatTwo[2].rstrip()))

                for k in range(j-1, 0, -1):
                    formatTwo = ratings[k].split("::")
                    if format[0] != formatTwo[0]:
                        break
                    if formatTwo[1] == target:
                        firstRatings.append(float(format[2].rstrip()))
                        secondRatings.append(float(formatTwo[2].rstrip()))

    if len(firstRatings) >= 10:
        A = np.array(firstRatings)
        B = np.array(secondRatings)
        cosine = np.dot(A, B)/((norm(A))*norm(B))
        dataOuter.append(cosine)
    else:
        dataOuter.append(0.0)


# Random 2D points to make scatter plot
#x = [np.random.random() for i in range(len(dataOuter))]
#y = [np.random.random() for i in range(len(dataOuter))]

#fig = plt.figure(figsize=(20, 8))
#ax = plt.subplot(111)

print(mapping[str(np.argmax(dataOuter))])

# print(data)
