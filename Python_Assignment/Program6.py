# Accept input from the user
input_str = input("Enter a sequence of comma-separated numbers: ")

# Split the input string into a list of numbers
number_list = input_str.split(',')

# Convert the list of numbers to a tuple
number_tuple = tuple(number_list)

# Print the list and tuple
print("List:", number_list)
print("Tuple:", number_tuple)
