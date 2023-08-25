""" list1=[1,2,3,3,3,2,4]
set1=set()
max=0
for i in list1:
    set1.add(i)
    s=0
    for j in list1:
        if(i==j):
            s+=1
    print("the frequency of ",i,"is",s)
    if(s>max):
        max=s

print(set1)
print("maximum of the frequency",max) """
from collections import Counter

list1 = [1, 2, 3, 3, 3, 2, 4]

counter = Counter(list1)
max_frequency = max(counter.values())

for element, frequency in counter.items():
    print(f"The frequency of {element} is {frequency}")

print(f"The set of unique elements: {set(list1)}")
print(f"The maximum frequency: {max_frequency}")