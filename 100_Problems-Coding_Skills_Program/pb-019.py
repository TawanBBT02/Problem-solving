def sum_matrices(matrix1:list[list[int]],matrix2:list[list[int]])-> list[list[int]]:
    result = []
    for i in range(len(matrix1)):
        sum_mat= []
        for ii in range(len(matrix1[0])):
            sum_mat.append(matrix1[i][ii] + matrix2[i][ii])
        result.append(sum_mat)
        
    return result

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix2 = [[4,3,2,1],[4,3,2,1],[4,3,2,1]]

print(sum_matrices(matrix1,matrix2))