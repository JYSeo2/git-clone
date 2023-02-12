#Variables are ways for us to store information on our computer
#When I imput the fact that my iq is 190, I type like 'iq = 190'. In this case iq means variables. With the printf(iq), 190 is shown
#In other words, we can stor that information 190 in this variable
#varibles sometimes be called name, assigning a value is also known as binding we are binding the value 190 to this variable
#so that when we request this variable later on

#Variables rule
#1. snake_case / 2. Start with lowercase or underscore / 3. Letters, numbers, underscores / 4. case sensitive / 5. don't overwrite keywords
# https://www.w3schools.com/python/python_ref_keywords.asp keywords list
# i can reassign variables
iq = 190
user_age = iq/4

print(user_age)

#constants = never change in a program eg) PI = 3.14 -> wrong
#__ dunder don't recommend to use like this
a, b, c = 1, 2, 3
print(a,b,c)