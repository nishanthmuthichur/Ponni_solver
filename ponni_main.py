import numpy as np

import ponni_lib as pl
import ponni_usermod as pum
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

    # Read the data from the input grid
    x_coord = io.read_1D_grid_data(ip.wkdir_grid_read,  \
                                   ip.ip_fname)

    # Compute the time step
    dt = pl.comp_1D_time_step(x_coord, ip.CFL)

    # Setup the necessary data structures
    flow = pl.flow_blk()
    
    # Setup the initial conditions
    flow = pum.set_init_cond_1D_conv(flow, x_coord)
    
    
    

