import openpyxl

# 打开Excel文件
file_path = '预处理后文件数据.xlsx'
wb = openpyxl.load_workbook(file_path)

# 选择第一个sheet
sheet = wb.active

# 定义映射关系
mapping = {
    'D. 没有改善': 2,
    'B. 很大': 4,
    'C.一般': 3,
    'D. 努力不够': 2,
    'E. 完全没有': 1
}

# 遍历第13列到第22列，并进行替换
for col in range(1, 100):  # 列索引从1开始，所以是第13列到第22列
    column_letter = openpyxl.utils.get_column_letter(col)
    for cell in sheet[column_letter]:
        if cell.value in mapping:
            cell.value = mapping[cell.value]

# 保存修改后的Excel文件
wb.save(file_path)

print("替换完成并保存到原始文件。")
