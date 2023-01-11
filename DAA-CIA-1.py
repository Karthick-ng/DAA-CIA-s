import random as rd

char = ['a','c','g','t']
str1 = ""
str2 = ""
length = 16

counts = {'a': 0, 'c': 0, 'g': 0, 't': 0}
while len(str1) < length:
    ch = rd.choice(char)
    if counts[ch] < 4:
        str1 += ch
        counts[ch] += 1

counts = {'a': 0, 'c': 0, 'g': 0, 't': 0}
while len(str2) < length:
    ch = rd.choice(char)
    if counts[ch] < 4:
        str2 += ch
        counts[ch] += 1

print(str1)
print(len(str1))
print(str2)
print(len(str2))


import numpy as np

match = 5
mismatch = -4
gap = -1

n = len(str1) + 1
m = len(str2) + 1
matrix = np.zeros((n, m), dtype=int)

for i in range(1, n):
    matrix[i][0] = matrix[i-1][0] + gap
for j in range(1, m):
    matrix[0][j] = matrix[0][j-1] + gap

for i in range(1, n):
    for j in range(1, m):
        diagonal = matrix[i-1][j-1] + (match if str1[i-1] == str2[j-1] else mismatch)
        up = matrix[i-1][j] + gap
        left = matrix[i][j-1] + gap
        matrix[i][j] = max(diagonal, up, left)

s1_aligned = ""
s2_aligned = ""
i = n-1
j = m-1
while i > 0 or j > 0:
    if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + (match if str1[i-1] == str2[j-1] else mismatch):
        s1_aligned = str1[i-1] + s1_aligned
        s2_aligned = str2[j-1] + s2_aligned
        i -= 1
        j -= 1
    elif i > 0 and matrix[i][j] == matrix[i-1][j] + gap:
        s1_aligned = str1[i-1] + s1_aligned
        s2_aligned = "-" + s2_aligned
        i -= 1
    elif j > 0 and matrix[i][j] == matrix[i][j-1] + gap:
        s1_aligned = "-" + s1_aligned
        s2_aligned = str2[j-1] + s2_aligned
        j -= 1

score = matrix[n-1][m-1]

print(matrix)
print(s1_aligned)
print(s2_aligned)
print(score)

