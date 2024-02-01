import ponni_utils as pu
import ponni_main as pm

ip = pu.ip_params()

ip.wkdir_grid_read = 'C:\\Users\\Nishanth\\Desktop\\nish_work\\python_proj\\ponni_solver\\grid_gen\\'
ip.ip_fname        = 'ip_grid_1D_101.h5'

ip.CFL = 0.1

#print(f'Input grid working directory: {ip.wkdir_grid_read}')
#print(f'Input grid filename: {ip.ip_fname}')

pm.ponni_main(ip)

