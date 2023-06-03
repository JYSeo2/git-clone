List = [1,2,3,'happy']
print(List[0])
print(List[3])

#list is and ordered sequence of objects the can be of any type
#lists are like arrays

#Data structure it's a way for us to organize information and data into a folder or a cupboard or a box


#List slicing
Dream = [
    'happy',
     'love',
     'peace',
     'adventure']

print(Dream)

print(Dream[0:3])

Dream_alter = Dream[0:3]
print(Dream_alter) # this is much more simpler than upper one


#copying versus modifying the list
Dream_new = Dream[:] 
Dream_new[0]='sure'
print(Dream_new)
print(Dream)

Dream_mew = Dream # the value of Dream_mew is whatever is in the memory of Dream
Dream_mew[0]='sure'
print(Dream_mew)
print(Dream)