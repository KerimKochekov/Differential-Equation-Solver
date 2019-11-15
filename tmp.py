from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from scipy.integrate import odeint
from PIL import ImageTk, Image
import draw

#y'=f(x,y)
#f(x,y)=-y^2/3-2/(3*x^2)

class ODE_GRAPH:
    def __init__(self, root, derivative, gui_app_title="ODE_GRAPH"):
        # internal parameters
        self.root = root
        self.update_flag = 0
        self.gui_app_geometry = "1503x600"
        self.gui_app_title = gui_app_title
        self.x0 = DoubleVar(value=1)
        self.X = DoubleVar(value=5)
        self.derivative = derivative
        self.y0 = DoubleVar(value=2)
        self.n = DoubleVar(value=10)
        self.N = DoubleVar(value=100)
        self.m1 = IntVar(0)
        self.m2 = IntVar(0)
        self.m3 = IntVar(0)

        # GUI construction
        self.root.geometry(self.gui_app_geometry)
        self.root.title(self.gui_app_title)
        self.function_graph_label = Label(self.root, text="Graph of functions of grid size N",font=("Helvetica", 15))
        self.function_graph_label.place(x=80,y = 5)

        self.f1 = Figure(figsize=(5, 5), dpi=100)
        draw.Graph(self.f1,self.x0.get(),self.X.get(),self.y0.get(),self.derivative)

        self.canvas1 = FigureCanvasTkAgg(self.f1, master=self.root)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().place(x=5,y=35)
        #----------------------------------------------------------------------------
        self.function_graph_label = Label(self.root, text="Local errors of grid size N",font=("Helvetica", 15))
        self.function_graph_label.place(x=630,y = 5)

        self.f2 = Figure(figsize=(5, 5), dpi=100)
        self.f2.clear()

        self.canvas2 = FigureCanvasTkAgg(self.f2, master=self.root) 
        self.canvas2.draw()
        self.canvas2.get_tk_widget().place(x=505,y=35)
        #---------------------------------------------------------------------------
        self.function_graph_label = Label(self.root, text="Maximum local errors of grid sizes in range(n,N)",font=("Helvetica", 15))
        self.function_graph_label.place(x=1070,y = 5)

        self.f3 = Figure(figsize=(5, 5), dpi=100)
        self.f3.clear()

        self.canvas3 = FigureCanvasTkAgg(self.f3, master=self.root) 
        self.canvas3.draw()
        self.canvas3.get_tk_widget().place(x=1000,y=35)
        #---------------------------------------------------------------------------------
        a,b=550,20
        self.mm1 = Checkbutton(self.root, text="Euler's", variable=self.m1, command=self._update_callback)
        self.mm1.place(x=950, y=a-b+5)
        self.mm2 = Checkbutton(self.root, text="Improved Euler's", variable=self.m2, command=self._update_callback)
        self.mm2.place(x=1050, y=a-b+5)
        self.mm3 = Checkbutton(self.root, text="Runge Kutte", variable=self.m3, command=self._update_callback)
        self.mm3.place(x=1200, y=a-b+5)
        #---------------------------------------------------------------------------------
        
        aa,bb,cc=50,10,55
        self.label = Label(self.root, text="y(x0)")
        self.label.place(x=aa-10, y=a)
        self.b2 = Entry(self.root, textvariable=self.y0, width=5)
        self.b2.place(x=aa-bb, y=a+b)
        aa+=cc
        self.label = Label(self.root, text="x0",font=("Helvetica", 8))
        self.label.place(x=aa, y=a)
        self.b1 = Entry(self.root, textvariable=self.x0, width=5)
        self.b1.place(x=aa-bb, y=a+b)
        aa+=cc
        self.label = Label(self.root, text="X")
        self.label.place(x=aa, y=a)
        self.b4 = Entry(self.root, textvariable=self.X, width=5)
        self.b4.place(x=aa-bb, y=a+b)
        aa+=cc
        self.label = Label(self.root, text="n")
        self.label.place(x=aa, y=a)
        self.b3 = Entry(self.root, textvariable=self.n, width=5)
        self.b3.place(x=aa-bb, y=a+b)
        aa+=cc
        self.label = Label(self.root, text="N")
        self.label.place(x=aa, y=a)
        self.b5 = Entry(self.root, textvariable=self.N, width=5)
        self.b5.place(x=aa-bb, y=a+b)
        aa+=100
        #----------------------------------------------------------------
        self.p1 = Label(self.root, text="Function")
        self.p1.place(x=aa+80, y=a-15)
        img = ImageTk.PhotoImage(Image.open("function.jpg"))
        panel = Label(root, image = img)
        panel.image = img
        panel.place(x=aa+40,y=a+5)
        #----------------------------------------------------------------
        aa+=100
        self.p2 = Label(self.root, text="General solution")
        self.p2.place(x=aa+260, y=a-37)
        img = ImageTk.PhotoImage(Image.open("general.jpg"))
        panel = Label(root, image = img)
        panel.image = img
        panel.place(x=aa+210,y=a-15)
        #----------------------------------------------------------------
        self.close_button = Button(self.root, text="Update", command=self._update_callback)
        self.close_button.place(x=1350,y=a+15)
        self.close_button = Button(self.root, text="Close", command=self._quit)
        self.close_button.place(x=1430,y=a+15)
        

    def _quit(self):
        self.root.quit() 
        self.root.destroy() 

    def _update_callback(self):
        if(self.x0.get()<=0 & 0<=self.X.get()):
            print("Interval contains discontinued point")
            return
        self.f1.clear()
        self.f2.clear()
        self.f3.clear()
        draw.Graph(self.f1,self.x0.get(),self.X.get(),self.y0.get(),self.derivative)
        if self.m1.get() == 1:
            draw.Euler(self.f1,self.f2,self.f3,self.x0.get(),self.X.get(),self.y0.get(),self.derivative,self.n.get(),self.N.get())
        if self.m2.get() == 1:
            draw.Improved_Euler(self.f1,self.f2,self.f3,self.x0.get(),self.X.get(),self.y0.get(),self.derivative,self.n.get(),self.N.get())
        if self.m3.get() == 1:
            draw.Runge(self.f1,self.f2,self.f3,self.x0.get(),self.X.get(),self.y0.get(),self.derivative,self.n.get(),self.N.get())
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()
        pass