import numpy as np

# Part 1

data = np.loadtxt('input.txt')
list1, list2 = (np.sort(data[:, 0]), np.sort(data[:, 1]))
dist = np.linalg.norm(list1 - list2, 1)

print('The total distance is:', int(dist))

# Part 2

score = 0
for i in range(len(list1)):
    score += len(np.argwhere(list2 == list1[i]))*list1[i]

print('The total similarity score is:', int(score))