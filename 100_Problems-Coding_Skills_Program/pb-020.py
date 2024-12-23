def transpose_matrix(matrix:list[list[int]])->list[list[int]]:
    #วิธีที่ 1
    tm= []
    for i in range(len(matrix[0])):
        tt = []
        for j in range(len(matrix)):
            tt.append(matrix[j][i])
        tm.append(tt)

    #วิธีที่ 2
    transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


    return tm


matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(transpose_matrix(matrix1))