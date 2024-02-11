import numpy as np


def set_init_cond_1D_conv(flow):

    x_coord = flow.x_coord
    Nx = len(x_coord)
    
    u_vel_init = np.zeros(Nx)

    sig = 0.04
    x_0 = 0.3

    #U_init = (1 / (sig * np.sqrt(2 * np.pi))) * \
    #       np.exp(-((x_coord - x_0)**2)/(2 * sig**2))

    U_init = np.sin(2 * np.pi * x_coord)

    flow.U_sol = U_init
    
    print('usermod: Initial conditions has been computed')        
        
    return flow

