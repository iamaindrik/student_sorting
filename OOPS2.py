class Main:
    def __init__(self, roll, name, mark1, mark2, mark3):
        self.s_rollno = roll
        self.s_name = name
        self.s_marksone = mark1
        self.s_markstwo = mark2
        self.s_marksthree = mark3

    def calcavg(self):
        return (self.s_marksone + self.s_markstwo + self.s_marksthree) / 3

    def grade(self):
        avg = self.calcavg()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "D"

    def StudentInfo(self):
        return f"{self.s_rollno}-{self.s_name}"

    def StudentMarks(self):
        return f"{self.s_rollno}-{self.s_marksone}-{self.s_markstwo}-{self.s_marksthree}"


# Data Input
studentnum = int(input("Enter the number of Students: "))

students = []
for i in range(1, studentnum + 1):
    print(f"ENTER DETAILS OF STUDENT {i}")
    roll = input("Enrollment No.: ")
    name = input("Name: ")
    mark1 = int(input("Subject 1 Marks: "))
    mark2 = int(input("Subject 2 Marks: "))
    mark3 = int(input("Subject 3 Marks: "))

    student = Main(roll, name, mark1, mark2, mark3)
    students.append(student)

students.sort(key=lambda student: student.calcavg(), reverse=True)
grades = {"A": [], "B": [], "C": []}
for student in students:
    grade = student.grade()
    grades[grade].append(student)

# FILE IO
with open('StudentInfo.txt', 'w') as stuinfo:
    for student in students:
        stuinfo.write(student.StudentInfo() + '\n')

with open('StudentMarks.txt', 'w') as stumarks:
    for student in students:
        stumarks.write(student.StudentMarks() + '\n')

with open('StudentGrade.txt', 'w') as stugrade:
    for student in students:
        stugrade.write(f"{student.s_rollno}-{student.s_name}-{student.grade()}\n")
with open('A-Grade.txt', 'w') as a_grade:
    for student in grades["A"]:
        a_grade.write(student.StudentInfo() + '\n')

with open('B-Grade.txt', 'w') as b_grade:
    for student in grades["B"]:
        b_grade.write(student.StudentInfo() + '\n')

with open('C-Grade.txt', 'w') as c_grade:
    for student in grades["C"]:
        c_grade.write(student.StudentInfo() + '\n')
