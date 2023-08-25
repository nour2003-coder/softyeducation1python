def create_matrix():
    numrow=int(input("donner le nombre de lignes : "))
    numcolu=int(input("donner le nombre de columns : "))
    matrix=[]
    for i in range (numcolu):
        row=[]
        for j in range(numrow):
            item=int(input("donner : "))
            row.append(item)
        matrix.append(row)
    return(matrix)
        
m= create_matrix()
print(m)
