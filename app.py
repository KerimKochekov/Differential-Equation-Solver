import tkinter as tk
from tmp import ODE_GRAPH

root = tk.Tk()
def derivative(y,x): 
    x = float("{0:.5f}".format(x))
    return -(1/3*y*y)-(2/(3*x*x))
gui = ODE_GRAPH(root,derivative)
root.mainloop()