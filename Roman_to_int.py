def roman():
    symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    s="IV"
    val=0
    
    for i in range(len(s)):
        if i < len(s)-1 and symbols[s[i]]<symbols[s[i+1]]:
            # print(symbols[i])
            # if s.startswith(("V","X","L","C","D","M")):

                val-=symbols[s[i]]
        else:
                val+=symbols[s[i]]
    return val
res=roman()
print(res)
# roman()
        
