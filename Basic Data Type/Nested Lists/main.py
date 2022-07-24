if __name__ == '__main__':
  students_list = []
  for _ in range(int(input())):
      name = input()
      score = float(input())
      score = [name, score]
      students_list.append(score)
  new_list = [i[1] for i in students_list]
  new_list = list(set(new_list))
  new_list.sort()
  second_lowest_score = new_list[1]
  students_list.sort(key = lambda x: x[0])
  for i in range(len(students_list)):
    if students_list[i][1] == second_lowest_score:
      print(students_list[i][0])