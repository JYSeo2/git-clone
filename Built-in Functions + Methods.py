#last class, I learned a few built in functions(actions-we take on data)
#numbers is sum of integer + float(소수) + Bolean(true or false) "https://chaelist.github.io/docs/python_basics/numbers_list_string/#numbers"
#str int float type print 

#good sentence numbers had some fucntions than we can use some built in function
#strings also has a very useful one called len

print(len('01234567')) #len count from 1 not 0


greet = 'hellloooo'
print(greet)
print(greet[:])
print(greet[0:len(greet)]) 

#A built in fucntion had the syntax of the word that has highlighted in blue, and then we
#used curly(?, 찾아보기) brackets to perform some action on a data type
#Phthon also has this iday of methods and methods are similar to functions but they owned by somtehing

quote = 'try hard unitil your heart stops'
print(quote.upper())
print(quote.capitalize())
print(quote.find('hard'))
print(quote.replace('stops','stops, then happy come'))

print(quote) #the value of quote don't change due to its immutability