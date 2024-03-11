def multiply_numbers_in_list(numbers_list):
    # Initialize the product to 1
    product = 1
    
    # Iterate through each number in the list
    for num in numbers_list:
        # Multiply the current number with the product
        product *= num
        
    # Return the product
    return product

# Input a list of numbers from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()

# Convert each input string to an integer and store them in the list
numbers = [int(num) for num in numbers]

# Call the multiply_numbers_in_list function with the list of numbers as an argument
result = multiply_numbers_in_list(numbers)

# Print the result
print(f"The product of all the numbers in the list is: {result}")
