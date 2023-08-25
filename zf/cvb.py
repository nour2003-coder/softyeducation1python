def vowels(s):
    l=["a","e","u","i","o","y"]
    k=0
    for j in range(len(s)):
         for i in l:
            if(s[j]==i):
                k+=1
    return(k)
s=input("donner")
k=vowels(s)
print(k)