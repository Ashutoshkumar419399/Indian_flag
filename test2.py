from tkinter import *



class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        '''canvas.create_rectangle(230, 10, 1000, 160,
                                outline="#fb0", fill="#FF9912")
        canvas.create_rectangle(230, 160, 1000, 310,
                                outline="#f50", fill="white")
        canvas.create_rectangle(230, 310, 1000,460,
                                outline="#66CD00", fill="#66CD00")
        canvas.create_rectangle(200, 0, 230, 900,
                                outline="#9C661F", fill="#9C661F")'''
        canvas.pack(fill=BOTH, expand=1)
        canvas.create_oval(540, 160, 690, 310, outline="#0000FF",
                           fill="white", width=2)
        canvas.create_oval(580, 200, 600, 220, outline="#0000FF",
                           fill="white", width=2)
        canvas.create_oval(630, 200, 650, 220, outline="#0000FF",
                           fill="white", width=2)
        coord = 600,270,630,280
        arc = canvas.create_arc(coord, start=0, extent=150, fill="red")
        canvas.create_rectangle(500, 330, 730, 500,
                                outline="#9C661F", fill="#9C661F")
        #oval = canvas.create_polygon(500, 500, 415, 600,615,500,500,600,700,700, outline="#fb0", fill="#FF9912")


        # Frock
        canvas.create_line(500, 500, 420, 650, fill="#0000FF")
        canvas.create_line(730, 500, 810, 650, fill="#0000FF")
        canvas.create_line(420, 650, 810, 650, fill="#0000FF")
        #Nose
        canvas.create_line(615, 210, 607, 255, fill="#0000FF")
        canvas.create_line(615, 210, 623, 255, fill="#0000FF")
        canvas.create_line(607, 255, 623, 255, fill="#0000FF")
        #Neck
        canvas.create_line(580, 302, 580, 332, fill="#0000FF")
        canvas.create_line(650, 302, 650, 332, fill="#0000FF")
        canvas.create_line(650, 302, 650, 332, fill="#0000FF")
        #Leg
        canvas.create_line(530, 650, 542, 750, fill="#0000FF")
        canvas.create_line(580, 650, 568, 750, fill="#0000FF")
        canvas.create_line(700, 650, 688, 750, fill="#0000FF")
        canvas.create_line(650, 650, 662, 750, fill="#0000FF")
        #foot
        canvas.create_line(542, 750, 535, 770, fill="#0000FF")
        canvas.create_line(568, 750, 573, 770, fill="#0000FF")
        canvas.create_line(688, 750, 695, 770, fill="#0000FF")
        canvas.create_line(662, 750, 657, 770, fill="#0000FF")
        canvas.create_line(535, 777, 573, 777, fill="#0000FF")
        canvas.create_line(695, 777, 657, 777, fill="#0000FF")
        canvas.create_line(535, 770, 535, 777, fill="#0000FF")
        canvas.create_line(573, 770, 573, 777, fill="#0000FF")
        canvas.create_line(695, 770, 695, 777, fill="#0000FF")
        canvas.create_line(657, 770, 657, 777, fill="#0000FF")
        #foot finger right
        canvas.create_line(669, 767, 669, 777, fill="#0000FF")
        canvas.create_line(677, 767, 677, 777, fill="#0000FF")
        canvas.create_line(684, 767, 684, 777, fill="#0000FF")
        canvas.create_line(690, 767, 690, 777, fill="#0000FF")
        # foot finger right
        canvas.create_line(561, 767, 561, 777, fill="#0000FF")
        canvas.create_line(553, 767, 553, 777, fill="#0000FF")
        canvas.create_line(546, 767, 546, 777, fill="#0000FF")
        canvas.create_line(540, 767, 540, 777, fill="#0000FF")
        # hair
        coord = 520, 140, 700, 220
        arc = canvas.create_arc(coord, start=320, extent=260, fill="black")
        #left hand frock

        canvas.create_line(500, 330, 450, 270, fill="#0000FF")
        canvas.create_line(500, 390, 450, 330, fill="#0000FF")
        canvas.create_line(450, 270, 450, 330, fill="#0000FF")
        # right hand frock
        canvas.create_line(730, 330, 780, 390, fill="#0000FF")
        canvas.create_line(730, 390, 780, 450, fill="#0000FF")
        canvas.create_line(780, 390, 780, 450, fill="#0000FF")
        #left hand
        canvas.create_line(450, 278, 438, 260, fill="#0000FF")
        canvas.create_line(450, 322, 400, 265, fill="#0000FF")
        canvas.create_line(438, 260, 510, 190, fill="#0000FF")
        canvas.create_line(400, 265, 510, 175, fill="#0000FF")
        canvas.create_oval(500, 170, 520, 200, outline="#0000FF",
                           fill="white", width=2)
        #right hand
        canvas.create_line(780, 396, 830, 453, fill="#0000FF")
        canvas.create_line(780, 440, 792, 452, fill="#0000FF")
        canvas.create_line(830, 453, 740, 500, fill="#0000FF")
        canvas.create_line(792, 452, 740, 485, fill="#0000FF")
        canvas.create_oval(722, 502, 742, 482, outline="#0000FF",
                           fill="white", width=2)








def main():
    root = Tk()
    ex = Example()
    root.geometry("1600x800+0+0")
    root.title("Indian Flag")
    root.mainloop()


if __name__ == '__main__':
    main()