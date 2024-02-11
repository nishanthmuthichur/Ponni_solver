
def comp_fluxes_lconv_1D(flow):
    
    U_sol = flow.U_sol
    metric_Ex = flow.metric_Ex
   
    dUdE_sol = flow.comp_deriv(U_sol)        
    dUdx_sol = metric_Ex * dUdE_sol
        
    c0 = 1
    
    F_sol = -c0 * dUdx_sol
        
    flow.F_sol = F_sol
    
    return flow

