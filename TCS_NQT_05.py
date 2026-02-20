# #  Solution 1
# def Sum_of_cube(s,e):
#     sum=0
#     for i in range(s,e+1):
#         sum+=i*i*i
#     return sum

# res=Sum_of_cube(1,3)
# print(res)

s,e=map(int,input().split())
cube_sum=sum(i**3 for i in range(s,e+1))
print(cube_sum)