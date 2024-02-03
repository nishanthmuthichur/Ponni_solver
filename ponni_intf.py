import sys

import fin_diff_lib as fd

import lconv_1D as LC1D
import ponni_utils as pu


def get_comp_fluxes_func_ptr(flow_model):
    
    if (flow_model == pu.LCONV_1D):
    
        f_ptr = LC1D.comp_fluxes_lconv_1D
        
    else:
        
        print(f'ponni_main: Error! Specified flow model does not exist.')
        sys.exit(1)    
        
    return f_ptr

def get_deriv_sten_func_ptr(deriv_sten):
    
    if (deriv_sten == pu.CD8):
    
        f_ptr = fd.comp_CD8_deriv_periodic
        
    elif (deriv_sten == pu.DRP4):
        
        f_ptr = fd.comp_DRP4_deriv_periodic
        
    else:
        
        print(f'ponni_main: Error! Specified derivative stencil does not exist.')
        sys.exit(1)    
        
    return f_ptr

def get_time_march_func_ptr(time_march):
    
    if (time_march == pu.RK4):
    
        f_ptr = fd.comp_RK4_time_step
        
    else:
        
        print(f'ponni_main: Error! Specified time marching routine does not exist.')
        sys.exit(1)    
        
    return f_ptr

def get_fil_sten_func_ptr(fil_sten):
    
    if (fil_sten == pu.FIL_1):
    
        f_ptr = fd.comp_DRP4_fil_periodic
        
    else:
        
        print(f'ponni_main: Error! Specified time marching routine does not exist.')
        sys.exit(1)    
        
    return f_ptr