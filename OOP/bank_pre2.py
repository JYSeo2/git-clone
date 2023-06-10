from bankaccount import BankAccount

acc1 = BankAccount(holder = "alex", number = 123)
print(type(acc1))

print(acc1.number)      #outside the class, we can access attributes using the name of object
print(acc1.holder)
print(acc1.balance)

#acc2 = BankAccount(holder = "Bob", number = 567, balance = 100) # in this case, we need some argument to the class Constructor
#print(acc2.number)
#print(acc2.holder)
#print(acc2.balance)

print(acc1.balance)
acc1.deposit(20)
print(acc1.balance)

acc1.withdraw(10)
print(acc1.balance)

acc1.withdraw(15) 
print(acc1.balance) #in previous steop, because the balance is lower than the price of withdrawing, the balance remains 10  

#So, we learned how to create simple class, how to define Constructor method, how to define objects from the class and how to acess the object's atttribute inside and outside of the class