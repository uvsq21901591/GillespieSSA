import numpy as np
import matplotlib.pyplot as plt

time,x00,x01,x02,x03,x04,x05,x06,x07,x08,x09,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40,x41,x42,x43,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61,x62 = np.loadtxt('data.txt', skiprows=1).T

# plt.plot(time, x00, label='Na', c='blue')
# plt.plot(time, x01, label='Cl2', c='green')
# plt.plot(time, x02, label='NaCl', c='black')
plt.plot(time, x03, label='H2', c='orange')
plt.plot(time, x04, label='O2', c='red')
plt.plot(time, x05, label='H2O', c='brown')
plt.plot(time, x06, label='C', c='purple')
#==# plt.plot(time, x07, label='H2O2', c='yellow')
plt.plot(time, x08, label='CO2', c='coral')
# plt.plot(time, x09, label='CH4', c='yellow')
# plt.plot(time, x10, label='N2', c='gold')
plt.plot(time, x11, label='NH3', c='peru')
plt.plot(time, x12, label='H3O', c='khaki')
plt.plot(time, x13, label='HO', c='tan')
# plt.plot(time, x14, label='C5H12', c='darkred')
# plt.plot(time, x15, label='S2O8', c='goldenrod')
# plt.plot(time, x16, label='I', c='darkkhaki')
# plt.plot(time, x17, label='SO4', c='olive')
# plt.plot(time, x18, label='I2', c='olivedrab')
# plt.plot(time, x19, label='Fe', c='darkseagreen')
# plt.plot(time, x20, label='FeO3', c='limegreen')
# plt.plot(time, x21, label='Fe3O4', c='palegreen')
# plt.plot(time, x22, label='C2H6', c='lime')
# plt.plot(time, x23, label='C3H8', c='turquoise')
# plt.plot(time, x24, label='C4H10', c='silver')
# plt.plot(time, x25, label='C2H4', c='darkcyan')
# plt.plot(time, x26, label='C2H2', c='aquamarine')
# plt.plot(time, x27, label='C6H12O6', c='seagreen')
# plt.plot(time, x28, label='Fe2O3', c='deepskyblue')
# plt.plot(time, x29, label='Al', c='dodgerblue')
# plt.plot(time, x30, label='Al2O3', c='cadetblue')
# plt.plot(time, x31, label='NO', c='violet')
# plt.plot(time, x32, label='CO', c='indigo')
# plt.plot(time, x33, label='Cu2S', c='slateblue')
# plt.plot(time, x34, label='Cu2O', c='lightblue')
# plt.plot(time, x35, label='Cu', c='plum')
# plt.plot(time, x36, label='SO2', c='maroon')
# plt.plot(time, x37, label='NaCl*', c='navy')
# plt.plot(time, x38, label='H2SO4', c='royalblue')
# plt.plot(time, x39, label='HCl', c='teal')
plt.plot(time, x40, label='Na2SO4', c='springgreen')
plt.plot(time, x41, label='Cu(OH)2', c='mediumblue')
plt.plot(time, x42, label='Ag', c='darkviolet')
plt.plot(time, x43, label='PO4', c='darkorange')
plt.plot(time, x44, label='Ag3PO4', c='firebrick')
plt.plot(time, x45, label='CaC2', c='magenta')
plt.plot(time, x46, label='C2H2', c='rebeccapurple')
plt.plot(time, x47, label='Ca(OH)2', c='deeppink')
plt.plot(time, x48, label='KClO3', c='paleturquoise')
plt.plot(time, x49, label='KCl', c='steelblue')
plt.plot(time, x50, label='Ba(ClO3)2', c='lightseagreen')
plt.plot(time, x51, label='BaCl2', c='greenyellow')
plt.plot(time, x52, label='Sr(ClO3)2', c='saddlebrown')
plt.plot(time, x53, label='SrCl2', c='sienna')
plt.plot(time, x54, label='Al2O3', c='rosybrown')
plt.plot(time, x55, label='HNO3', c='orchid')
plt.plot(time, x56, label='C6H6', c='burlywood')
plt.plot(time, x57, label='C6H5NO2', c='tomato')
plt.plot(time, x58, label='TiCl4', c='crimson')
plt.plot(time, x59, label='Mg', c='darkmagenta')
plt.plot(time, x60, label='Ti', c='cornflowerblue')
plt.plot(time, x61, label='MgCl2', c='lightgreen')
plt.plot(time, x62, label='CuO', c='palevioletred')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Amounts')
plt.title('Gillespie Algorithm - Stochastic Simulation of Chemical Reactions')
plt.grid()
plt.show()
