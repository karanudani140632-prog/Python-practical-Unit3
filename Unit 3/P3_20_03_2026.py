class Student:
    college_name = "Marwadi University"   

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("College:", Student.college_name)

    def update_marks(self, new_marks):
        self.marks = new_marks

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name


s1 = Student("Karan", 85)
s2 = Student("Deep", 90)


s1.display()
s2.display()

s1.update_marks(95)
print("\nAfter updating marks:")
s1.display()

Student.change_college("GLS University")

print("\nAfter changing college name:")
s1.display()
s2.display()
