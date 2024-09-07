
# total_n=int(input().strip())
# numbers=[]
# for i in range(total_n):
#     number=int(input().strip())
#     numbers.append(number)
# print(numbers)
# output=[]
# for n in numbers:
#     if n%7==0:
#         output.append(n)
#     else:
#         nlast=n%10
#         n=n-nlast
#         for i in range(10):
#             if n%7==0:
#                 output.append(n)
#                 break
#             n+=1
# for outs in output:
#     print(outs)

def make_divisible_by_7(n):
    # If n is already divisible by 7, return n
    if n % 7 == 0:
        return n
    # Otherwise, modify n by the minimum amount to make it divisible by 7
    else:
        # Find the nearest number to n that is divisible by 7
        remainder = n % 7
        if n % 10 + (7 - remainder) <= 9:  # Adding (7 - remainder) keeps it a single digit change
            return n + (7 - remainder)
        else:
            return n - remainder

# Input processing
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())
    print(make_divisible_by_7(n))
