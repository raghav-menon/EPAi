from functools import wraps
from datetime import datetime
from time import perf_counter

# Decorator that allows to run a function only at odd seconds
# else prints out "We're even!"


def odd_it(fn):
    '''Decorator allowing the incoming function 'fn' to only run in \
        odd seconds \
        input : function \
        output : Executed result if the function goes in at the odd second \
            else none '''
    @wraps(fn)
    def inner(*args, **kwargs):
        # Checking the current system time. It takes the seconds and checks
        # whether even or odd
        if datetime.now().second % 2 != 0:
            # return the executed Function value if the seconds is odd
            return fn(*args, **kwargs)
        else:
            # return None if the seconds is even
            return None
    return inner

# The same logger that we coded in the class
# it will be tested against a function that will be sent 2 parameters, and
# it would return some random string.


def logger(fn):
    '''Logger Decorator to log the details like function name, date and time \
    when the function is executed, time taken for function execution, \
    function description function parameters \
    Function result is returned as the output'''
    @wraps(fn)
    def inner(*args, **kwargs):
        # printing when the function was executed and its name
        print(f"The function {fn.__name__} was called at:", datetime.now())
        # printing the function name
        print("The function_name is: ", fn.__name__)
        # Assigning the time to current value to calculate the time taken
        # for execution
        start = perf_counter()
        # Returning the result after function execution
        result = fn(*args, **kwargs)
        # printing the time taken for execution
        print("Execution time:", perf_counter() - start)
        # printing the document for the function
        print("Function description:", fn.__doc__)
        # printing the function parameters
        print("Function annotation:", fn.__annotations__)
        return result
    return inner

# start with a decorator_factory that takes an argument one of these strings,
# high, mid, low or no
# then write the decorator that has 4 free variables
# based on the argument set by the factory call,
# give access to 4, 3, 2 or 1 arguments
# to the function being decorated from var1, var2, var3, var4
# YOU CAN ONLY REPLACE "#potentially missing code" LINES WITH MULTIPLE LINES
# BELOW KEEP THE REST OF THE CODE SAME


def decorator_factory(access: str):
    '''Decorator factory for providing access rights to variables \
        var1, var2, var3, var4. All four variables would be accessable if \
            access is 'high', 3 variables if access is 'mid', 2 variable if \
                access is 'low', 1 variable if access is 'no' and returns \
                    'improper access keyword set' if any other string is \
                        passed \
                '''
    def decorator(fn):
        var1 = 10
        var2 = 20
        var3 = 30
        var4 = 40
        def inner(*args, **kwargs):
            if access == 'high':
                return [var1, var2, var3, var4]
            elif access == 'mid':
                return [var1, var2, var3]
            elif access == 'low':
                return [var1, var2]
            elif access == 'no':
                return [var1]
            else:
                return "Improper access keyword set"
        return inner
    return decorator


# The authenticate function. Start with a dec_factory that sets the password.
# It's inner will not be called with "password", *args, **kwargs on the fn


def authenticate(set_password):
    '''A decorator factory which is used to set the password and authenticate \
        the passowrd passed through a function. If the password is right \
            it executes the function otherwise it returns wrong password
        '''
    passWord = set_password

    def auth(fn):

        @wraps(fn)
        def inner(password, *args, **kwargs):
            nonlocal passWord
            if password == passWord:
                return fn(*args, **kwargs)
            else:
                return 'Wrong Password'
        return inner
    return auth


# The timing function


def timed(reps):
    ''' The timed function is the decorator factory for the other inner \
    functions. It helps us to send in parameters via the decorator \
    input: Number of times the function has to be executed 'reps' '''
    def decorator(fn):
        '''This is the decorator function which calculates the total and
        average time required for an input function to be executed for 'reps'
        times
        input: Function
        Output: Function output 'reps' times'''
        @wraps(fn)
        def inner(*args, **kwargs):
            '''Closure Function which takes in the function arguments and \
            executes the input function'''
            total_elapsed = 0
            for rep in range(reps):
                # Counter start time
                start = perf_counter()
                # Calling Function
                fn(*args, **kwargs)
                # Calculating total elapsed time
                total_elapsed += (perf_counter() - start)
            # finding Average time
            avg_elapsed = total_elapsed / reps
            # Printing Average time for executing function for 'reps' times
            print('Avg Run time: {0:.6f}s({1} reps)'.format(avg_elapsed, reps))
            # Printing total elapsed time for executing function for 'reps'
            # times
            print('Total time:{0:.6f}s ({1} reps)'.format(total_elapsed, reps))
        return inner
    return decorator
