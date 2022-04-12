import numpy as np
import matplotlib.pyplot as plt

def displayGradient(X1, Y1, DX, DY, plotTitle):
    fig, ax = plt.subplots()
    q = ax.quiver(X1, Y1, DX, DY)
    ax.set_title(plotTitle)

    # Show plot
    plt.show()
    print('end')


def displaySurfPlot():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

def F(distance, radius):
    if distance > radius:
        return 0
    elif ((0 < distance) and (distance <= radius)):
        return np.log(np.divide(radius, distance))    

if __name__ == "__main__":
    xl = np.linspace(0, 99, 100)  
    yl = np.linspace(0, 99, 100)
    X, Y = np.meshgrid(xl, yl)

    g = [25, 25]

    Gx = X
    Gy = Y

    Gx[:,:] = g[0]
    Gy[:,:] = g[1]

    C1 = abs(np.sqrt((X-Gx)**2+(Y-Gy)**2))

    DX, DY = np.gradient(C1)

    delta = 5
    dxl = np.linspace(0, delta, delta+1)  
    dyl = np.linspace(0, delta, delta+1)

    print(DX[1:delta:100])

    displayGradient(X, Y, DX[1:delta:100], DY[1:delta:100], 'Please Work')

    # z = abs(np.sqrt((mx-Gx)**2+(my-Gy)**2))

    # dx, dy = np.gradient(z)

    # delta = 5
    # X1, Y1 = np.meshgrid(x,y) 
    # displaySampledGradient(X1, Y1, dx[1:delta:-1,1:delta:-1], dy[1:delta:-1,1:delta:-1], z, 'Gradient of penalty term (object 2)','w')

    # r = 10
    # o = [10 , 10]
    # Ox = mx
    # Oy = my

    # Ox[:,:] = o[0]
    # Oy[:,:] = o[1]

    # d2 = np.sqrt( (mx - Ox)**2 + (my - Oy)**2 ); 

    # C2 =

    # plt.contourf(xa, xb, cmap = 'jet')  
    # plt.colorbar()  
    # plt.show()   

    print('end')