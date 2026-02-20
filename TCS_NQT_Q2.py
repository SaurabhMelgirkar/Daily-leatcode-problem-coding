# # In the Kingdom of Arithmoria, a ritual staircase has n glowing steps. The first step emits energy 1, the
# # second 2, the third 3, and so on.
# # To activate the royal beacon, the total cumulative energy of all n steps must be calculated.
# # However, due to time constraints, the calculation must be performed in constant time.
# # Compute the total energy emitted by the stairc
# ample Test Cases
# Case 1
# Input:
# n = 1
# Output:
# 1
# Case 2
# Input:
# n = 5
# Output:
# 15
# Case 3 (Large Constraint)
# Input:
# n = 1000000000
# Output:
# 500000000500000000




def activate_becon(n):
    count=0
    for i in range(n+1):
       count+=i
    return count
res=activate_becon(1000000000)
print(res)