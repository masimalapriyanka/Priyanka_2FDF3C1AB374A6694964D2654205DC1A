






class BankAccount

def__init__(self, account_number, account_holder_name,initial_balance =0.0):
  self.__account_number=account_number
  self.__account_holder_name=account_holder_name
  self.__account_balance=initial_balance
  def deposit (self, amount):
    if amount>0:
      self.__account_balance +=amount
      # self.__account_ balance = self.__account_balance + amount
print ("Deposit ₹{}. New balance: ₹{}". format (amount, self.__amount_balance))
else:
print ("Invalid deposit amount.please deposit a positive amount".)
def withdraw(self, amount):
  if amount>0and amount <= self.__amount_balance
  self.__account_balance -= amount
print ("withdraw ₹{}.New balance: ₹{}". format(amount,self.__account_balance))
else:
print("the Invalid withdrawal amount or insufficient balance".)
def display_balance(self):
  print ("Amount balance for {} (account"#{}): ₹{}". format")
         self.__account_holder_name,self.__acount_number:
  self.account_balance
  # create an instance of the Bank account class
  account=Bank Account (account_number="123456789,"account_holder_name"Hariprabu", initial_balance=5000.0)
  #test deposit and withdrawal functionality
  account.display_balance()
  # account.deposit(500.0)
  # account.withdraw(200.0)
  # account.display_balance()
  
      
      