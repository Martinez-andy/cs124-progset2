# Part 1 - Daniel




# Part 2 - Andy Martinez
import numpy as np


# Optimal n values
nOpt = 1


# Adds row and column of zeros
def addZeros(m):
    row_of_zeros = np.zeros((1, m.shape[1]))  # Create a row of zeros with the same number of columns
    updated_matrix = np.vstack((m, row_of_zeros))

    # Add a column of zeros on the right
    column_of_zeros = np.zeros((m.shape[0], 1))  # Create a column of zeros with the same number of rows
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



def strasens(m1, m2):
    n = len(m1)
    
    # Once we reach base case, do normal matrix mult
    if n <= nOpt:
        return matMult(m1, m2)
    
    # Handle odd case by adding col and row of zeros
    if n % 2:
        m1 = addZeros(m1)
        m2 = addZeros(m2)
        n += 1
    
    # Otherwise, strasens algorithm
    
    # TODO: Implement algorithm
    
    return None



# Part 3 - TBD