Python Scopes
-------------
In programming, the scope defines the area where the names, function, variables etc. can be unambiguously used or accessed. The variables or functions would only be visible and accessible by the code within its scope. In python we have 
1. Global Scope : The variable, functions etc with this scope is available throughout the code. 
2. Local Scope : The variable, function etc with this sccope is available to the code within this scope.

Thus if a variable is defined outside all the functions, then it will have a Global scope whereas if it is defined within the function it will have a local scope.

Python Scope and Namespaces
---------------------------
The concept of scopes is closely related to namespaces. Python scopes are implemented as dictionaries that map names to objects. They are stored in a special attribute called __dict__. These dictionaries are namespaces. If a module is imported and we type in the command module.__dict__.keys(), it would provide the names of the variable, functions within the module namespace. 

Whenever a name is used, such as a variable or a function name, Python searches through different scope levels (or namespaces) to determine if the name exists or not. If the name exists, then the first occurance of the name is used. If not it results in an error.

LEGB Rule
---------
Python resolves names using the LEGB rule. The letters LEGB can be expanded as follows: 

L --> Local (or function) scope is the code block or body of any Python function or lambda expression. This scope contains the names that are defined inside the function. These variable names are visible only within the function. They are created on function call and not when the function definition is encountered. This is true even if the same function is called multiple times, or recursively. Each call will result in a new local scope being created.

E --> Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. This scope contains the names that is defined in the enclosing function. The names in the enclosing scope are visible from the code of the inner and enclosing functions.

G --> Global (or module) scope is the top-most scope in a Python program, script, or module. This scope contains all of the names that is defined at the top level of a program or a module. Names in this scope are visible from everywhere within the code.

B --> Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python. Names in this Python scope are also available from everywhere in your code. It’s automatically loaded by Python when you run a program or script.

The LEGB rule is a name lookup procedure, which determines the order in which Python looks up names. Thus, if a given name is referenced, then Python will look that name up sequentially in the local, enclosing, global, and built-in scope. If the name exists, then the first occurrence of it otherwise it results in an error.

Nested Functions and Python Closures
-------------------------------------
A function defined within a function is called a Nested function. Nested functions can access variables of the enclosing functions which are said to be in the nonlocal scope.

Closure: A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created. A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.


Session 7 Assignments
----------------------

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable
2. Write a closure that gives you the next Fibonacci number
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries
