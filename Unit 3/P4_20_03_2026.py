class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.laptop = self.Laptop()   

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        self.laptop.show()

    # Inner class
    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = "8GB"
            self.cpu = "i5"

        def show(self):
            print("Laptop Brand:", self.brand)
            print("RAM:", self.ram)
            print("CPU:", self.cpu)



s1 = Student("Karan", 101)
s1.show()
