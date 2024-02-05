import numpy as np
import h5py as h5

import fin_diff_lib as fdl
#***************************MACRO DEFINITIONS**********************************

INIT_DUM_VAL = -100000

#************************DATA STRUCTURE DEFINITIONS****************************

class flow_blk_1D:
    
    def __init__(self):

        self.U_sol = list()
        self.F_sol = list()
    
        self.x_coord = 0
    
        self.metric_xE = 0
        self.metric_Ex = 0
    
        self.Iter  = 0
        self.time  = 0
        self.op_idx = 0

        self.comp_fluxes     = 0
        self.comp_deriv      = 0
        self.comp_time_march = 0
        self.time_fil        = 0

    def __str__(self):
        
        return f'Iter = {self.Iter}'    

#*************************FUNCTION DEFINITIONS*********************************

#****************************
def comp_1D_time_step(x_coord, \
                         CFL):
        
    dx_min = INIT_DUM_VAL
    
    Nx = len(x_coord)
    
    d_xcoord = x_coord[1 : (Nx - 1)] - \
               x_coord[0 : (Nx - 2)]
               
    dx_min = d_xcoord.min()
    
    dt = CFL * dx_min
     
    print(f'ponni_1D: CFL = {CFL}; time step = {dt} s')    
    
    return dt
    
#****************************
def comp_2D_time_step(xcoord, \
                      ycoord, \
                         CFL):
        
    dx_min = INIT_DUM_VAL
    dy_min = INIT_DUM_VAL
    
    (Nx, Ny) = xcoord.shape
    
    d_xcoord = xcoord[1 : (Nx - 1), :] - \
               xcoord[0 : (Nx - 2), :]
               
    d_ycoord = ycoord[:, 1 : (Ny - 1)] - \
               ycoord[:, 0 : (Ny - 2)]
    
    dx_min = d_xcoord.min()
    dy_min = d_ycoord.min()    
    
    if (dx_min < dy_min):
        
        dt = CFL * dx_min
        
    else:
    
        dt = CFL * dy_min    
    
    print(f'flow_solver_2D: CFL = {CFL}; time step = {dt} s')    
    
    return dt

def comp_1D_grid_metrics(flow):
    
    x_coord = flow.x_coord
    
    metric_xe = flow.comp_deriv(x_coord)
    
    metric_ex = 1 / metric_xe
    
    flow.metric_xe = metric_xe
    flow.metric_ex = metric_ex
    
    return flow
    

def filter_sol(Flow_vec):
    
    N_var = len(Flow_vec.U_sol)
    
    (Nx, Ny) = Flow_vec.U_sol[0].shape
    
    for var_idx in range(0, N_var):
        
        sol_field = Flow_vec.U_sol[var_idx]
        
        #Filtering along y-direction
        for x_idx in range(0, Nx):
            
            sol_field[x_idx, :] = fdl.compute_CD10_filter(sol_field[x_idx, :])    
            
        for y_idx in range(0, Ny):
            
            sol_field[:, y_idx] = fdl.compute_CD10_filter(sol_field[:, y_idx])
            
        Flow_vec.U_sol[var_idx] = sol_field    
    
    return Flow_vec

         

