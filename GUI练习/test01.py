import tkinter

main = tkinter.Tk()

main.title("Hello")
windows = tkinter.Frame(main,bd=2,bg="yellow")

windows.pack(padx=5, pady=5)

text = tkinter.Label(windows,text="qiaoyang")
text.pack()
main.mainloop()
