import xlwings as xw


app = xw.App(visible=True, add_book=False)
for i in range(10):
    work = app.books.add()
    work.save(f'C:\\Users\\赵鑫杰\\Desktop\\python\\批量处理工作簿\\file\\test{i}.xlsx')
    work.close()
app.quit()
