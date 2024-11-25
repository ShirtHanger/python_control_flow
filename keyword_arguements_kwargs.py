""" Keyword arguments - (kwargs) """

""" 
This is a different style of passing arguments that isn’t possible in JavaScript.

These are arguments that have a name. You can provide as many as you like to a function when you call it.

As we’ve seen, we can pass positional arguments to a function:
"""

def make_employee(role):
    print(role)
    # prints: CEO

    employee = {"role": role}
    return employee

print(make_employee("CEO"))
# prints: { 'role': 'CEO' }

""" But we can pass keyword arguments to a function as well: """

print(make_employee(role="CEO"))
# prints: { 'role': 'CEO' }

""" 
If you’d like to access a varying number of keyword arguments, 
use **kwargs at the end of the parameter list. 
This is similar to how we passed an arbitrary number of positional arguments with *args.
kwargs are not positional! You can provide them in any order, but they must come after any positional arguments.
"""

def make_employee(role, **kwargs):
    print(kwargs)
    # prints: {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
    print(type(kwargs))
    # prints: <class 'dict'>
    # kwargs is a DICTIONARY - you can use it anywhere you'd use one:
    employee = {"role": role, "name": kwargs}
    return employee

print(make_employee("CEO", first="Sam", middle="Harris", last="Altman"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }

""" 
As you can see above, in a function, kwargs can be accessed by its name - kwargs.
kwargs is a dictionary, meaning you can treat it as such. 
For example, you could iterate through it using the values() method:
"""


def make_employee(role, **kwargs):
    username = ""
    for name in kwargs.values():
        username += name

    employee = {"role": role, "username": username}
    return employee

print(make_employee("CEO", first="Sam", middle="Harris", last="Altman"))


# Let's combine these ideas in the same function

print(make_employee(role="CEO", first="Sam", middle="Harris", last="Altman"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }

# We can even profile the 'Role' out of order

print(make_employee(first="Sam", middle="Harris", last="Altman", role="CEO"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }


""" 
Required positional, optional positional (*args), and keyword (**kwargs) arguments can all be used simultaneously.

But note that order is important! Check out this example:
"""

def arg_demo(pos1, pos2, *args, **kwargs):
    print(f'Positional params: {pos1}, {pos2}')
    print('*args:')
    for arg in args:
        print(' ', arg)
    print('**kwargs:')
    for keyword, value in kwargs.items():
        print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')

""" Prints:
Positional params: A, B
*args:
  1
  2
  3
**kwargs:
  color: purple
  shape: circle
"""