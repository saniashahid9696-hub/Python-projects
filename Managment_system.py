class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


class School:
    def __init__(self):
        self.students = []

    # Add student
    def add_student(self, name, roll_no, marks):
        student = Student(name, roll_no, marks)
        self.students.append(student)
        print("Student added successfully!")

    # Display students
    def display_students(self):
        if not self.students:
            print("No students available.")
            return
        
        print("\nStudent List:")
        for student in self.students:
            print(f"Name: {student.name}, Roll No: {student.roll_no}, Marks: {student.marks}")

    # Calculate average marks
    def calculate_average(self):
        if not self.students:
            print("No students available to calculate average.")
            return
        
        total = sum(student.marks for student in self.students)
        average = total / len(self.students)
        print(f"\nAverage Marks: {average:.2f}")


school = School()

school.add_student("Ali", 1, 85)
school.add_student("Sara", 2, 90)
school.add_student("Aslam", 3, 78)

school.display_students()
school.calculate_average()