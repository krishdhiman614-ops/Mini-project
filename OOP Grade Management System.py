class Course:
    def __init__(self, course_name):
        self.course_name = course_name
    def display(self):
        print("Course:", self.course_name)
    def __str__(self):
        return self.course_name
class Student(Course):
    def __init__(self, name, marks, course_name):
        super().__init__(course_name)
        self.name = name
        self.marks = marks
# Polymorphism
    def display(self):
        print("\nStudent Name :", self.name)
        print("Course       :", self.course_name)
        print("Marks        :", self.marks)
    def __str__(self):
        return f"Student,{self.name},{self.marks},{self.course_name}"
class Teacher(Course):
    def __init__(self, name, subject, course_name):
        super().__init__(course_name)
        self.name = name
        self.subject = subject
    # Polymorphism
    def display(self):
        print("\nTeacher Name :", self.name)
        print("Subject      :", self.subject)
        print("Course       :", self.course_name)
    def __str__(self):
        return f"Teacher,{self.name},{self.subject},{self.course_name}"
filename = "records.txt"
def save_record(obj):
    with open(filename, "a") as file:
        file.write(str(obj) + "\n")
    print("Record Saved Successfully!")
def view_records():
    try:
        with open(filename, "r") as file:
            print("Records")
            data = file.read()
            if data:
                print(data)
            else:
                print("No Records Found.")
    except FileNotFoundError:
        print("File Not Found!")
while True:
    print("Grade Management System")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. View Records")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        course = input("Enter Course Name: ")
        s = Student(name, marks, course)
        s.display()
        save_record(s)
    elif choice == "2":
        name = input("Enter Teacher Name: ")
        subject = input("Enter Subject: ")
        course = input("Enter Course Name: ")
        t = Teacher(name, subject, course)
        t.display()
        save_record(t)
    elif choice == "3":
        view_records()
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")