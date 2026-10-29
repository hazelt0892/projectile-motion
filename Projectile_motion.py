#split two second-order ODEs into four coupled first-order ODEs
#use numerical solver??
#find optimal angle (less than 45)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dsdt(t, S, B):
    x, vx, y, vy = S
    return [vx, -B*np.sqrt(vx**2+vy**2)*vx, vy, -1-B*np.sqrt(vx**2+vy**2)*vy]

B = 1
V = 1
g = 9.80665
a1 = 40 * np.pi / 180
a2 = 45 * np.pi / 180
a3 = 50 * np.pi / 180

#atol = 1e-7, rtol = 1e-4
sol1 = solve_ivp(dsdt, [0, 2], y0 = [0, V*np.cos(a1), 0, V*np.sin(a1)], t_eval = np.linspace(0, 2, 1000), args = (B,))

x1 = sol1.y[0] *  g
y1 = sol1.y[2] * g

plt.plot(x1, y1)
plt.ylim(bottom = 0)

#print(len(sol1.y))

plt.show()




