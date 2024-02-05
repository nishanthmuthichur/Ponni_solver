import numpy as np

import ponni_lib as pl
import ponni_utils as pu
import ponni_usermod as pum
import ponni_intf as pi
import io_lib as io

# 1. Parse the input parameters
# 2. Read the input grid
# 3. Compute metrics
# 4. Setup the boundary conditions
# 5. Setup the initial conditions
# 6. Time marching
#       a. Compute derivatives
#       b. RK4 time stepping
#       c. Filtering
# 7. Print output as needed

def ponni_main(ip):

    # Setup the necessary data structures
    flow = pl.flow_blk_1D()
    
    flow.comp_fluxes     = pi.get_comp_fluxes_func_ptr(ip.flow_model)    
    flow.comp_deriv      = pi.get_deriv_sten_func_ptr(ip.deriv_sten)
    flow.comp_time_march = pi.get_time_march_func_ptr(ip.time_march)
    flow.comp_fil        = pi.get_fil_sten_func_ptr(ip.fil_sten)    
    
    # Read the data from the input grid
    x_coord = io.read_1D_grid_data(ip.wkdir_grid_read,  \
                                   ip.ip_fname)
    flow.x_coord = x_coord

    # Compute the grid metrics
    flow = pl.comp_1D_grid_metrics(flow)
    
    # Compute the time step
    Delta_t = pl.comp_1D_time_step(x_coord, ip.CFL)
    
    # Setup the initial conditions
    flow = pum.set_init_cond_1D_conv(flow, x_coord)
    
    while ((flow.time < ip.stop_time) or (flow.Iter < ip.stop_iter)):
        
        print(f'ponni_main: Iter = {flow.Iter}')
     
        flow = flow.comp_time_march(flow, Delta_t)
        
        flow.U_sol = flow.comp_fil(flow.U_sol)
        
        if ((flow.Iter % ip.output_freq) == 0):
            
            io.write_output_to_hdf5_file(ip, flow)
            flow.op_idx = flow.op_idx + 1
        
        flow.Iter = flow.Iter + 1
        flow.time = flow.time + Delta_t
        
