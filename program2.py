# s="apple cat bat atom elephant vijay"
# s_splitted=s.split(" ")
# print(s_splitted)
# 
# for no in range(1,len(s_splitted)):
    # for i in range(0,len(s_splitted)-no):
        # if s_splitted[i]>s_splitted[i+1]:
            # s_splitted[i],s_splitted[i+1]=s_splitted[i+1],s_splitted[i]
# print(s_splitted)




# mru = [7,5,3,1,9]
# for i in range(0, len(mru)-1):
    # if mru[i] > mru[i+1]:   
        # mru[i], mru[i+1] = mru[i+1], mru[i] 
# print(mru)

"""selection sorting ---  it wil sort one one time
selection sorting is a sorting algorrithem where
the the element presebt inside the collection will get sorted 
by considering its minimum position

in thos swaping of values takes place only once in a complete pass

Alogorithem-
consider a list collection to be sorted

initilize a variable with assumed minnimum position

compare the values with assumed min position if it is greater change the min position value
at least swap the values 

"""
l=[3,4,5,6,7]
min=0
for i in range(1,len(l)):
    if l[min]>l[i]:
        min=i
    l[min],l[0]=l[0],l[min]
    l[0],l[4]=l[4],l[0]
print(l)
    
