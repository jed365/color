from itertools import product

def is_valid_row(row):
    """检查单行是否满足左右相邻颜色不同的条件"""
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            return False
    return True

def is_compatible(row1, row2):
    """检查两行是否满足上下相邻颜色不同的条件"""
    for i in range(len(row1)):
        if row1[i] == row2[i]:
            return False
    return True

def count_colorings(rows=4, cols=4, colors=3):
    """计算满足条件的填色方案总数"""
    # 生成所有可能的单行排列
    all_rows = [row for row in product(range(colors), repeat=cols) if is_valid_row(row)]

    # 动态规划数组，dp[i][row] 表示第 i 行以 row 为排列的方案数
    prev_dp = {row: 1 for row in all_rows}  # 初始第一行的方案数

    for _ in range(1, rows):
        curr_dp = {}
        for row in all_rows:
            curr_dp[row] = sum(prev_dp[prev_row] for prev_row in all_rows if is_compatible(prev_row, row))
        prev_dp = curr_dp

    return sum(prev_dp.values())

# 计算 4x4 表格的总填色方案
result = count_colorings()
print(f"Total number of colorings: {result}")
