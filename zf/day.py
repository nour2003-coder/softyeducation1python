try:
    with open("pets.txt","r") as name:
        content=name.read()
        print(content)
except (FileNotFoundError,FileExistsError):
    print("it doesn't exist")

#lazem ki nhot path fil windows nhot \
#ama nhot 9balha r bich ye9bilha 
# becanse python maya9bilch character \