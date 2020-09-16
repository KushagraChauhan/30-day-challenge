'''This is the first of the 30-day coding challenge'''
# Hour-glass problem - Hacker Rank
array = []

for i in range(6):
    array.append([int(x) for x in input().split()])

maxSum = -63

for i in range(4):
    for j in range(4):
        top = sum(array[i][j:j+3])
        mid = array[i+1][j+1]
        down = sum(array[i+2][j:j+3])

        finalSum = top + mid + down

        if finalSum > maxSum:
            maxSum = finalSum

print(maxSum)
