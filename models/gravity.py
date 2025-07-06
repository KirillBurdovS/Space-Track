import numpy as np
from scipy.integrate import solve_ivp

def gravity_equation(t, state, GM):
    x,y,z,vx,vy,vz = state
    r = np.sqrt(x**2 + y**2 + z**2)
    ax = -GM * x / r**3
    ay = -GM * y / r ** 3
    az = -GM * z / r ** 3
    return [vx, vy, vz, ax, ay, az]

def simulate_orbit(initial_state, t_span, GM):
    sol = solve_ivp(gravity_equation, t_span, initial_state, args=(GM,), dense_output=True)
    return sol
