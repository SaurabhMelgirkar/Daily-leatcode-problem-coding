# # Q1.
# # In the intergalactic archive of Planet Xyphor, two ancient data crystals a[] and b[] store encrypted
# # energy signatures. Due to cosmic duplication anomalies, many signatures may repeat within and
# # across the crystals.
# # The Galactic Council must compute the total number of distinct energy signatures present when
# # both crystals are merged into a unified repository.
# # If a signature appears multiple times, it must be counted only once.
# # Your task is to determine the number of unique energy signatures after combining both arrays.

# Case 1
# Input:
# a[] = [1, 2, 3, 4, 5]
# b[] = [1, 2, 3]
# Output:
# 5
# Case 2
# Input:
# a[] = [85, 25, 1, 32, 54, 6]
# b[] = [85, 2]
# Output:
# 7
# Case 3
# Input:
# a[] = [1, 2, 1, 1, 2]
# b[] = [2, 2, 1, 2, 1]
# Output:

def encrypt(a,b):
    c=[]
    for i in a:
        c.append(i)
        for j in b:
            if j not in c:
                c.append(j)
    return c
res=encrypt([1,2,3],[1,6])
print(len(res))
