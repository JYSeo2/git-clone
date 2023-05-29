#formatted strings

name = 'Andrew'
age = 55

print('hi  ' +name + '. my age is  ' + str(age) + '  years old')

print(f'hi {name} . my age is  {age}  years old')

print('hi {} . my age is  {}  years old'.format('Andrew', '55'))

print('hi {} . my age is  {}  years old'.format(name, age))

print('hi {1} . my age is  {0}  years old'.format(name, age))

print('hi {new_name} . my age is  {age}  years old'.format(new_name='sally', age=100))