import numpy as np
import fin_diff_lib as fd
import ponni_utils as pu

def comp_fluxes_lconv_1D(flow, deriv_sten):
    
    U_sol = flow.U_sol
    
    dUdX_sol = deriv_sten(U_sol)        
        
    F_sol = -dUdX_sol
        
    flow.F_sol = F_sol
    
    return flow

