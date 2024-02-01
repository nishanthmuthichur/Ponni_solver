import numpy as np
import h5py as h5

#*****************************INPUT PARAMETERS*********************************

wkdir_grid_write = 'C:\\Users\\Nishanth\\Desktop\\nish_work\\python_proj\\flow_solver_2D'
op_fname = 'ip_grid_2D_101_x_101.h5'

x_min = 0
x_max = 5

y_min = -1
y_max =  1

Nx = 101
Ny = 101

#****************************START_OF_CODE_EXECUTION***************************

op_fname_abs = wkdir_grid_write + '\\' + op_fname

xcoord = np.zeros((Nx, Ny))        
ycoord = np.zeros((Nx, Ny))            
    
dx = (x_max - x_min) / (Nx - 1)
dy = (y_max - y_min) / (Ny - 1)    
    
for x_idx in range(0, Nx):
  for y_idx in range(0, Ny):  
    
      xcoord[x_idx, y_idx] = x_min + dx * x_idx        
      ycoord[x_idx, y_idx] = y_min + dy * y_idx

file_dp = h5.File(op_fname_abs, 'w')

file_dp.create_dataset('/xcoord', data = xcoord)
file_dp.create_dataset('/ycoord', data = ycoord)

file_dp.close()

print('grid_gen_2D: 2D grid generated successfully')