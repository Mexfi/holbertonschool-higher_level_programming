#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

# Test 1: Create an instance of MyList
my_list = MyList()
print("Test 1: Create an empty list")
print(my_list)  # Expected: []

# Test 2: Append some values and print the list
my_list.append(1)
my_list.append(4)
my_list.append(2)
print("Test 2: Append some values")
print(my_list)  # Expected: [1, 4, 2]

# Test 3: Print sorted list
print("Test 3: Print sorted list")
my_list.print_sorted()  # Expected: [1, 2, 4]

# Test 4: Print the original list again (should be unchanged)
print("Test 4: Print original list again")
print(my_list)  # Expected: [1, 4, 2]

# Test 5: Append more values and print sorted
my_list.append(3)
my_list.append(5)
print("Test 5: Append more values")
print(my_list)  # Expected: [1, 4, 2, 3, 5]
my_list.print_sorted()  # Expected: [1, 2, 3, 4, 5]

# Test 6: Test with negative values
print("Test 6: Test with negative values")
my_list.append(-1)
my_list.append(-3)
my_list.print_sorted()  # Expected: [-3, -1, 1, 2, 3, 4, 5]

# Test 7: Test with empty list
print("Test 7: Test with empty list")
empty_list = MyList()
empty_list.print_sorted()  # Expected: []
