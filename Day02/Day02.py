import numpy as np

# Part 1

def HowManySafe(list):
    N = len(list)
    unsafe = []
    safe = 0
    for i in range(N):
        report = list[i]
        sorted = np.sort(report)
        if np.all(report == sorted) or np.all(report == np.flip(sorted)):
            n = len(report) - 1
            diff = np.empty((n,))
            for j in range(n):
                diff[j] = abs(report[j+1] - report[j])
            if np.any(diff == 0) or np.any(diff > 3):
                unsafe.append(report)
            else:
                safe += 1
        else:
            unsafe.append(report)
    return safe, unsafe

reports = []
with open('input02.txt', 'r') as f:
    for row in f:
        reports.append(np.array([int(x) for x in row.split()]))
    
safe, unsafe = HowManySafe(reports)
print('The number of safe reports is:', safe)

# Part 2

N = len(unsafe)
for i in range(N):
    newsafe, _ = HowManySafe([ np.delete(unsafe[i], j) for j in range(len(unsafe[i])) ])
    safe += int(bool(newsafe))

print("The new number of safe reports is:", safe)