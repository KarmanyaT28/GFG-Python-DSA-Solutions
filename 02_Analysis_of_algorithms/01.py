# sum of first n natural numbers

# Iterative approach

def sum_of_numbers(n):
    total_sum = 0 # Changed name from 'sum' to avoid shadowing built-in function
    if n <= 0:
        return 0
    else:
        # Use range(1, n + 1) to include the number n itself
        for i in range(1, n + 1):
            total_sum = total_sum + i
        return total_sum

n = int(input("Enter a number: "))
result = sum_of_numbers(n)
print(f"The sum is: {result}")


# Recursive approach

