class Student:
    # same for every instance of the class
    college="ABC University"

    def __init__(self, name, age,password):
        # unique to each instance
        self.name = name
        self.age = age
        # private attribute
        self.__password=password

    def show_password(self):
        return self.__password
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    

if __name__ == "__main__":
    student = Student("Alice", 22, "mypassword123")
    print(student.greet())
    del student
    print("Student object has been deleted.")