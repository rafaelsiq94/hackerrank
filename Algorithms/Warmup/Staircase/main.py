def staircase(n):
  x = "#"
  y = ""
  for i in range(n):
    y += " "
  for i in range(n):
    y = y.replace(" ", "", 1)
    print(y+x)
    x += "#"

if __name__ == '__main__':
    n = 6

    staircase(n)