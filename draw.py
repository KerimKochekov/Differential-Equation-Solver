from scipy.integrate import odeint
import numpy as np
def normalize(x0,X,h):
    tmp = np.arange(x0,X,h)
    for i in range(len(tmp)):
        tmp[i] = float("{0:.5f}".format(tmp[i]))
    return tmp
def Graph(f1,x0,X,y0,derivative):
    xf = normalize(x0, X, 0.001)
    yf = odeint(derivative,y0,xf)
    f1.add_subplot(111).plot(xf,yf,color='black')

def Euler(f1,f2,f3,x0,X,y0,derivative,n,N):
    h,yy = (X-x0)/N,y0
    xf,ey = normalize(x0,X,h),[]
    yf = odeint(derivative,y0,xf)
    for xx in xf:
        ey.append(yy)
        yy = yy+h*derivative(yy,xx)
        yy = float("{0:.5f}".format(yy))
    f1.add_subplot(111).plot(xf,ey,color="red")

    er = []
    for i in range(len(yf)):
        er.append(abs(yf[i]-ey[i]))
    f2.add_subplot(111).plot(xf,er,color="red")

    xn,yn = normalize(n,N,1),[]
    for x in xn:
        h,yy,mx = (X-x0)/x,y0,0
        xf = normalize(x0,X,h)
        yf = odeint(derivative,y0,xf)
        for i in range(len(xf)):
            yy = yy+h*derivative(yy,xf[i])
            yy = float("{0:.5f}".format(yy))
            if abs(yy-yf[i]) > mx:
                mx = abs(yy-yf[i])
        yn.append(mx)
    f3.add_subplot(111).plot(xn,yn,color="red")


def Improved_Euler(f1,f2,f3,x0,X,y0,derivative,n,N):
    h,yy = (X-x0)/N,y0
    xf,ey = normalize(x0,X,h),[]
    yf = odeint(derivative,y0,xf)
    for xx in xf:
        ey.append(yy)
        k1 = derivative(yy,xx)
        k2 = derivative(yy+h*k1,xx+h)
        yy = yy+h*(k1+k2)/2
        yy = float("{0:.5f}".format(yy))
    f1.add_subplot(111).plot(xf,ey,color="blue")

    er = []
    for i in range(len(yf)):
        er.append(abs(yf[i]-ey[i]))
    f2.add_subplot(111).plot(xf,er,color="blue")
    
    xn,yn = normalize(n,N,1),[]
    for x in xn:
        h,yy,mx = (X-x0)/x,y0,0
        xf = normalize(x0,X,h)
        yf = odeint(derivative,y0,xf)
        for i in range(len(xf)):
            k1 = derivative(yy,xf[i])
            k2 = derivative(yy+h*k1,xf[i]+h)
            yy = yy+h*(k1+k2)/2
            yy = float("{0:.5f}".format(yy))
            if abs(yy-yf[i]) > mx:
                mx = abs(yy-yf[i])
        yn.append(mx)
    f3.add_subplot(111).plot(xn,yn,color="blue")

def Runge(f1,f2,f3,x0,X,y0,derivative,n,N):
    h,yy = (X-x0)/N,y0
    xf,ey = normalize(x0,X,h),[]
    yf = odeint(derivative,y0,xf)
    for xx in xf:
        ey.append(yy)
        k1 = derivative(yy,xx)
        k2 = derivative(yy+h/2*k1,xx+h/2)
        k3 = derivative(yy+h/2*k2,xx+h/2)
        k4 = derivative(yy+h*k3,xx+h)
        yy = yy+h*(k1+k2+k3+k4)/6
        yy = float("{0:.5f}".format(yy))
    f1.add_subplot(111).plot(xf,ey,color="green")

    er = []
    for i in range(len(yf)):
        er.append(abs(yf[i]-ey[i]))
    f2.add_subplot(111).plot(xf,er,color="green")

    xn,yn = normalize(n,N,1),[]
    for x in xn:
        h,yy,mx = (X-x0)/x,y0,0
        xf = normalize(x0,X,h)
        yf = odeint(derivative,y0,xf)
        for i in range(len(xf)):
            k1 = derivative(yy,xf[i])
            k2 = derivative(yy+h/2*k1,xf[i]+h/2)
            k3 = derivative(yy+h/2*k2,xf[i]+h/2)
            k4 = derivative(yy+h*k3,xf[i]+h)
            yy = float("{0:.5f}".format(yy))
            if abs(yy-yf[i]) > mx:
                mx = abs(yy-yf[i])
        yn.append(mx)
    f3.add_subplot(111).plot(xn,yn,color="green")