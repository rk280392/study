my_student = { 'name' : 'raj', 'marks': [70,80,90,100]}

def avg(marks):
    marks_list = my_student['marks']
    average_marks = sum(marks_list)/len(marks_list)
    return average_marks

print(avg(my_student))
