if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if student_marks[query_name]:
      marks_sum = 0
      for i in range(len(student_marks[query_name])):
        marks_sum = marks_sum + student_marks[query_name][i]
      average = marks_sum / len(student_marks[query_name])
      print(format(average, '.2f'))