#split two second-order ODEs into four coupled first-order ODEs
#use numerical solver??
#find optimal angle (less than 45)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dsdt(t, S, B):
    x, vx, y, vy = S
    return [vx, -B*np.sqrt(vx**2+vy**2)*vx, vy, -g-B*np.sqrt(vx**2+vy**2)*vy]

def distance(a, B, V, t=8):
    sol = solve_ivp(dsdt, [0, t], y0 = [0, V*np.cos(a), 0, V*np.sin(a)], t_eval = np.linspace(0, t, 10000), args = (B,))
    pos_idx = np.where(np.diff(np.sign(sol.y[2])) < 0)[0][0]
    neg_idx = pos_idx + 1
    distance = (sol.y[0][pos_idx] + sol.y[0][neg_idx]) / 2
    return distance

#define variables
rho = 1.225
Cd = 0.47 #approximate value only 
r = 0.025
A = np.pi * (r**2)
b = 0.5 * rho * Cd * A
m = 2
B = b / m
V = 60
g = 9.80665

#angles
a1 = 40 * np.pi / 180
a2 = 45 * np.pi / 180
a3 = 50 * np.pi / 180

#atol = 1e-7, rtol = 1e-4
sol1 = solve_ivp(dsdt, [0, 8], y0 = [0, V*np.cos(a1), 0, V*np.sin(a1)], t_eval = np.linspace(0, 8, 4000), args = (B,))
max_distance = round(distance(a1, B, V, 8), 2)

x1 = sol1.y[0]
y1 = sol1.y[2]

# Height against distance graph
plt.figure(1)
plt.plot(x1, y1)
plt.ylim(bottom = 0)
plt.xlabel("Distance /m")
plt.ylabel("Height /m")
plt.text(240, 70, f'Max distance: {max_distance}')

plt.show()
