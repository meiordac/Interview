def correct_parentheses(seq):
    s = []
    index=0
    if len(seq)%2!=0:
        return False
    while index<len(seq):
        c=seq[index]
        if c=="(" or c=="[":
            s.append(c)
        else:
            if len(s)==0:
                return False
            o=s.pop()
            if o=="(" and c=="]" or o=="[" and c==")" :
                return False
        index+=1
    return True
    
                
                
print(correct_parentheses("([)]"))
