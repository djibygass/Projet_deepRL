import numpy as np


def generate_rotations(matrix):
    """
    Generate all unique rotations of a given matrix.
    """
    rotations = [matrix]
    for _ in range(3):
        matrix = np.rot90(matrix)
        rotations.append(matrix.tolist())
    return rotations


def is_duplicate(matrix, existing_matrices):
    """
    Check if a given matrix or any of its rotations exist in the set of existing matrices.
    """
    for rotation in generate_rotations(matrix):
        if rotation in existing_matrices:
            return True
    return False


# # Test the functions
# test_matrix = [
#     [0, 1, 0],
#     [0, 1, 1],
#     [0, 1, 0]
# ]
# existing_matrices = [
#     [
#         [0, 1, 0],
#         [1, 1, 0],
#         [0, 1, 0]
#     ],
#     [
#         [0, 0, 1],
#         [1, 1, 1],
#         [0, 0, 1]
#     ]
# ]
#
# print(is_duplicate(test_matrix, existing_matrices))
