import tkinter as tk

root = tk.Tk()
root.title('Calculator')

def all_clear():
  var1.set('')
def clear():
  onetext = var1.get()
  onetext = onetext[:-1]
  var1.set(onetext)
def func(text):
  context = var1.get() + text
  var1.set(context)
def result(text):
  result = eval(text)
  all_clear()
  var1.set(result)

var1 = tk.StringVar()
label = tk.Label(root, textvariable=var1, fg='#ffffff', bg='#000000', anchor=tk.E, height=2)
label.grid(row=0, column=0, columnspan=4, sticky='EW')
#1列目
btn_c = tk.Button(root, text="C", command=clear, width=5, height=2)
btn_c.grid(row=1, column=0)
btn_ac = tk.Button(root, text="AC", command=all_clear, width=5, height=2)
btn_ac.grid(row=1, column=1)
btn_p = tk.Button(root, text = "%", command = lambda: func("%"), width = 5, height = 2)
btn_p.grid(row = 5, column = 2)
btn_add = tk.Button(root, text="+", command=lambda: func("+"), width=5, height=2)
btn_add.grid(row=1, column=3)

#2列目
btn_7 = tk.Button(root, text="7", command=lambda: func("7"), width=5, height=2)
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: func("8"), width=5, height=2)
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: func("9"), width=5, height=2)
btn_9.grid(row=2, column=2)
btn_div = tk.Button(root, text="/", command=lambda: func("/"), width=5, height=2)
btn_div.grid(row = 2, column = 3)

#３列目
btn_4 = tk.Button(root, text="4", command=lambda: func("4"), width=5, height=2)
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: func("5"), width=5, height=2)
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: func("6"), width=5, height=2)
btn_6.grid(row=3, column=2)
btn_mul = tk.Button(root, text="*", command=lambda: func("*"), width=5, height=2)
btn_mul.grid(row=3, column=3)

#４列目
btn_1 = tk.Button(root, text="1", command=lambda: func("1"), width=5, height=2)
btn_1.grid(row=4, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: func("2"), width=5, height=2)
btn_2.grid(row=4, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: func("3"), width=5, height=2)
btn_3.grid(row=4, column=2)
btn_sub = tk.Button(root, text="-", command=lambda: func("-"), width=5, height=2)
btn_sub.grid(row=4, column=3)

#５列目
btn_0 = tk.Button(root, text="0", command=lambda: func("0"), width=5, height=2)
btn_0.grid(row=5, column=0)
btn_pt = tk.Button(root, text=".", command=lambda: func("."), width=5, height=2)
btn_pt.grid(row=5, column=1)
btn_eq = tk.Button(root, text='=', command=lambda: result(var1.get()), width=5, height=2)
btn_eq.grid(row=5, column=2)
tk.mainloop()