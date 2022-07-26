import os

def simpleArraySum(ar):
    array_sum = 0
    for i in range(len(ar)):
        array_sum += ar[i]
    return array_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
