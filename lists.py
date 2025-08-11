users=['dev', 'ops', 'admin']
data=['23', '45', 'devops']

print('dev' in users)  # Check if 'dev' is in the list of users
print('dev' not in users)  # Check if 'dev' is not in the list of users

print('23' in data)  # Check if '23' is in the list of data
print('devops' not in data)  # Check if 'devops' is not in the list of data

print(users[-1])  # Access the last element in the list of users
print(data[0])  # Access the first element in the list of data
print(users[1:3])  # Access elements from index 1 to 2 in the list of users
print(data[:2])  # Access elements from start to index 1 in the list of data
print(users[1:])  # Access elements from index 1 to end in the list of users
print(data[-2:])  # Access the last two elements in the list of data
print(users[:-1])  # Access all but the last element in the list of users

users.append('guest')  # Add 'guest' to the end of the list of users
print(users)  # Print the updated list of users

users.insert(1, 'superuser')  # Insert 'superuser' at index 1 in the list of users
print(users)  # Print the updated list of users
users[2:2] = ['tester', 'developer']  # Insert 'tester' and 'developer' at index 2
print(users)  # Print the updated list of users
users[1:3] = ['sysadmin']  # Replace elements at index 1 and 2 with 'sysadmin'


users.remove('dev')  # Remove 'dev' from the list of users
print(users)  # Print the updated list of users

users.pop()  # Remove the last element from the list of users
print(users)  # Print the updated list of users


users.extend(['admin', 'manager'])  # Extend the list of users with new elements
print(users)  # Print the updated list of users

users.sort()  # Sort the list of users in ascending order
users.sort(reverse=True)  # Sort the list of users in descending order
users.sort(key=len)  # Sort the list of users by length of each string
print(users)  # Print the final list of users

users.reverse()

users+=' newuser'  # Concatenate ' newuser' to the list of users

print(sorted(users,reverse=True))  # Print the sorted list of users doesnt modify the original list


#to make a copy of the list
users_copy = users.copy()  # Create a copy of the list of users
print(users_copy)  # Print the copied list of users 
myusers = users[:]  # Another way to create a copy of the list of users
myusers=list(users)  # Yet another way to create a copy of the list of users    


#Tuples - data structure that is immutable (cannot be changed after creation)
# Tuples are created using parentheses or the tuple() constructor
# They can contain mixed data types and are often used to group related data together
mytuple = tuple(('dev', 'ops', 'admin'))
another_tuple = (1,2,3,4,5,6,7,7)  # Tuple creation using parentheses
print(mytuple)
print(another_tuple)


newlist = list(mytuple)  # Convert tuple to list
print(newlist)  # Print the converted list

(one, two, *three) = another_tuple  # Unpacking tuple values into variables
print(one)  # Print the first element of the tuple
print(two)  # Print the second element of the tuple
print(three)  # Print the remaining elements of the tuple as a list

print(another_tuple.count(7))  # Count occurrences of 7 in the tuple

#add 2 lists together
list1 = reversed[1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # Concatenate two lists
print(combined_list)  # Print the combined list