""" Create a program that takes two tuples, each containing three elements. Your task is to swap the first and last elements of the first tuple with the second and third elements of the 
second tuple, and vice versa. Return the new tuples. """

def remplir():
    # Get individual elements from the user
    element1 = input("Enter the first element: ")
    element2 = input("Enter the second element: ")
    element3 = input("Enter the third element: ")
    tuple1= (element1, element2, element3)
    return(tuple1)
tuple1=()
tuple2=()
tuple1=remplir()
tuple2=remplir()
print(tuple1)
print(tuple2)
list=[]
list.append(tuple2[0])
list.append(tuple1[1])
list.append(tuple2[2])
list1=[]
list1.append(tuple1[0])
list1.append(tuple2[1])
list1.append(tuple1[2])
tuple2=tuple(list1)
tuple1=tuple(list)
print(tuple1)
print(tuple2)