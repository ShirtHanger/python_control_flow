# Here's how to define a function in Python, and pass in parameters
    
def print_banner():
    print("=======================")
    print("Insert banner text here")
    print("=======================")

print_banner()

# You CANNOT hoist functions from the bottom of page in python. But you can import them from 
# Other files, you already know how though

""" 
Lambda functions 

Like arrow functions in JavaScript:

* They implicitly return a single expression’s result.
* They can be assigned to a variable.
* However, they cannot have any code blocks - only a single expression with its result implicitly returned.

For example, in JavaScript, we might have something that looks like this:
const nums = [1, 3, 2, 6, 5];
let odds = nums.filter(num => num % 2);

This same behavior and functionality could be duplicated in Python:
"""

nums = [1, 3, 2, 6, 5]
odds = list(filter(lambda num: num % 2, nums))

# Lambda functions are useful when using Python functions such as map(), just like how arrow functions are when using JavaScript’s array iterator methods.
# https://realpython.com/python-lambda/
# https://docs.python.org/3/reference/expressions.html#lambda