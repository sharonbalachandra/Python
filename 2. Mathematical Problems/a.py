# Question: For a given list of integers, sum up all the even numbers and multiply all the odd numbers

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For each number, divide by 2. If the result is a whole number, then the number is even. If not, then the number is odd.

list_of_even_numbers = []
list_of_odd_numbers = []

for item in list_of_numbers:
    # The word "item" can be anything e.g. "x", "blah", etc.
    if item % 2 == 0:
        # print("The number is even")
        list_of_even_numbers.append(item)
    else:
        # print("The number is odd")
        list_of_odd_numbers.append(item)
    
print(list_of_even_numbers)
print(list_of_odd_numbers)

# EVEN NUMBERS
# Long but mathematically pleasing way
sum_of_even_numbers = 0
for i in list_of_even_numbers:
    sum_of_even_numbers += i
    # Same as writing sum_of_even_numbers = sum_of_even_numbers + i
print(sum_of_even_numbers)

# The Python way aka the easy way
print(sum(list_of_even_numbers))

# ODD NUMBERS
multiplication_total_of_odd_numbers = 1
for x in list_of_odd_numbers:
    multiplication_total_of_odd_numbers *= x
    # Same as writing multiplication_total_of_odd_numbers = multiplication_total_of_odd_numbers * x
print(multiplication_total_of_odd_numbers)
