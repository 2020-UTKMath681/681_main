"""
Solves the SIR system of ODEs
"""

import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt

#time points to solve at
tpts = np.linspace(0,10,1001)

#initial values as population fractions
I0 = 1e-2
R0 = 0

# parameter values
params = {}
params['beta'] = 1.4247
params['gamma'] = 0.14286
params['mu'] = 0.01


##################################

# vectorize initial conditions
x0 = np.array([1-I0-R0, I0, R0])

# define ode equations
def SIR_ODEs(t,x,params):
    '''This function returns the time derivates of S,I,R.

    The ode solver expects the first two arguments to be t and x
    NOTE: This is the OPPPOSITE order from scipy.integrate.odeint!!

    The params argument should be a dict with beta, gamma, and mu as keys.
    It must be passed into the solver using the set_f_params method
    '''

    S = x[0]; I = x[1]; R = x[2]
    dx = np.zeros(3)

    dx[0] = -params['beta']*S*I + params['mu']*(I+R)
    dx[1] = params['beta']*S*I - params['gamma']*I - params['mu']*I
    dx[2] = params['gamma']*I - params['mu']*R

    return dx

##### Solve procedure #####
Ssol = []; Isol = []; Rsol = []

# create solver object
solver = ode(SIR_ODEs)
# set the solver method to RK 4(5), Dormand/Prince
# see the docs for scipy.integrate.ode for the options with this solver
# here we'll use the defaults, but pay attention to atol/rtol especially
solver.set_integrator('dopri5')
# set the initial conditions
solver.set_initial_value(x0,0)
# pass in the solver parameters
solver.set_f_params(params)

# the solver will solve (integrate) up to a given time.
# we want a mesh of times, so we will integrate up to each time in our
#   mesh in a loop
for t in tpts:
    # tpts[0] = 0, so take this opportunity to record the initial conditions
    if t == 0:
        Ssol.append(x0[0])
        Isol.append(x0[1])
        Rsol.append(x0[2])
    else:
        #otherwise, integrate up to the new time and record solution
        solver.integrate(t)
        assert solver.successful(), "Solver did not converge at time {}.".format(t)
        Ssol.append(solver.y[0])
        Isol.append(solver.y[1])
        Rsol.append(solver.y[2])

##### Plot result #####
fig = plt.figure(figsize=(9,7))
plt.plot(tpts,Ssol,tpts,Isol,tpts,Rsol)
plt.legend(['S','I','R'])
plt.title("Plot of $S,I,R$ vs. time")
plt.xlabel("$t$")
plt.ylabel("population fraction")
plt.show()

