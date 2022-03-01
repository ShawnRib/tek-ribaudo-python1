import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print("Introduction with mix of default args")
introduction_with_mix_of_default_args('Kyle')

print('Product of two num')
print('5+2='+str(product_of_two_num(5,2)))

print('Add all numbs: 5 + 2 + 6 + 3')
print(add_all_nums(5,2,6,3))

print('double 5')
print(double(5))

print('fib 10')
print(fib(10))

print('subtract 5-3')
print(subtract(5,3))

print('Palindrome function')
print('Check bob')
print(check_palindrome('bob'))
print('Check Jose')
print(check_palindrome('Jose'))