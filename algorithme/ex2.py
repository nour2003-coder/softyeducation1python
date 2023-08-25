import pprint
def create_matrix():
    number_rows=int(input("donner rows: "))
    number_columns=int(input("donner columns: "))
    matrix=[]
    for i in range(number_rows):
        row=[]
        for j in range(number_columns):
            number=int(input("donner un entier : "))
            row.append(number)
        matrix.append(row)
    pprint.pprint(matrix)
create_matrix()