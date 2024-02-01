import numpy as np
import h5py as h5

#*****************************INPUT PARAMETERS*********************************

wkdir_grid_write = 'C:\\Users\\Nishanth\\Desktop\\nish_work\\python_proj\\ponni_solver\\grid_gen'
op_fname = 'ip_grid_1D_101.h5'

x_min = 0
x_max = 1

Nx = 101

#****************************START_OF_CODE_EXECUTION***************************

op_fname_abs = wkdir_grid_write + '\\' + op_fname

xcoord = np.zeros(Nx)        
    
dx = (x_max - x_min) / (Nx - 1)
    
for x_idx in range(0, Nx):
    
      xcoord[x_idx] = x_min + dx * x_idx        

file_dp = h5.File(op_fname_abs, 'w')

file_dp.create_dataset('/xcoord', data = xcoord)

file_dp.close()

print('grid_gen_1D: 1D grid generated successfully')

