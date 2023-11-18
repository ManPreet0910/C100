class Student(object):
    def __init__(self, name, age, gender, level, grades = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}
    
    def set_grade(self, course, grade):
        self.grades[course] = grade
    
    def get_grade(self, course):
        return self.grades[course]
    
    def get_GPA(self):
        return sum(self.grades.values())/len(self.grades)
    
student1 = Student("manpreet", 15, "male", 10, {"math":4.5/5})
print(student1.set_grade("maths", 80))