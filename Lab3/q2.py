class Student:
    def __init__(self, name, roll_no, department, address, gender, marks):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.address = address
        self.gender = gender
        self.marks = marks
        self.total_marks = sum(marks)
        self.percentage = self.total_marks / len(marks)

def get_student_details():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    department = input("Enter Department: ")
    address = input("Enter Address: ")
    gender = input("Enter Gender: ")
    marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
    return Student(name, roll_no, department, address, gender, marks)

def display_student_details(student):
    print("\nStudent Details:")
    print(f"Name: {student.name}")
    print(f"Roll No: {student.roll_no}")
    print(f"Department: {student.department}")
    print(f"Address: {student.address}")
    print(f"Gender: {student.gender}")
    print(f"Total Marks: {student.total_marks}")
    print(f"Percentage: {student.percentage:.2f}%")

def get_total_marks(student):
    return student.total_marks

def main():
    num_students = int(input("Enter the number of students: "))
    students = [get_student_details() for _ in range(num_students)]
    
    for student in students:
        display_student_details(student)
    
    max_marks_student = max(students, key=get_total_marks)
    min_marks_student = min(students, key=get_total_marks)
    failed_students = []
    for s in students:
        for m in s.marks:
            if m < 10:
                failed_students.append(s.name)
                break  # Stop checking once we find a failing mark  
                  
    print(f"\nStudent with Maximum Marks: {max_marks_student.name}")
    print(f"Student with Minimum Marks: {min_marks_student.name}")
    print(f"Failed Students: {', '.join(failed_students) if failed_students else 'None'}")

if __name__ == "__main__":
    main()
