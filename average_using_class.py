class Student:
    def __init__(self,new_name,new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        average = sum(self.grades) / len(self.grades)
        return average

student_one = Student('raj',[60,89,90,89])
student_two = Student('rajesh',[100,100,100,100])

print(student_one.__class__)
print(student_one.average())
print(student_two.average())

