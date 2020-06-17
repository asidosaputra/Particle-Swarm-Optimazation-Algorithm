import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy as dc

class PSO():
    '''
    Particle Swarm Optimization, 17 June 2020
    Created by : Asido Saputra Sigalinggin, S.T
    '''
    def __init__(self):
        self.__problem = None
        self.__params = None

    
    def optimize(self, problem, params):
        self.__problem = problem
        self.__params  = params

    def run(self, verbose=True, show_iter = False):
        ## initialize number of iteration
        num_iter = self.__params['num_iter']
        c1 = self.__params['c1']
        c2 = self.__params['c2']
        w = self.__params['w']
        w_damp = self.__params['w_damp']
        cost_hist = np.zeros(num_iter)

        particle, global_best = self.__gen_pop()
        for i in range(num_iter):
            for j in range(num_pop):
                particle[j]['velocity'] = w*particle[j]['velocity'] + c1*np.random.rand(num_var)*(particle[j]['best']['position'] - particle[j]['position']) + c2*np.random.rand(num_var)*(global_best['position'] - particle[j]['position'])
                particle[j]['position'] = particle[j]['position'] + particle[j]['velocity']

                particle[j]['cost'] = cost_function(particle[j]['position'])

                if particle[j]['cost'] < particle[j]['best']['cost']:
                    particle[j]['best']['cost'] =  particle[j]['cost']
                    particle[j]['best']['position'] =  particle[j]['position']

                    if particle[j]['best']['cost'] < global_best['cost']:
                        global_best['cost'] = particle[j]['best']['cost']
                        global_best['position'] = particle[j]['best']['position']
            
            w = w*w_damp
            cost_hist[i] = global_best['cost']
            if verbose : print('iteration - {0}, cost : {1}'.format(i, global_best['cost']))
        if show_iter: self.__show_iter(cost_hist)
        return global_best, cost_hist
        
    def __gen_pop(self):
        '''
        Generate population
        '''
        empty_particle = {
            'position' : None,
            'velocity' : None,
            'cost' : None,
            'best' : {
                'position' : None,
                'cost' : None
            }
        }

        global_best = {
            'position' : None,
            'cost' : np.inf
        }


        num_pop = self.__problem['num_pop']
        var_min = self.__problem['var_min']
        var_max = self.__problem['var_max']
        num_var = self.__problem['num_var']
        seed    = self.__problem['seed'] 

        if seed is not None : np.random.seed(seed)
        position = np.random.uniform(var_min, var_max, size=(num_pop, num_var))
        particle = []
        for i in range(num_pop):
            empty_particle['position']  = position[i, :]
            empty_particle['velocity'] = np.zeros(num_var)
            empty_particle['cost'] = self.__problem['cost_function'](empty_particle['position'])
            empty_particle['best']['position'] = empty_particle['position']
            empty_particle['best']['cost'] = empty_particle['cost']

            particle.append(dc(empty_particle))

            if empty_particle['cost'] < global_best['cost']:
                global_best['position'] = empty_particle['position']
                global_best['cost'] = empty_particle['cost']
            
        return particle, global_best

    def __show_iter(self, cost_hist):
        iter = np.arange(len(cost_hist))
        plt.plot(iter, cost_hist)
        plt.ylabel('Log Cost')
        plt.xlabel('Iteration')
        plt.show()
        


if __name__ == "__main__":
    def surface_function(position):
        x = position[0]
        # y = position[1]
        # z = 3*np.exp(-1*(y + 1)**2 - x**2) * (x-1)**2 - ((np.exp(-(x+1)**2 - 8**2))/3) + np.exp(-x**2 - y**2) *(10*x**3 - 2*x + 10*y**5)
        z = x**2 + x + 1
        return z

    cost_function = lambda position : surface_function(position)

    #model
    var_min = -10
    var_max = 10
    num_pop = 2
    num_var = 1
    seed = 12345

    #params
    num_iter = 1000
    # c1, c2 = 2.05, 2.05
    # w  = 1
    w_damp = 1

    kappa = 1
    phi_1 = 2.05
    phi_2 = 2.05
    phi = phi_1 + phi_2
    chi = kappa/np.abs(2 - phi - np.sqrt(phi**2 - 4*phi))

    problem = {
        'cost_function' : cost_function,
        'var_min' : var_min,
        'var_max' : var_max,
        'num_var' : num_var,
        'num_pop' : num_pop,
        'seed'    : 12345
    }

    params = {
        'num_iter' : num_iter,
        'w'        : chi,
        'w_damp'   : w_damp,
        'c1'       : chi*phi_1,
        'c2'       : chi*phi_2
    }

    pso = PSO()
    pso.optimize(problem, params)
    global_best, cost_hist = pso.run(verbose=False, show_iter=False)
    
    print(global_best)
    x = np.arange(-10, 10, 0.01)
    z = x**2 + x + 1
    plt.plot(x, z)
    plt.scatter(global_best['position'], global_best['cost'] )
    plt.show()