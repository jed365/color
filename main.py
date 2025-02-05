from itertools import product
import numpy as np


def generate_all_arrays(rows=3, cols=2, values=[1, 2, 3]):
  """
    生成所有可能的 3x2 二维数组，数组中的元素取自 values
    """
  all_combinations = product(values, repeat=rows * cols)  # 生成所有可能的排列组合
  arrays = [np.array(comb).reshape(rows, cols) for comb in all_combinations]
  return arrays


def check_color_array(color_array, rows, cols):
  for i in range(rows):
    for j in range(cols - 1):
      if color_array[i][j] == color_array[i][j + 1]:
        return False
  for j in range(cols):
    for i in range(rows - 1):
      if color_array[i][j] == color_array[i + 1][j]:
        return False
  return True


#define color array rows,cols
N, M = 3, 4
colors = [1, 2, 3]

check_count = 0
total_count = 0
all_arrays = generate_all_arrays(N, M, colors)
for i, array in enumerate(all_arrays):
  total_count = i + 1
  if check_color_array(array, N, M):
    check_count += 1
#print(check_count)
print(f"{check_count} of total combs {total_count}:")
