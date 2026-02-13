# s="FizzBuzz"
# l1=[]
# n=3
# for i in range(n):
#     if i%3==0:
#         print("Fizz")
#         l1.append("Fizz")
#     elif i%5==0:
#         print("Buzz")
#         l1.append()
#     else:
#         print(i)
#         l1.append(str(i))

# print(l1)

s = "FizzBuzz"
l1 = []
n = 3

for i in range(1, n + 1):
    if i % 3 == 0:
        l1.append("Fizz")
    elif i % 5 == 0:
        l1.append("Buzz")
    else:
        l1.append(str(i))

print(l1)
