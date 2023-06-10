#!!difference between _ and __

#we need  to know concept of encapsulation,
#encapsulation, it is need to restriced the attributes of object to some of function like input.


class BankAccount:
    def __init__(self, number, holder, balance=0):#Method is a function that is defined inside a class #self point to the object and we can access the attributes and methods through this parameter
                                                #In my opinion, we define self and attributes what is mentioned in upper line
                                                #Special Methods start and end double underscore or Dounder
                                                #the method of the class usually takes a parameter called "self" that represents the instance of the class it means that      
        print("A new bank account was created") 
        self.number = number                       #inside the class, we can access attributes through self parameter
        self.holder = holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        
        else:
            print("Not Enough Money")