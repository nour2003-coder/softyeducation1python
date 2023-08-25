def factoriel(n):
    if(n==0):
        return 1
    return(n*factoriel(n-1))
n=int(input("donner: "))
p=factoriel(n)
print(p)