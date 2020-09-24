'''
This script demonstrates function calls and structure
'''

import numpy as np

def main(task,A=None):
    '''
    If no matrix A is passed in, this function will print one of several 5x5
    matrices depending on the string passed in to type:
    - task='diag': I + a matrix of ones on the sub and super diagonal
    - task='corners': I + a matrix of ones on the corners
    - task='mult5': I*5
    If a matrix A is passed in, I is replaced with A and the size of the output
    matrix is dependent on A. A must be square.
    '''

    # Never use a mutable object as a default value! If you want a mutable object
    #   to be the default value for a function argument, set the default to "None"
    #   and then check for it as is done below.
    if A is None:
        A = np.eye(5)
    else:
        # If we're not using the default, make sure the user provided matrix is square
        assert A.shape[0]==A.shape[1], "The provided matrix must be square."

    # Check the value of task and call the appropriate function, printing the output
    #   If a string that is not recognized is passed, throw an error to stop execution.
    if task == 'diag':
        print(diag_func(A))
    elif task == 'corners':
        print(corners_func(A))
    elif task == 'mult5':
        print(mult5_func(A))
    else:
        raise RuntimeError("Task not defined.")


def diag_func(mat):
    '''Add a matrix of ones on the sub and super diagonal'''

    return mat + np.diag(np.ones(mat.shape[0]-1),1) + np.diag(np.ones(mat.shape[0]-1),-1)


def corners_func(mat):
    '''Add 1 to each corner of the matrix'''

    newmat = np.array(mat) # get a copy so we are not overwriting mat
    # since it's only four values that need changing, loop over them.
    for r in [0,-1]:
        for c in [0,-1]:
            newmat[r,c] += 1 # shorthand for newmat[r,c] = newmat[r,c] + 1
    return newmat


def mult5_func(mat):
    '''Multiply the matrix by 5'''

    return mat*5


if __name__ == "__main__":
    # If run from the command line, print the default 'diag' result
    main('diag')