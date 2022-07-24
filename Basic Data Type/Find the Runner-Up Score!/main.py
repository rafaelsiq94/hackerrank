if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    array = list(arr)
    array = list(set(array))
    array.sort(reverse=True)
    if len(array) > 1:
      print(array[1])
    else:
      print(array[0])