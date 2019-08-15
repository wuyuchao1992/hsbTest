import xlrd
data = xlrd.open_workbook('text.xlsx')
# table = data.sheets()[0]        # 通过索引顺序获取
# table = data.sheet_by_index(0)  # 通过索引顺序获取

table = data.sheet_by_name(u'Sheetl')   # 通过名称获取

nrows = table.nrows # 获取总行数
ncols = table.ncols # 获取总列数

# 获取一行或一列的值，参数是第几行
print(table.row_values(0)) # 获取第一行值
print(table.col_values(0)) # 获取第一列值
