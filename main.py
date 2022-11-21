import tkinter as tk
button = [9,8,7,"+",6,5,4,"-",3,2,1,"*","A/C",0,"=","/"]
def create():
    windows = tk.Tk()
    windows.title("Calculator")
    for i in range(16):
        newbutton = tk.Button(text=button[i])
        print(int(i /4))
        newbutton.grid(column=round(i % 4), row=int(i / 4))
    windows.mainloop()


if __name__ == '__main__':
    create()
    print("hello")

