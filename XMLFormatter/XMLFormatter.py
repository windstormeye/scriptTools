# -*- coding: utf-8 -*-


from openpyxl import load_workbook
from openpyxl import Workbook

import re

# 文件名
wb = load_workbook('data.xlsx')

# 工作区
a_sheet = wb.get_sheet_by_name('工作表2')
# 获得当前正在显示的sheet, 或用wb.get_active_sheet()
sheet = wb.active

# 中文
keyArr = []
# 英文
valueArr = []

for row in sheet.rows:
    for cell in row:
        string = cell.value
        # pattern = re.compile(u"[\u4e00-\u9fa5]+")
        pattern = re.compile(u">(.*?)<")
        result = re.findall(pattern, str(string))
        for key in result:
            if key:
                keyArr.append("\"" + key + "\"")
                # print(keyArr[len(keyArr) - 1])

for cell in list(sheet.columns)[1]:
    value = cell.value
    if value != None:
        valueArr.append("\"" + value + "\"")
        # print(valueArr[len(valueArr) - 1])


index = 0
for value in valueArr:
    print(value + " = " + keyArr[index])
    index += 1

