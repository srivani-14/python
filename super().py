class P:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")

class C(P):
    def __init__(self, name,age, gender):
        super().__init__(name)  
        self.age = age
        self.gender = gender
    def display(self):
        super().display()  # Call the parent class's display method
        print(f"Age: {self.age}, gender: {self.gender}")


c1 = C("Sri", 22, "female")
c1.display()