#we need  to know concept of encapsulation,
#encapsulation, it is need to restriced the attributes of object to some of function like input.


class BankAccount_pre:
    def __init__(self):                               #Method is a function that is defined inside a class #self point to the object and we can access the attributes and methods through this parameter
                                                #Special Methods start and end double underscore or Dounder
                                                #the method of the class usually takes a parameter called "self" that represents the instance of the class it means that      
        print("A new bank account was created") 
        self.number = 123                       #inside the class, we can access attributes through self parameter
        self.holder = "Alex"
        self.balance = 0