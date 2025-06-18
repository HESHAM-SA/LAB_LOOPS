# ## Bonus

# Sum of Even Numbers
# Write a Python program that prompts the user for a positive integer `n`, and then calculates the sum of all even numbers between 1 and `n`, inclusive.
# Your program should use a loop (either a `for` loop or a `while` loop) to iterate over the numbers between 1 and `n`, and only add the even numbers to the sum.

user_number = int(input('Enter a positive integer:'))
sum_even_number = 0
for i in range(user_number + 1):
    if i % 2 == 0:
        sum_even_number += i
        print(i)

print(f'Enter a positive integer:{user_number}')
print(f'The sum of even numbers between 1 and {user_number} is {sum_even_number}.')