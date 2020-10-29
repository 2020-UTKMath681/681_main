'''
Solve the SIR equations in parallel while varying parameters
'''

from multiprocessing import Pool
import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt

#time point to solve to
t_end = 10

#initial values as population fractions
I0 = 1e-2
R0 = 0
# vectorize initial conditions
x0 = np.array([1-I0-R0, I0, R0])

# static parameter values
params = {}
#params['beta'] = 1.4247
params['gamma'] = 1
params['mu'] = 0.01

# what parameter will we be varying?
p_name = 'beta'


def main(pool):
    # parameter values to loop over
    p_vals = np.linspace(0,1.5,4001)

    # apply this new function to all our p_vals and collect the results
    results = pool.map(solve_ODEs, p_vals)
    results = np.array(results)
    print(results.shape)

    ##### Plot results #####
    fig = plt.figure(figsize=(9,7))
    plt.plot(p_vals,results[:,0],p_vals,results[:,1],p_vals,results[:,2])
    plt.legend(['S','I','R'])
    plt.title("Plot of $S,I,R$ at t={} with various {}".format(t_end,p_name))
    plt.xlabel(p_name)
    plt.ylabel("population fraction")
    plt.show()


def solve_ODEs(p_val):
    '''Solves ODEs with the passed in settings.
    p_val should be a single value to set the parameter p_name to

    Has to be specified on the module level to be pickleable
    '''
    params[p_name] = p_val

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

    # the solver will solve (integrate) up to the given time.
    solver.integrate(t_end)
    
    return (solver.y[0], solver.y[1], solver.y[2])


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


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        main(pool)
