"""Write a function to return the sum of digits of a number, n"""

n = int(input("Enter the number :"))

def sumation(n):
    digi_sum = 0
    while(n>0):
        last_dig = n%10
        digi_sum = digi_sum + last_dig
        n = int(n / 10)
    return digi_sum
ans = sumation(n)
print("Sum of digits of given numbers is :", ans)

# def digit_sum(n):
#     total = 0
#     while n > 0:
#         last_dig = n % 10
#         total = total + last_dig
#         n = n // 10
#     return total

# n = int(input("Enter the number : "))
# ans = digit_sum(n)
# print("Sum of digits :", ans)
