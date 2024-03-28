# Part 1 - Daniel




# Part 2 - Andy Martinez
import numpy as np
import sys


# Optimal n values
nOpt = 1


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
    result = np.zeros((m1.shape[0], m2.shape[1]))

    # Iterate over rows of the first matrix
    for i in range(m1.shape[0]):
        # Iterate over columns of the second matrix
        for j in range(m2.shape[1]):
            # Iterate over rows of the second matrix (or columns of the first matrix)
            for k in range(m1.shape[1]):
                # Update the element at position (i, j) of the result matrix
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
def strasens(m1, m2):
    n = len(m1)
    
    # Once we reach base case, do normal matrix mult
    if n <= nOpt:
        return matMult(m1, m2)
    
    # Handle odd matrix case
    if n % 2:
        m1 = addZeros(m1)
        m2 = addZeros(m2)
        n += 1
    
    # Make quadrants
    A, B, C, D = makeQuads(m1)
    E, F, G, H = makeQuads(m2)
    
    # Calculate p values from lecture slides
    p1 = strasens(A, (F-H))
    p2 = strasens((A + B), H)
    p3 = strasens((C + B), E)
    p4 = strasens(D, (G - E))
    p5 = strasens((A + D), (E + H))
    p6 = strasens((B - D), (G + H))
    p7 = strasens((C - A), (E + F))
    
    # Merge sub problems
    return np.vstack((
        np.hstack((-p2 + p4 + p5 + p6, p1 + p2)),
        np.hstack((p3 + p4, p1 - p3 + p5 + p7))
    ))
    


def getMats(d):
    # Open given file
    with open(sys.argv[3], "r") as file:  
        ms = [[], []]
        
        # Iterate over ms list
        for i in range(2):
           for _ in range(d):
               # Add a new row
               ms[i].append([])
               for k in range(d):
                   # Add the new number entry into slot
                   ms[i][-1].append(int(file.readline()))         
        
        return np.matrix(ms[0]), np.matrix(ms[1]) 

def main():
    # Get dimensions of matrices
    d = int(sys.argv[2])
    
    # Turn input file into matrices
    m1, m2 = getMats(d)

    # Multiply both matrices
    m = strasens(m1, m2)
    
    for i in range(d):
        print(int(m[i, i]))

main()
# Part 3 - TBD