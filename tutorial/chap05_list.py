matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(matrix)

print("="*100)

print([row for row in matrix])

print("="*100)

print([row[0] for row in matrix])
print([row[1] for row in matrix])
print([row[2] for row in matrix])
print([row[3] for row in matrix])

print("="*100)

print([[row[i] for row in matrix] for i in range(4)])

print("="*100)

print(list(zip(*matrix)))
