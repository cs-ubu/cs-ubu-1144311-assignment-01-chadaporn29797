def readm(fname='A.csv'):
    f = open('A.csv', 'r')  
    A = []
    for line in f.readlines():
        A.append( [ float(a) for a in line.strip().split(',') ] )
    f.close()
    return A

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