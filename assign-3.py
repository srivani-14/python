class ShoppingCart:
    def __init__(self):
        self.items = {} 

    def add_item(self, item_name, price):
        self.items[item_name] = price  

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name] 
        else:
            print(f"{item_name} not in ShoppingCart")

    def total_price(self):
        total_price = sum(self.items.values())  
        return total_price
my_cart = ShoppingCart()
my_cart.add_item("jeans", 1500)
my_cart.add_item("tee", 700)
my_cart.add_item("shirt", 800)
print("Total price:", my_cart.total_price())
my_cart.remove_item("saree")



class Bank:
    def __init__(self):
        self.balance = 0
        print("the account is created")
    def deposit(self):
        amount = float(input("enter the amount to be deposit:"))
        self.balance=self.balance+amount
        print ("deposit is successfull and the balance in the account is %f:" %self.balance)
    def withdraw(self):
        amount =float(input("enter the amount to withdraw:"))
        if (self.balance>= amount):
         self.balance = self.balance - amount
         print("the withdraw is successful and the remaing balanxe is %f: " %self.balance)
        else:
          print("insufficient balance") 
    def balance_enquiry(self)  :
       print("balance in the account is %f"% self.balance)    
account=Bank()  
account .deposit() 
account.withdraw()
account.balance_enquiry()
