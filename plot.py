import numpy as np
import matplotlib.pyplot as plt

time, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u = np.loadtxt('data.txt', skiprows=1).T

plt.plot(time, a, label='H', c='blue')
plt.plot(time, b, label='C', c='green')
#plt.plot(time, c, label='N', c='150')
plt.plot(time, d, label='O', c='orange')
#plt.plot(time, e, label='Br', c='yellow')
#plt.plot(time, f, label='I', c='010')
#plt.plot(time, g, label='Cl', c='030')
plt.plot(time, h, label='H2O2', c='yellow')
#plt.plot(time, i, label='H2', c='black')
#plt.plot(time, j, label='N2', c='060')
plt.plot(time, k, label='Br2', c='090')
#plt.plot(time, l, label='I2', c='120')
#plt.plot(time, m, label='Cl2', c='purple')
plt.plot(time, n, label='H2O', c='red')
#plt.plot(time, o, label='HBrO', c='180')
#plt.plot(time, p, label='NO2', c='110')
plt.plot(time, q, label='CO2', c='brown')
plt.plot(time, r, label='CO', c='black')
plt.plot(time, s, label='CH4', c='purple')
plt.plot(time, t, label='C6H6', c='210')
plt.plot(time, u, label='C4H10', c='030')
plt.legend(loc='upper left')
plt.xlabel('Time')
plt.ylabel('Amounts')
plt.title('Gillespie Algorithm - Stochastic Simulation of Chemical Reactions')
plt.grid()
plt.show()
