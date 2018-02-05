# top 2 scores

number = int(input("Number of students: "))
students = {}
scores = []

for i in range (number):
    name = str(input("Name of student: "))
    score = int(input("Score of student: "))
    if score in students:
        students[score].append(name)
    else:
        students[score] = []
        students[score].append(name)
    scores.append(score)
scores.sort()
highest = students[scores[len(scores)-1]]
x = len(highest)
second = students[scores[len(scores)-(x+1)]]
print ("Student with highest score: {0}".format(' and '.join(highest)))
print ("Student with second highest score: {0}".format(' and '.join(second)))
                        

                                        
                       
