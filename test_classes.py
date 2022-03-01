from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values
print('-----ar1------')
ar1 = Arithmetic(40,20)
print(ar1.add())

print('-----ar2------')
ar2 = Arithmetic(2,5)
print(ar2.multiply())
print(ar2.divide())
ar2.print_self()

print('-----ar3------')
ar3 = Arithmetic(15,35)
print(ar3.remainder())
ar3.print_self()

print('-----ar4------')
ar4 = Arithmetic(100,34)
print(ar4.add())
print(ar4.subtract())
print(ar4.multiply())
print(ar4.divide())
ar4.print_self()

print('-----bonus------')
print(ar1.add()+ar4.subtract())
print(ar2.remainder()+ar3.divide())