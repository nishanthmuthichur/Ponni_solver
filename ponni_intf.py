import sys

import fin_diff_lib as fd

import lconv_1D as LC1D
import ponni_utils as pu

def get_comp_fluxes_func_ptr(flow_model):
    
    if (flow_model == pu.LCONV_1D):
    
        f_ptr = LC1D.comp_fluxes_lconv_1D
        print('ponni_main: 1D linear convection flow model is selected.')        
        
    else:
        
        print('ponni_main: Error! Specified flow model does not exist.')
        sys.exit(1)    
        
    return f_ptr

def get_comp_deriv_func_ptr(deriv_sten):
    
    if (deriv_sten == pu.CD8):
    
        f_ptr = fd.comp_CD8_deriv_periodic
        print('ponni_main: 8th order explicit CD derivative scheme is selected.')        
        
    elif (deriv_sten == pu.DRP4):
        
        f_ptr = fd.comp_DRP4_deriv_periodic
        print('ponni_main: 4th order DRP derivative scheme is selected.')        
        
    else:
        
        print('ponni_main: Error! Specified derivative stencil does not exist.')
        sys.exit(1)    
        
    return f_ptr

def get_time_march_func_ptr(time_march):
    
    if (time_march == pu.RK4):
    
        f_ptr = fd.comp_RK4_time_step_test
        print('ponni_main: RK4 time stepping scheme is selected.')        
        
    else:
        
        print(f'ponni_main: Error! Specified time marching routine does not exist.')
        sys.exit(1)    
        
    return f_ptr

def get_comp_fil_func_ptr(fil_sten):
    
    if (fil_sten == pu.FIL_1):
    
        f_ptr = fd.comp_DRP4_fil_periodic
        print('ponni_main: 4th order filtering scheme is selected.')                
        
    else:
        
        print(f'ponni_main: Error! Specified time marching routine does not exist.')
        sys.exit(1)    
        
    return f_ptr