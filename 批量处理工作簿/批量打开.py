import os
import xlwings as xw

file_path = 'C:\\Users\\赵鑫杰\\Desktop\\python\\批量处理工作簿\\file'
file_list = os.listdir(file_path)
app = xw.App(visible=True, add_book=False)
for i in file_list:
    if os.path.splitext(i)[1] == '.xlsx':
        app.books.open(file_path + "\\" + i)
