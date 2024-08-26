
#public access
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
c1 = A("manu", 22)
print(c1)
print(c1.display()) 

#protected access
class A:
    def __init__(self, name, age):
        self._name = name 
        self._age = age    
    def _display(self):
        return f"Name: {self._name}, Age: {self._age}"  

class B(A): 
    def _display2(self):
      return f"Name: {self._name}, Age: {self._age}"  
  

c1 = B("manu", 22) 
print(c1._display())

#private access
class A:
    def __init__(self, name, age):
        self.__name = name  
        self.__age = age   
    
    def __display(self):
        return f"Name: {self.__name}, Age: {self.__age}" 
class B(A):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def public_display(self):
        return f"Name: {self._A__name}, Age: {self._A__age}, Gender: {self.gender}"
    

c1 = B("Srivani", 22, "male")
print(c1)
print(c1.public_display())
