class Student:
    # same for every instance of the class
    college="ABC University"

    def __init__(self, name, age):
        # unique to each instance
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    

if __name__ == "__main__":
    student = Student("Alice", 22)
    print(student.greet())