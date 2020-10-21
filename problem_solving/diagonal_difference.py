
def diagonal_difference(arr, n):
    first_diagonal = 0
    for i in range(n):
        first_diagonal += arr[i][i]

    second_diagonal = 0
    for j in range(n):
        second_diagonal += arr[j][n - (j + 1)]

    return abs(first_diagonal - second_diagonal)


if __name__ == "__main__":
    print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 3))
