def hello():
    print("Hello, World!")
    #function to print a greeting message

hello()    

def sum_numbers(a, b):
    if(type(a) is not int or type(b) is not int):
        return
    return a + b
    #function to return the sum of two numbers

result = sum_numbers('a', 10)
print(result)  # Output: 15 

