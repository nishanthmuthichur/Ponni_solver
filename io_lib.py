import numpy as np
import h5py  as h5


def read_1D_grid_data(wkdir_grid_read, ip_fname):
    
    ip_fname_abs = wkdir_grid_read + ip_fname

    print(f'ponni_solver: Reading grid data from file:{ip_fname_abs}')

    file_dp = h5.File(ip_fname_abs, 'r')

    xcoord = file_dp.get('/xcoord')

    xcoord = np.array(xcoord)

    file_dp.close()

    return xcoord

def read_2D_grid_data(wkdir_grid_read, ip_fname):
    
    ip_fname_abs = wkdir_grid_read + ip_fname

    print(f'ponni_solver: Reading grid data from file:{ip_fname_abs}')

    file_dp = h5.File(ip_fname_abs, 'r')

    xcoord = file_dp.get('/xcoord')
    ycoord = file_dp.get('/ycoord')

    xcoord = np.array(xcoord)
    ycoord = np.array(ycoord)    

    file_dp.close()

    return xcoord, ycoord

def write_output_to_hdf5_file(ip, flow):

    op_fname_abs = ip.wkdir_write_data + \
                       ip.op_gen_fname + \
                                   '_' + \
                      str(flow.op_idx) + \
                                 '.h5'
                              
    file_dp = h5.File(op_fname_abs, 'w')

    file_dp.create_dataset('/time'     , data = flow.time)
    file_dp.create_dataset('/time_idx' , data = flow.Iter)    
    file_dp.create_dataset('/u_vel'    , data = flow.U_sol)

    file_dp.close()                                   
