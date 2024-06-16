# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)

# Example usage:
print(max_num(3, 5, 1))  # Output: 5


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
    result = 1
    for num in list:
        result = result * num
    return result

# Example usage:
print(mult_list([1, 2, 3, 4]))  # Output: 24


# Write a Python function called rev_string() to reverse a string.
def rev_string(s):
    return s[::-1]

# Example usage:
print(rev_string("hello"))  # Output: "olleh"


# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(x, start, end):
    return start <= x <= end

# Example usage:
print(num_within(9, 5, 14))  # Output: True


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    for row in triangle:
        print(row)

# Example usage:
pascal(5)
