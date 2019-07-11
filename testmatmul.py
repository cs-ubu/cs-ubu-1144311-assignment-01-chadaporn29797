from matmul import readm, matmul
# 1. read mt A from 'A.csv'
A = readm('A.csv')

# 2. read mt b from 'b.csv'
b = readm('b.csv')

# 3. find the result of c = A*b
def matmul(A,b):
    m, n = len(A), len(b[0])
    J = len(A[0]) # A - mxj  # b - Jxn
    if len(A[0]) == len(b):
        C = [ [0]*n for i in range(m) ]
        # A[0][0]*b[0][0] + A[0][1]*b[1][0]+ A[0][1]*b[2][0]
        for r in range(m):
            for c in range(n):
                C[r][0] = sum([ A[r][j]*b[j][0] for j in range(J) ])
        return C
    return []

# 4.print C
C = matmul(A,b)
print('----')
for row in C:
    print(row)
print('----')
