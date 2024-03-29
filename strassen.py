# Part 1 - Daniel
# No code for Part 1
# Part 1 Description is in the Project Report

# Part 2 - Andy Martinez
import numpy as np
import sys


# Optimal n values
nOpt = 9


# Adds row and column of zeros, needed for odd matrices
def addZeros(m):

    row_of_zeros = np.zeros((1, m.shape[1]))  # Create a row of zeros with the same number of columns
    updated_matrix = np.vstack((m, row_of_zeros))

    # Add a column of zeros on the right
    column_of_zeros = np.zeros((updated_matrix.shape[0], 1))  # Create a column of zeros with the same number of rows
    updated_matrix = np.hstack((updated_matrix, column_of_zeros))
    
    return updated_matrix


# Normal matrix multiplication
def matMult(m1, m2):
    # Initialize result matrix with appropriate dimensions
    n = m1.shape[0]
    result = np.zeros((n, n))

    # Iterate over rows of the first matrix
    for i in range(n):
        # Iterate over columns of the second matrix
        for j in range(n):
            for k in range(n):
                result[i, j] += m1[i, k] * m2[k, j]
                
    return result



# Take a matrix as input and return 4 quadrants
def makeQuads(m):
    # Get the dimensions of the matrix
    n = m.shape[0]

    # Calculate splitting points
    mid_row = n // 2
    mid_col = n // 2
    
    # Create quadrants
    uLeft = m[:mid_row, :mid_col]
    uRight = m[:mid_row, mid_col:]
    lLeft = m[mid_row:, :mid_col]
    lRight = m[mid_row:, mid_col:]

    # Return quadrants
    return uLeft, uRight, lLeft, lRight
    
    
# Strasen's algorithm
def strassens(m1, m2):
    n = len(m1)
    
    nOpt = nOpt if sys.argv[1] == 0 else int(sys.argv[1])
    
    # Once we reach base case, do normal matrix mult
    if n <= nOpt:
        return matMult(m1, m2)
    
    isOdd = False
    # Handle odd matrix case
    if n % 2:
        isOdd = True
        m1 = addZeros(m1)
        m2 = addZeros(m2)
        n += 1
    
    # Make quadrants
    A, B, C, D = makeQuads(m1)
    E, F, G, H = makeQuads(m2)
    
    # Calculate p values from lecture slides
    p1 = strassens(A, (F - H))
    p2 = strassens((A + B), H)
    p3 = strassens((C + D), E)
    p4 = strassens(D, (G - E))
    p5 = strassens((A + D), (E + H))
    p6 = strassens((B - D), (G + H))
    p7 = strassens((C - A), (E + F))
    
    m = np.vstack((
        np.hstack((-p2 + p4 + p5 + p6, p1 + p2)),
        np.hstack((p3 + p4, p1 - p3 + p5 + p7))
    ))    
    
    if isOdd:
        m = m[:-1, :-1]
        
    return m
    

def getMats(d):
    # Open given file
    with open(sys.argv[3], "r") as file:  
        ms = [[], []]
        
        # Iterate over ms list
        for i in range(2):
           for _ in range(d):
               # Add a new row
               ms[i].append([])
               for _ in range(d):
                   # Add the new number entry into slot
                   ms[i][-1].append(int(file.readline()))         
        
        return np.matrix(ms[0]), np.matrix(ms[1]) 


def main():
    # Get dimensions of matrices
    d = int(sys.argv[2])
    
    # Turn input file into matrices
    m1, m2 = getMats(d)

    # Multiply both matrices
    m = strassens(m1, m2)
    
    for i in range(d):
        print(int(m[i, i]))
            
main()
# part 3 moved to part3.py
