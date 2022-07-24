if __name__ == '__main__':
  students_list = []
  for _ in range(int(input())):
      name = input()
      score = float(input())
      score = [name, score]
      students_list.append(score)
  new_list = [i[1] for i in students_list]
  new_list = list(set(new_list)).sort()
  print(students_list[1][0])
  print(students_list[2][0])