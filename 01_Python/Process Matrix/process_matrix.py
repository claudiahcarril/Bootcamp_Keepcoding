from functools import reduce

def process_matrix(matrix):
  """
  Receives a matrix of numbers as a parameter and returns another,
  with the same size and number of elements.
  """
  if matrix == [] or matrix == [[]]: 
    return('Sorry! Your matrix is empty')
  elif is_numerical_matrix(matrix):
    return _process_matrix(matrix)
  else:
    return('Sorry! Your matrix is not valid')


def is_numerical_matrix(matrix):
    """
    Receives the matrix to process and verify. Returns True only if matrix is correct
    (matrix is a list of lists, all sublists have the same size and there is only numbers)
    """
    result = True
    for column in matrix:
        if type(matrix) != list:
            result = False
            break
        elif len(column) != len(matrix[0]):
            result = False
            break
        for element in column:
            if type(element) != int:
                result = False
                break
    
    return result

def _process_matrix(matrix):
    """
    Receives a verified matrix of numbers as a parameter and returns another,
    with the same size and number of elements.
    """    
    processed_matrix = []
    if len(matrix) == 1:
        processed_matrix = matrix
    else:
        for i, column in enumerate(matrix):
            new_matrix = []
            for index, value in enumerate(column):
                new_value = process_element(i, index, matrix)
                new_matrix.append(new_value)
            processed_matrix.append(new_matrix)
    
    return processed_matrix           
    

def process_element(i, index, matrix):   
    """
    Get the index of the column, the index of the element and
    computes its average with its neighbors and returns that average
    """  
    values = get_neighbours(i, index, matrix)
    avr = get_average(values)
    return avr


def get_neighbours(i, index, matrix):
    """
    Receive an array of indices and return a list of values of the filtered neighbors.
    The element itself is included.
    """
    new_matrix = [
            [i, index],
            [i, index - 1],
            [i, index + 1],
            [i - 1, index],
            [i + 1, index],
        ]
    filtered = list(filter(lambda i: i[0] > -1 and i[0] < len(matrix) and i[1] > -1 and i[1] < len(matrix[0]), new_matrix))
    
    values = []
    for a, b in filtered:
        values.append(matrix[a][b])
    return values


def get_average(values):
    """
    Receive a list of numbers and return their average
    """
    return reduce(lambda x, y: x + y, values, 0) / len(values)



test_matrix_1 = [[2, 4, 6, 8], [1, 3, 5, 7], [8, 10, 12, 14], [7, 9, 11, 13]]
test_matrix_2 = [[2,4],[3,5]]
test_matrix_3 = [[1,3,5], [2,4,6], [7,9,11], [8,10,12]]
test_matrix_4 = [[1,3,5,7], [2,4,6,8], [7,9,11,13]]
test_matrix_5 = [[2, 4, 5, 2], [4, 6, 2, 3], [1, 2, 3, 4], [5, 6, 7, 8]]
test_matrix_6 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 3, 5, 7, 9], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

wrong_matrix1 = [[1,"b","c"], [1, "n", 5, 7], [8, True, 12, 14]]
wrong_matrix2 = [[1,3,5], [2,4], [7,9,11], [8,10,12]]
wrong_matrix3 = [[]]

if __name__ == "__main__":
    average_test_1 = process_matrix(test_matrix_1)
    print("Numbers Test 1: {}".format(test_matrix_1))
    print("Averages Test 1: {}".format(average_test_1))
    print("\n")
    average_test_2 = process_matrix(test_matrix_2)
    print("Numbers Test 2: {}".format(test_matrix_2))
    print("Averages Test 2: {}".format(average_test_2))
    print("\n")
    average_test_3 = process_matrix(test_matrix_3)
    print("Numbers Test 3: {}".format(test_matrix_3))
    print("Averages Test 3: {}".format(average_test_3))
    print("\n")
    average_test_4 = process_matrix(test_matrix_4)
    print("Numbers Test 4: {}".format(test_matrix_4))
    print("Averages Test 4: {}".format(average_test_4))
    print("\n")
    average_test_5 = process_matrix(test_matrix_5)
    print("Numbers Test 5: {}".format(test_matrix_5))
    print("Averages Test 5: {}".format(average_test_5))
    print("\n")
    average_test_6 = process_matrix(test_matrix_6)
    print("Numbers Test 6: {}".format(test_matrix_6))
    print("Averages Test 6: {}".format(average_test_6))
    print("\n")
    print("\n WRONG MATRIX 1: Matrix con letras y booleans")
    print(wrong_matrix1)
    print(process_matrix(wrong_matrix1))
    print("\n")
    print("\n WRONG MATRIX 2: Matrix con sublista de diferente tamaño")
    print(wrong_matrix2)
    print(process_matrix(wrong_matrix2))
    print("\n")
    print("\n WRONG MATRIX 3: Matrix es una lista")
    print(wrong_matrix3)
    print(process_matrix(wrong_matrix3))