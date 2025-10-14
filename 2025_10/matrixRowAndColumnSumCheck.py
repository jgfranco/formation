def check_sums(matrix, row_sums, column_sums):

    rows = [0 for _ in range(len(row_sums))]
    columns = [0 for _ in range(len(column_sums))]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            rows[row] += matrix[row][col]
            columns[col] += matrix[row][col]

    return row_sums == rows and column_sums == columns



print(check_sums(
  [[1, 2], [3, 4]],
  [3, 7],
  [4, 6]
), True)

print(check_sums(
  [[1, 2, 3], [4, 5, 6]],
  [6, 15],
  [5, 7, 9]
), True)

print(check_sums(
  [[1, 2], [3, 4]],
  [3, 7],
  [4, 7]
), False)

print(check_sums(
  [[1, 2], [3, 4]],
  [3, 7],
  [4, 5]
), False)
