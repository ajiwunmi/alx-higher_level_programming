#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for i in range(len(matrix[m])):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(matrix[m][i]), end='')
        print()
