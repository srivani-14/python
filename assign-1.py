def find_numbers():
   
    for number in range(2000, 3201):
        
        if number % 7 == 0 and number %5!=0: 
            print(number,end=",")


find_numbers()






"""def squares(n):
    
   new__dict = {}
   for i in range(1, n + 1):
    new__dict[i] = i *i
   return  new__dict
n = 10
new_dict = squares(n)
print(new_dict)"""


# Accept comma-separated numbers from the console
"""string=input("enter the sequence of numbers")
new_list=string.split()
new_tuple=tuple(new_list)
print(new_list)
print(new_tuple)"""


 # Initialize counters for letters and digits
'''input_string = input("Enter a sentence: ")
letters_count = 0
digits_count = 0
for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1
print(f"LETTERS {letters_count}")
print(f"DIGITS {digits_count}")'''



#NO OF IUPPERCASE AND LOWER CASE LETTERS
"""s=input("enter your text")
u=0
l=0
for i in s:
    if i.isupper():
      u=u+1
    elif i.islower():
        l=l+1
print(" the number of uppercase letter{} and the number of lower case letter{}".format(u,l))
                 
                 """

"""#sorting them alphabeticall
words = ["abhi", "sunny", "laddu", "manu"]
sorted_words = sorted(words)

print(sorted_words)
"""
# Creating a dictionary with keys from 1 to 20 and values as their squares
'''new_dict={}
for i in range(1, 21):  
    new_dict[i]={i*i}
print(new_dict)'''



   

#print last 5 squares
"""def print_last_five_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i**2)
    print("The last 5 elements are:", squares[-5:])
print_last_five_squares()"""



 #input username and password to register
"""username=input("enter your username")
password=input("enter your password")
        
if len(password)>12 or len(password)<6:
    print("maximum length of password :12 and minimum length :6")
else:
    print("great")
if password.isalnum()==password or password.upper()==password or password.lower()==password:
        print("password must have 1(a-z),1(A-Z),1(0-9),1([$#@])")
elif password.isalnum()==password and password.upper()==password or password.lower()==password:
            print("password must have 1(a-z),1(A-Z),1(0-9),1([$#@])")  
elif password.isalnum()==password and password.upper()==password and password.lower()==password:
        print("password must have 1(a-z),1(A-Z),1(0-9),1([$#@])")
    
else:
 print("password is strong")"""




