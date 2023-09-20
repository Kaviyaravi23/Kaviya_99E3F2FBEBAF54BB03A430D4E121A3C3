class BankAccount:
        def __init__(self, accuont_number, account_holder_name, initial_balance=0.0):
            self.__accuont_number = accuont_number
            self.__account_holder_name = account_holder_name
            self.__account_balance = initial_balance
           
        def deposit(self, amount):
            if amount > 0 :
               self.__account_balance += amount
               print("\n Amount Deposited{}.New Balance{}:".format(amount,  self.__account_balance))
            else:
               print("Invalid deposit amount, Please Deposit a positive amount")
               
        def withdraw(self, amount):
            if amount > 0 and amount <= self.__account_balance:
               self.__account_balance -= amount 
               print("\n Withdraw amount{}.New Balance{}:".format(amount,  self.__account_balance)) 
            else:
               print("Invalid withdraw amount, Insufficient Balancet")      

# Function to display the amount
        def display_balance(self):
                print("\nAccount Balance for {} (Account #{}): {}".format(self.__account_holder_name, self.__accuont_number, self.__account_balance)) 

# creating an object of class
Account = BankAccount(accuont_number = "1111111",account_holder_name = "Kaviya",initial_balance = 5000.0)
  
# Calling functions with that class object
Account.display_balance()
Account.deposit(500.0)
Account.withdraw(200.0)
Account.display_balance()