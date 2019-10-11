import numpy as np
import matplotlib.pyplot as plt
import math

bullet_speed =  float(input("Input bullet speed(m/s): "))
height =        float(input("Input the height(metre): "))
angle =         float(input("Input the angle(Degres 0-360): "))
wind_factor =   float(input("Wind Factor(Horizontal): "))

rho = 1.22  #konstanta rho
g = 9.81    #gravitasi

A = 0.4            #luas permukaan peluru
Cd = wind_factor    #pengaruh angin terhadap peluru   
m = 4.2             # berat dari peluru

v = bullet_speed    #kec peluru
alpha = angle*3.14/180 #sudut

x = 0.      #jarak awal
y = height  #Tinggi dari tanah
vx = v * np.cos(alpha)
vy = v * np.sin(alpha)
vx_init = vx
t = 0.

X = [x]
Y = [y]

dt = 0.01

def drag(v, alpha):
    F =0.5*rho*(v**2)*A*Cd # F = gaya dari peluru terhadap anginnya
    return (F*np.cos(alpha), F*np.sin(alpha))

while ((y>0) | (vy>0)):
    Fx, Fy = drag(v, alpha)
    # acceleration:
    ax = -Fx/m
    ay = -Fy/m - g

    x = x + vx*dt + 0.5*ax*dt**2
    y = y + vy*dt + 0.5*ay*dt**2

    vx = vx + ax*dt
    vy = vy + ay*dt

    v = np.sqrt(vx*vx+vy*vy)
    alpha = math.atan2(vy,vx)

    X.append(x)
    Y.append(y)
    t = t + dt

# Biar graph nya kaga kurang dari y=0
ft = Y[-2]/(Y[-2]-Y[-1]) # fractional time to last point
X[-1] = X[-2] + (X[-1]-X[-2])*ft
Y[-1] = 0.
t = t - (1-ft)*dt

print('Total flight time: %.2f sec'%t)
print('Total distance   : %.2f m'%X[-1])

plt.figure()
plt.plot(X,Y)

plt.title('Bullet Projectile')
plt.xlabel('Distance')
plt.ylabel('Height')
plt.show()

