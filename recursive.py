def add_one(num):

    if(num>=9):
        return num + 1
    
    total=num + 1
    print("Current total:", total)
    return add_one(total)
    #function to recursively add one to a number until it reaches 9

result = add_one(5)
print("Final result:", result)  # Output: Final result: 10