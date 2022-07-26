
def plusMinus(arr):
  positive = 0
  negative = 0
  zero = 0
  for i in range(len(arr)):
    if arr[i] == 0:
      zero += 1
    elif arr[i] > 0:
      positive += 1
    elif arr[i] < 0:
      negative += 1
  positive = "{:.6f}".format(positive/n)
  print(positive)
  negative = "{:.6f}".format(negative/n)
  print(negative)
  zero = "{:.6f}".format(zero/n)
  print(zero)

if __name__ == '__main__':
    n = 6

    arr = [3,2,1]

    plusMinus(arr)
