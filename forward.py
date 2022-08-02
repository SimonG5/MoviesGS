from csv import reader
import json
import numpy as np
from numpy import genfromtxt
from numpy.linalg import norm

averageRatings = {}
rawMapping = []
mapping = {}

with open('datasets/movies.dat','r',encoding="UTF8") as f:
    rawMapping = f.readlines()

for line in rawMapping:
    format = line.split("::")
    mapping[format[0]] = format[1].rstrip()

with open('datasets/averageRatings.json') as d:
    averageRatings = json.load(d)

userRating = []

for i in range(0, 1130):
    userRating.append(float(averageRatings[str(i+1)]))

userRating[689] = 9.5
userRating[901] = 9.0
userRating[483] = 8.5
userRating[891] = 9.0


userNp = np.array(userRating)

users = genfromtxt('datasets/users.csv', delimiter=',')
bestCos = 0
bestIndex = -1

for i in range(0, len(users)):
    userDNp = np.array(users[i])
    cosine = np.dot(userNp, userDNp)/(norm(userNp)*norm(userDNp))
    print(cosine)
    if cosine > bestCos:
        bestCos = cosine
        bestIndex = i


userBest = np.array(users[bestIndex])
print("Matching user is " + str(bestIndex+1) + " with a simmilarity of " + str(bestCos))

for i in range(0,len(userBest)):
    if str(userBest[i]) != averageRatings[str(i+1)]:
        print(mapping[str(i+1)] + " = " + str(userBest[i]))


#maxElement = np.amax(arr)
