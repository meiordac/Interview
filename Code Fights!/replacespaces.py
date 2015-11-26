def replacespace(word):
    pos=0
    newword=""
    while pos<len(word):
        print (newword)
        if word[pos]==" ":
            newword = newword+"%20"
            while pos<len(word) and word[pos]==" "  :
                pos = pos +1
        else:
            newword = newword+word[pos]
        pos = pos+1
    return newword
            

print(replacespace("Mr    John Smirth      "))
