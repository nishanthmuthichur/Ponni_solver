import ponni_utils as pu
import ponni_main as pm

ip = pu.ip_params()

ip.flow_model = pu.LCONV_1D
ip.deriv_sten = pu.DRP4
ip.time_march = pu.RK4
ip.fil_sten   = pu.FIL_1

ip.wkdir_grid_read = 'C:\\Users\\Nishanth\\Desktop\\nish_work\\python_proj\\ponni_solver\\grid_gen\\'
ip.ip_fname        = 'ip_grid_1D_101.h5'

ip.CFL = 0.1

ip.stop_time = 0
ip.stop_iter = 10

pm.ponni_main(ip)

print(f'ponni: Computation completed sucessfully')

