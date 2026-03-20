class Student:
    def AddStudent(self):
        self.rollno = int(input("Enter Rollno: "))       
        self.name = input("Enter name: ")        
        self.age = int(input("Enter age: "))        
        self.gender = input("Enter gender: ")

    def DisplayStudent(self):
        print("Displaying Student Info")
        print(f"Rollno: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


# Create object
s1 = Student()

# Add and display student info
s1.AddStudent()
s1.DisplayStudent()
