# Particle-Swarm-Optimization(PSO)
This code for multi-purpose of Particle Swarm Optimization(PSO) Algortihm. PSO algorithm is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. 


# Examples of Applied PSO Algorithm
To use this code for optimizes a problems,You required to passing two arguments. The statement argument mush following the rules below

**Step 1 : Cost function or objective function** is the mathematical function that minimize the output when the global minumum are given. The **Cost function or objective function** must be in ```lambda```function. **Noted** if your **Cost function or objective function** is complex, you can encapsulated in ```def``` function, and call it from ```lambda``` function. Example below, 
```
def surface_function(position):
    x = position[0]
    y = position[1]
    z = 3*np.exp(-1*(y + 1)**2 - x**2) * (x-1)**2 - ((np.exp(-(x+1)**2 - 8**2))/3) + np.exp(-x**2 - y**2) *(10*x**3 - 2*x +     10*y**5)

    return z

cost_function = lambda position : surface_function(position)
```

**Step 2 : Problems Argument** is to defines your specify the argument, **Problems Argument** must be in ```dict type```, all keys name must same to this examples below,
```
#youre initial models
var_min = -10       #lower bound of 
var_max = 10
num_pop = 2
num_var = 1
seed = 12345

#problems arguments
problem = {
    'cost_function' : cost_function,
    'var_min' : var_min,
    'var_max' : var_max,
    'num_var' : num_var,
    'num_pop' : num_pop,
    'seed'    : 12345
}
```

**Step 3 : Params Arguments** is parameters of the PSO iterative, like **Problems Argument**, type of  **Params Arguments**  must be in ```dict type```, all keys name must same to this examples below,

```
#youre params
num_iter = 1000     #minimum of iteratian
w_damp = 1          #damping constant

kappa = 1           
phi_1 = 2.05
phi_2 = 2.05
phi = phi_1 + phi_2
chi = kappa/np.abs(2 - phi - np.sqrt(phi**2 - 4*phi))
params = {
    'num_iter' : num_iter,
    'w'        : chi,
    'w_damp'   : w_damp,
    'c1'       : chi*phi_1,
    'c2'       : chi*phi_2
}
```

## 1. Optimize global minum of Surface Equation
Given a surface equation that have local and global minumun, the surface equation is

<img src="https://render.githubusercontent.com/render/math?math=f(x,y)=z=3e^{-(y + 1)^2-x^2}(x-1)^2-\frac{e^{(x + 1)^2-8^3}}{3}+e^{(-x^2-y^2)}(10x^3-2x \+ 10y^5)">

## 2. Invertion Modelling of Vertical Electrical Sounding(VES)
Vertical Electrical Sounding(VES) is geophysical methods that inject the current to the subsurface to identification of subsurface. The output of conducting VES methods are apperant resistivities. Apperant resistivities is ambiguity to interpreted due to coresponding of geometry factor, so we need to inverted apperant resistivities to true resistivites. PSO algortihm can applied to invertion modelling of VES. See my previous repository about VES <a> https://github.com/asidosaputra/PyVES </a>


