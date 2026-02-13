# what is data
# what is algorithem
# space complexity- comprehensiom 
# time complexity- worst ,  ,best 
'''
def liner_search(l,key):
    for i in range(0,len(l)):
        if l[i]==key:
            return i
print(liner_search([1,2,3,4,5],3))
'''
'''
step1-create one fun and pass list and key as parameyer
steop2-run for loop between the range of 0 to len(l)
check key is present or not
if present prenit the index position at which it is present

'''
'''
def binary_search(l,key):
    least_i=0
    highest_i=len(l)-1
    while least_i<=highest_i:
        mid=(least_i +highest_i)//2
    if key==l[mid]:
        return mid
    elif key <l[mid]:
        highest_i=mid-1
    elif key >l[mid]:
        least_i=mid+1
print(binary_search([10,20,30,40,50,60,70],key=50) )
        
'''


    
