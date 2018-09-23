from tkinter import *



class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(230, 10, 1000, 160,
                                outline="#fb0", fill="#FF9912")
        canvas.create_rectangle(230, 160, 1000, 310,
                                outline="#f50", fill="white")
        canvas.create_rectangle(230, 310, 1000,460,
                                outline="#66CD00", fill="#66CD00")
        canvas.create_rectangle(200, 0, 230, 900,
                                outline="#9C661F", fill="#9C661F")
        canvas.pack(fill=BOTH, expand=1)
        canvas.create_oval(540, 160, 690, 310, outline="#0000FF",
                           fill="white", width=2)

        canvas.create_line(540, 235, 690, 235, fill="#0000FF")
        canvas.create_line(615, 160, 615, 310, fill="#0000FF")
        canvas.create_line(577, 272, 653, 198, fill="#0000FF")
        canvas.create_line(577, 197, 653, 273, fill="#0000FF")



def main():
    root = Tk()
    ex = Example()
    root.geometry("1600x800+0+0")
    root.title("Indian Flag")
    root.mainloop()


if __name__ == '__main__':
    main()