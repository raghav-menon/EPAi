# Raghav Menon
# raghav.menon@capgemini.com

Changed the following in the tests

README_CONTENT_CHECK_FOR = [
    "odd_it",
    "authenticate",
    "logger",
    "timed",
    "decorator_factory"
]
 As we are only chceking for expalination of these functions

and

session4 to session8 in line 47 & in line 54 of test_session8.py

and

import re was added

Decorators
-----------

A decorator is a design pattern that allows to add a new functionality in python. The new functionality is added to the function without altering the properties of the 
object. Decorators are called beforethe definition of the function that is to be decorated. Decorators are very powerful and useful tool in Python since it allows programmers 
to modify the behavior of function or class. Decorators allow to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. 

Assignment Questions
---------------------

Write separate decorators that:
1. allows a function to run only on odd seconds
2. log
3. authenticate
4. timed (n times)
5. Provides privilege access to a class that has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)

1. odd seconds (odd_it):
------------------------
In odd_it function, we use a nested function where the inner function executes the decorated function only if the current second is odd. The statement

# if datetime.now().second % 2 != 0:

checks whether the current second is odd. If odd the function is executed and the result is sent back. If the current second is even then 'None' is returned.
This nested function called 'odd_it' can be used to decorate any function using @odd_it and then defining the function from the next line. When executed, the 
function executes only during the odd seconds. In order to get the details of the function passed rather than the inner function we use

# @wraps(fn)

2. log Function (logger):
-------------------------
Logger function is used to decorate any function and print out the details of the function. When a function is decorated with this the following details regarding
the function are printed out:
1. Function Name
    # print("The function_name is: ", fn.__name__)
2. Date and time when the function was called
    # print(f"The function {fn.__name__} was called at:", datetime.now())
3. Time required to execute the function. Here we first take the current time and then execute the function and then calculate the difference between the current 
   time and time stored
    # start = perf_counter()
    # result = fn(*args, **kwargs)
    # print("Execution time:", perf_counter() - start)
4. Doc string of the function
   # print("Function description:", fn.__doc__) 
5. Details of the function arguments
   # print("Function annotation:", fn.__annotations__)

Such a decorator can be used to decorate any functions whose details have to be logged while execution of the function.

3. authenticate:
----------------
The authenticate decorator is used to protect a function with password. The function will be executed only if the function is
called with the right password. Otherwise it would raise an incorrect password error.

4. timed (n times):
-------------------
This is an implementation of decorator factory.A decorator factory is just a callable that produces the actual decorator. 
It is used to make it possible to 'configure' a decorator. This is commonly achieved by nesting the decorator inside another function, 
and using the arguments of that new outer function to adjust the behaviour of the decorator returned.

In this 'timed' decorator, we sent the number of times the decorated function has to be executed though the arguments of the outer most
decorator. Whe the 'Timed' decorator, decorates a function, it returns the total and the average time taken to execute the function 'n'
times. We embed the function between the start and the current time variables and go on accumulating the time using

# total_elapsed += (perf_counter() - start)

and after executing 'n' times we find the average using:

# avg_elapsed = total_elapsed / n

5. Access Rights (decorator_factory):
-------------------------------------
This is another example of decorator factory function. The function itself is called decorator_factory. The access rights of the person is passed
through this decorator_factory which in turn configures the decorator. In this case there are 4 variables. The access rights are given as follows:

1. high --> if this is the access right, then all the four variables can be accessed
2. medium --> In case of this access right, only three variables are accessible 
3. low ---> In case the function is decorated with this access right, only two variables are accessible
4. no ---> In case the function is decorated with this access right, only one variable is accessible 
5. any other string --> if the function is decorated with any other string then it would return 'Improper access keyword'



