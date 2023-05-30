#input('jayjay')
#input('secret')

#print('{username}, your password {******} is {6} letters long')

username = input('what is use username?')

password = input('what is your password?')


password_length = len(password)

hidden_password = '*' * password_length

print(f'{username}, your password {password}, is {len(password)} letters long')

print(f'{username}, your password {hidden_password}, is {password_length} letters long') #readability



