name=open("name.txt","r")

lines=name.readlines()

""" list=[]
for i in lines:
    a=""
    for j in range (len(i)):
        if i[j]!="\n":
            a=a+i[j]
    list.append(a)
print(list) """


name.close()

list1=[]
for line in lines:
    list1.append(line.replace("\n",""))
print(list1)

