n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    student_marks[name] = marks
    
query_name = input()
scores = student_marks[query_name]
total_score = sum(scores)
number_of_scores = len(scores)
average_score = total_score / number_of_scores
print(f"{average_score:.2f}")