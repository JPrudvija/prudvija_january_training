#Question 4
def remove_even(numbers):
    # Create a new list containing only odd numbers
    result = []
    for n in numbers:
        if n % 2 != 0:
            result.append(n)
    # In previous code when an element is removed,sometimes the next element is skipped due to iteration, which gives wrong output 
    #so we created new list called result and stored the values for correct output
    return result
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_even(nums))