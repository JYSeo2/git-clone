from bankaccount_pre import BankAccount

acc1 = BankAccount()
print(type(acc1))

print(acc1.number)      #outside the class, we can access attributes using the name of object
print(acc1.holder)
print(acc1.balance)

acc2 = BankAccount()
print(acc2.number)
print(acc2.holder)
print(acc2.balance)