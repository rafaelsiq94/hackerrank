def miniMaxSum(arr):
    result_list = []
    full_result = 0
    for i in range(len(arr)):
        full_result += arr[i]
    for i in range(len(arr)):
      result_list.append(full_result-arr[i])
    result_list.sort()
    print(str(result_list[0])+" "+str(+result_list[-1]))

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
