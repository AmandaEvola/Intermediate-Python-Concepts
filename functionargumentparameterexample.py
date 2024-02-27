# Positional Arguments: 
def greet(name, message):
    print(f"Hello, {name}! {message}")

greet("Alice", "How are you?")

# Positional arguments in Python are arguments passed to a function or method based on their position or order in the function's parameter list. When you call a function and provide arguments without explicitly naming the parameters, Python matches the arguments to the parameters in the function definition based on their position.

# Keyword Arguments: 
greet(message="How are you?", name="Bob")

# Keyword arguments in Python are arguments passed to a function or method with explicitly specifying the parameter names along with their values. Unlike positional arguments, where the order of arguments matters, keyword arguments are identified by the parameter names they are associated with, allowing for more flexibility and clarity in function calls.

# Default Parameter Values: 
def greet(name, message="How are you?"):
    print(f"Hello, {name}! {message}")

greet("Charlie") # Output: Hello, Charlie! How are you?

# Default parameter values in Python are values assigned to function parameters that are used as a fallback when the function is called without providing a value for those parameters. They allow you to define functions with optional arguments, where the caller can choose to provide values for some parameters while relying on the default values for others. Default parameter values are helpful for providing flexibility in function definitions. They allow you to define functions with sensible default behavior while still allowing callers to customize the behavior by providing their own values for certain parameters when necessary.

# Arbitrary Number Of Arguments:
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

# An arbitrary number of arguments, also known as variable-length argument lists, allows a function to accept an indefinite number of arguments. In Python, you can define functions that accept such arguments using two special syntaxes: *args and **kwargs (args stands for arguments and kwargs stands for keyword arguments).

# These are Function and Argument Parameter Types in Python