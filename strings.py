#1)
print(type("hi there"))
usename = 'supercoder'
pssword = 'supersecret'
long_string = '''
WoW
O O
---
'''
print(long_string)

#2)
first_name = 'Andrei'
last_name = 'Neagoie'
full_name = first_name + ' ' + last_name
print(full_name)

#3) string concatenation
print('hello' + 'Anderei')
#wrong case print('hello' + 5)


#4) type conversion
a = str(100)
b = int(a)
c = type(b)
print(c)
#both is equal
print(type(int(str(100))))

#5 Escape Sequence
weather = "'It's kind of sunny'" #want to highlight later part -> "" or use esacpe sequence \ : letting what comes after become string
weather_2 = "\t it\'s \\ \"kind of\" sunny \n hope you hve a good day!" #\t tab \n new line
print(weather_2)