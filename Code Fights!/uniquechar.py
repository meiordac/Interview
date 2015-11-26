def uniquechar(word):
    num=0
    comparer=0
    for s1 in word:
        num=num+1
        comparer=num
        while comparer < len(word):
            if word[comparer] == s1:
                return False
            comparer = comparer+1
    return True

print(uniquechar("hola"))
            
        
