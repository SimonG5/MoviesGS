from csv import reader
import json
import numpy as np
from numpy import genfromtxt
from numpy.linalg import norm

averageRatings = {}

with open('datasets/averageRatings.json') as d:
    averageRatings = json.load(d)

userRating = []

for i in range(0, 1130):
    userRating.append(float(averageRatings[str(i+1)]))

userRating[1129] = 10
userRating[891] = 10
userRating[321] = 4
userRating[560] = 2
userRating[561] = 7

userRating[139] = 10
userRating[851] = 10
userRating[371] = 4
userRating[50] = 2
userRating[5] = 7

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

print("Matching user is " + str(i+1) + " with a simmilarity of " + str(bestCos))
