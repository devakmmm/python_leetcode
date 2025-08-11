import math
#literal assignment

first='dev'
last='ops'

print(isinstance(first, str))

#constructor function

pizza=str('pepperoni')

# concatenation
fullname= first + ' ' + last
print(fullname)

#casting numbers to strings
decade=str(2020)
print(type(decade))

statement= "The decade is " + decade
print(statement)

#multiline string
multiline_string = """This is a multiline string.

         It can span multiple lines."""
print(multiline_string)

#escaping special characters

escaped_string = "This is a string with an escaped quote: \"Hello!\""
print(escaped_string)

#string methods
print(first.upper())  # Convert to uppercase
print(last.lower())   # Convert to lowercase
print(first.replace('d', 'D'))  # Replace 'd' with 'D'
print(first.startswith('d'))  # Check if it starts with 'd'
print(last.endswith('s'))      # Check if it ends with 's'
print(first.find('e'))  # Find the index of 'e' in first
print(last.split('o'))  # Split last by 'o'
print(len(fullname))     # Length of fullname

name='John Doe'
print(name.split())  # Split name into a list of words
print(name.split('h'))  # Split name by space   
print(name.title())  # Convert to title case
print(name.capitalize())  # Capitalize the first letter
print(name.strip())  # Remove leading and trailing whitespace
print(name.count('o'))  # Count occurrences of 'o'
print(name.isalpha())  # Check if all characters are alphabetic
print(name.isalnum())  # Check if all characters are alphanumeric
print(name.isdigit())  # Check if all characters are digits
print(name.islower())  # Check if all characters are lowercase
print(name.isupper())  # Check if all characters are uppercase
print(name.swapcase())  # Swap case of all characters
print(name.center(20, '*'))  # Center the string with '*' padding
print(name.ljust(20, '-'))  # Left justify with '-' padding
print(name.rjust(20, '='))  # Right justify with '=' padding    

#build a menu

title = "Main Menu".upper()
print(title.center(30, '*') + "\n")
options = ["1. Start", "2. Settings", "3. Exit"]
print("Coffee".ljust(20, '-') + "$4".rjust(3, ' '))


menu = title + "\n" + "\n".join(options)
print(menu)

#string index values
print(title[-1])  # Last character
print(title[0])   # First character
print(title[1:5])  # Characters from index 1 to 4
print(title[:5])   # Characters from start to index 4
print(title[5:])   # Characters from index 5 to end
print(title[-5:])  # Last 5 characters
print(title[:-5])  # All but the last 5 characters

# some methods that return a boolean value
print(title.isupper())
print(title.islower())
print(title.startswith("Main"))
print(title.endswith("Menu"))
print(title.isalpha())
print(title.isalnum())
print(title.isdigit())

#boolean data type
is_active = True
print(is_active)
x=bool(1)  # Convert integer to boolean
print(x)  # True, because 1 is truthy
y=bool(0)  # Convert integer to boolean
print(y)  # False, because 0 is false

#built-in functions for numbers
print(10//3)  # Integer division
print(10 % 3)  # Modulus operation
print(10 ** 2)  # Exponentiation (10 squared)
print(abs(-5))  # Absolute value of -5
print(pow(2, 3))  # 2 raised to the power of 3
print(max(1, 2, 3))  # Maximum value
print(min(1, 2, 3))  # Minimum value
print(sum([1, 2, 3]))  # Sum of a list
print(len("Hello"))  # Length of a string
print(sorted([3, 1, 2]))  # Sort a list
print(reversed([1, 2, 3]))  # Reverse a list
print(list(reversed([1, 2, 3])))  # Convert reversed object to list
print(round(3.14159))
print(abs(-10)) # Absolute value
print(round(3.14159))  # Round to nearest integer
print(round(3.14159, 1))  # Round to 1 decimal place
print(round(3.14159, 3))  # Round to 3 decimal places
print(int(3.14))  # Convert float to integer
print(float(5))  # Convert integer to float
print(complex(2, 3))  # Create a complex number
print(bin(10))  # Binary representation of 10
print(oct(10))  # Octal representation of 10
print(hex(10))  # Hexadecimal representation of 10
print(abs(-5))  # Absolute value of -5
print(min(1, 2, 3))  # Minimum value
print(max(1, 2, 3))  # Maximum value
print(sum([1, 2, 3]))  # Sum of a list
print(len([1, 2, 3]))  # Length of a list
print(sorted([3, 1, 2]))  # Sort a list
print(reversed([1, 2, 3]))  # Reverse a list
print(list(reversed([1, 2, 3])))  # Convert reversed object to list
print(round(3.14159, 2))  # Round to 2 decimal places
print(pow(2, 3))  # 2 raised to the power of 3
print(max(1, 2, 3))  # Maximum value
print(min(1, 2, 3))  # Minimum value
print(sum([1, 2, 3]))
print(len("Hello, World!"))  # Length of a string
print(sorted([3, 1, 2]))  # Sort a list
print(reversed([1, 2, 3]))  # Reverse a list
print(list(reversed([1, 2, 3])))  # Convert reversed object to list 


#math module usage

print(math.sq(4))
print(math.sqrt(16))  # Square root of 16
print(math.factorial(5))  # Factorial of 5
print(math.pi)  # Value of pi
print(math.e)  # Value of e
print(math.pow(2, 3))  # 2 raised to the power of 3
print(math.ceil(3.14))  # Round up to nearest integer
print(math.floor(3.14))  # Round down to nearest integer
print(math.sin(math.pi / 2))  # Sine of pi/2
print(math.cos(0))  # Cosine of 0
print(math.tan(math.pi / 4))  # Tangent of pi/4 


#casting strings to numbers
number_str = "42"
number_int = int(number_str)  # Convert string to integer
print(number_int)  # Output: 42

float_str = "3.14"
number_float = float(float_str)  # Convert string to float
print(number_float)  # Output: 3.14