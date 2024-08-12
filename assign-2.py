list_numbers=[1,2,3,4,5,6,7,8,9,10]
even_number=list(filter(lambda i:i%2==0,list_numbers))
print(even_number)


my_list=[1,2,3,4,5,6,7,8,9,10]
square_elements=list(map(lambda x:x**2,my_list))
print(square_elements)

my_list= [1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,my_list))
suare_of_elemnts=list(map(lambda x:x**2,even_numbers))
print(suare_of_elemnts)


numbers= range(1,21)
even_numbers=list(filter(lambda i:i%2==0,numbers)) 
print(even_numbers)

numbers= range(1,21)
square_numbers=list(map(lambda i:i**2,numbers)) 
print(square_numbers)



class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
     return self.length * self.breadth
s1 = Rectangle(length=10, breadth=5)
print("Area of the rectangle:", s1.area())

class American:
    def __init__(self, name, age, language):
        self.name = "sri"
        self.age = 23
        self.language = "english"

    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and I speak {self.language}."

class NewYorker:
    def __init__(self, name, age, language):
        self.name = "manu"
        self.age = 20
        self.language = "english"
    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and I speak {self.language}."
s1 = American(name="sri", age=23, language="English")
print(s1.greet())
n = NewYorker(name="manu", age=20, language="English")
print(n.greet())


def compare_numbers(a, b):
    if a % 2 == 0 and b % 2 == 0:
      return  min(a, b)
    else:
        return max(a, b)
print(compare_numbers(4, 6)) 
print(compare_numbers(4, 7))   
print(compare_numbers(3, 9))

def two_letter_string(input_string):
    words = input_string.split()
    if len(words) != 2:
        print("Input string must contain atleast two words.")
        return False
    first_letter1 = words[0][0].lower()
    first_letter2 = words[1][0].lower()
    return first_letter1 == first_letter2
print(two_letter_string("h"))
print(two_letter_string("hello ben"))
print(two_letter_string("sri sree"))


def capitalize_first_and_fourth(name):
    if len(name) < 4:
        print("Name must be at least 4 characters ")
    
    name1 = list(name)
    name1[0] = name1[0].upper()
    name1[3] = name1[3].upper()
    capitalized_name = ''.join(name1)
    return capitalized_name
print(capitalize_first_and_fourth("srivani"))  
print(capitalize_first_and_fourth("sravani"))  
print(capitalize_first_and_fourth("manu")) 
#logic 2 
name=input("enter the name:")
c1=name[0].upper() + name[1]+name[2]+name[3]+name[4].upper()
print(c1)




