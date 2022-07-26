import os

def diagonalDifference(arr):
    x = 0
    y = n-1
    y2 = 0
    soma1 = 0
    soma2 = 0
    left_to_right = []
    right_to_left = []
    while x <= y:
      left_to_right.append(arr[x][x])
      x += 1
    while y >= 0:
      right_to_left.append(arr[y2][y])
      y -= 1
      y2 += 1
    for i in range(len(left_to_right)):
      soma1 += left_to_right[i]
      soma2 += right_to_left[i]
    return abs(soma1-soma2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
