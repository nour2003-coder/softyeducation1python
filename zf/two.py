#exercice 1
def remplir():
    set1=set()
    n1=int(input("give me the length of the set1"))
    i=0
    while i<n1 :
        a=int(input("donner l'element de set 1"))
        i+=1
        set1.add(a)
    return(set1)
def intersection(set1,set2):
    for i in (set1):
        for j in ((set2)):
            if j==i:
                print(i)

set1=remplir()
set2=remplir()
intersection(set1,set2)
#improved version
def input_set():
    n = int(input("Enter the number of elements in the set: "))
    my_set = set()

    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        my_set.add(element)

    return my_set

def intersection(set1, set2):
    common_elements = set1 & set2  # You can use the & operator for set intersection
    return common_elements

set1 = input_set()
set2 = input_set()
common_elements = intersection(set1, set2)

print("Common elements:", common_elements)
