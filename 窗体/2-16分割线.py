from tkinter import *
from tkinter.ttk import Separator

tk = Tk()
tk.title("分割线")
my = "2022年5月26日0—24时，新增本土新冠肺炎确诊病例45例和无症状感染者219例，其中33例确诊病例为既往无症状感染者转归，12例确诊病例和219例无症状" \
     "感染者在隔离管控中发现。新增境外输入性确诊病例1例和无症状感染者6例，均在闭环管控中发现。"
other = "病例1，居住于徐汇区，病例2、病例3，居住于静安区，病例4，居住于普陀区，病例5—病例7，居住于虹口区，病例8—病例10，居住于杨浦区，病例11、病" \
        "例12，居住于闵行区，"

Label(tk, text=my, fg="blue", bg="yellow", justify="center", wraplength=170).pack(padx=10, pady=10)
Separator(tk, orient=HORIZONTAL).pack(fill=X, padx=2)
Label(tk, text=other, fg="purple", bg="green", justify="left", wraplength=170).pack(pady=10, padx=10)
mainloop()
