from operator import add

import numpy as np

# This function is used to compute the derivative 'dYdX' of 'Y' using 
# an explicit 8th order central difference stencil

def comp_CD8_deriv_periodic(U):

    N_pts = len(U);
    dUdX = np.zeros(N_pts);    

    a_m4 = (1/280)
    a_m3 = (-4/105)
    a_m2 = (1/5)
    a_m1 = (-4/5)
    a_0  =  0 
    a_p1 = (4/5)
    a_p2 = (-1/5)
    a_p3 = (4/105)
    a_p4 = (-1/280)

    for idx in range(0, N_pts):

        idx_m4 = idx - 4            
        idx_m3 = idx - 3
        idx_m2 = idx - 2
        idx_m1 = idx - 1
        idx_0  = idx
            
        if (idx <= (N_pts - 5)):
                
            idx_p1 = idx + 1
            idx_p2 = idx + 2
            idx_p3 = idx + 3
            idx_p4 = idx + 4                
                
        elif (idx == (N_pts - 4)): 
                
            idx_p1 = idx + 1
            idx_p2 = idx + 2
            idx_p3 = idx + 3
            idx_p4 = (idx + 4) % N_pts                
            
        elif (idx == (N_pts - 3)): 
                
            idx_p1 = idx + 1
            idx_p2 = idx + 2
            idx_p3 = (idx + 3) % N_pts                            
            idx_p4 = (idx + 4) % N_pts                            
            
        elif (idx == (N_pts - 2)): 
                
            idx_p1 = idx + 1
            idx_p2 = (idx + 2) % N_pts                            
            idx_p3 = (idx + 3) % N_pts                            
            idx_p4 = (idx + 4) % N_pts
            
        elif (idx == (N_pts - 1)): 
                
            idx_p1 = (idx + 1) % N_pts                            
            idx_p2 = (idx + 2) % N_pts                            
            idx_p3 = (idx + 3) % N_pts                            
            idx_p4 = (idx + 4) % N_pts            
            
        else: 
            
            print(f'Error! All if conditions are exhausted.')

        dUdX[idx] = a_m3 * U[idx_m3] + \
                    a_m2 * U[idx_m2] + \
                    a_m1 * U[idx_m1] + \
                    a_0  * U[idx_0 ] + \
                    a_p1 * U[idx_p1] + \
                    a_p2 * U[idx_p2] + \
                    a_p3 * U[idx_p3]

    return dUdX

# 4th order DRP derivative scheme
def comp_DRP4_deriv_periodic(Y):

    N_pts = len(Y);
    dYdX = np.zeros(N_pts);    

    a_m3 = -0.02651995
    a_m2 =  0.18941314
    a_m1 = -0.79926643
    a_0  =  0 
    a_p1 = -a_m1
    a_p2 = -a_m2
    a_p3 = -a_m3

    for idx in range(0, N_pts):

        idx_m3 = idx - 3
        idx_m2 = idx - 2
        idx_m1 = idx - 1
        idx_0  = idx
            
        if (idx <= (N_pts - 4)):
                
            idx_p1 = idx + 1
            idx_p2 = idx + 2
            idx_p3 = idx + 3
                
        elif (idx == (N_pts - 3)): 
                
            idx_p1 = idx + 1
            idx_p2 = idx + 2
            idx_p3 = (idx + 3) % N_pts                
            
        elif (idx == (N_pts - 2)): 
                
            idx_p1 = idx + 1
            idx_p2 = (idx + 2) % N_pts                            
            idx_p3 = (idx + 3) % N_pts                            
            
        elif (idx == (N_pts - 1)): 
                
            idx_p1 = (idx + 1) % N_pts                            
            idx_p2 = (idx + 2) % N_pts                            
            idx_p3 = (idx + 3) % N_pts
            
        else: 
            
            print(f'Error! All if conditions are exhausted.')

        dYdX[idx] = a_m3 * Y[idx_m3] + \
                    a_m2 * Y[idx_m2] + \
                    a_m1 * Y[idx_m1] + \
                    a_0  * Y[idx_0 ] + \
                    a_p1 * Y[idx_p1] + \
                    a_p2 * Y[idx_p2] + \
                    a_p3 * Y[idx_p3] 

    return dYdX

# 4th order DRP derivative scheme
def comp_DRP4_fil_periodic(U):

    N_pts = len(U);
    fil_U = np.zeros(N_pts) 

    d_m3 = -0.01712408960
    d_m2 =  0.08910250435 
    d_m1 = -0.2328759104
    d_0  =  0.3217949913
    d_p1 = d_m1
    d_p2 = d_m2
    d_p3 = d_m3

    for idx in range(0, N_pts):

        idx_m3 = idx - 3
        idx_m2 = idx - 2
        idx_m1 = idx - 1
        idx_0  = idx
            
        if (idx <= (N_pts - 4)):
                
            idx_p1 = idx + 1
            idx_p2 = idx + 2
            idx_p3 = idx + 3
                
        elif (idx == (N_pts - 3)): 
                
            idx_p1 = idx + 1
            idx_p2 = idx + 2
            idx_p3 = (idx + 3) % N_pts                
            
        elif (idx == (N_pts - 2)): 
                
            idx_p1 = idx + 1
            idx_p2 = (idx + 2) % N_pts                            
            idx_p3 = (idx + 3) % N_pts                            
            
        elif (idx == (N_pts - 1)): 
                
            idx_p1 = (idx + 1) % N_pts                            
            idx_p2 = (idx + 2) % N_pts                            
            idx_p3 = (idx + 3) % N_pts
            
        else: 
            
            print(f'Error! All if conditions are exhausted.')

        fil_U[idx] = d_m3 * U[idx_m3] + \
                     d_m2 * U[idx_m2] + \
                     d_m1 * U[idx_m1] + \
                     d_0  * U[idx_0 ] + \
                     d_p1 * U[idx_p1] + \
                     d_p2 * U[idx_p2] + \
                     d_p3 * U[idx_p3] 

    return fil_U

def comp_CD8_deriv(Y):

    N_pts = len(Y);
    dYdX = np.zeros(N_pts);
  
    m = 4;
  
    A = np.array([ \
        [   0    ,    0     ,   0    ,    0   , (-25/12) ,  4    ,   -3    , (4/3)   ,  (-1/4)  ], \
        [   0    ,    0     ,   0    , (-1/4) ,  (-5/6)  , (3/2) , (-1/2)  , (1/12)  ,     0    ], \
        [   0    ,    0     , (1/12) , (-2/3) ,     0    , (2/3) , (-1/12) ,   0     ,     0    ], \
        [   0    , (-1/60)  , (3/20) , (-3/4) ,     0    , (3/4) , (-3/20) , (1/60)  ,     0    ], \
        [(1/280) , (-4/105) , (1/5)  , (-4/5) ,     0    , (4/5) , (-1/5)  , (4/105) , (-1/280) ], \
        [   0    , (-1/60)  , (3/20) , (-3/4) ,     0    , (3/4) , (-3/20) , (1/60)  ,     0    ], \
        [   0    ,    0     , (1/12) , (-2/3) ,     0    , (2/3) , (-1/12) ,   0     ,     0    ], \
        [   0    , (-1/12)  , (1/2)  , (-3/2) ,   (5/6)  , (1/4) ,    0    ,   0     ,     0    ], \
        [ (1/4)  , (-4/3)   ,   3    ,    -4  ,  (25/12) ,   0   ,    0    ,   0     ,     0    ], \
    ])
  
    for idx in range(0, N_pts):
        
        if (idx == 0):
                  
            dYdX[idx] =  A[0,    m   ] * Y[idx    ] + \
                         A[0, (m + 1)] * Y[idx + 1] + \
                         A[0, (m + 2)] * Y[idx + 2] + \
                         A[0, (m + 3)] * Y[idx + 3] + \
                         A[0, (m + 4)] * Y[idx + 4]          
            
        elif (idx == 1):
             
            dYdX[idx] =  A[1, (m - 1)] * Y[idx - 1] + \
                         A[1,    m   ] * Y[idx    ] + \
                         A[1, (m + 1)] * Y[idx + 1] + \
                         A[1, (m + 2)] * Y[idx + 2] + \
                         A[1, (m + 3)] * Y[idx + 3]
                        
        elif (idx == 2):

            dYdX[idx] =  A[2, (m - 2)] * Y[idx - 2] + \
                         A[2, (m - 1)] * Y[idx - 1] + \
                         A[2,    m   ] * Y[idx    ] + \
                         A[2, (m + 1)] * Y[idx + 1] + \
                         A[2, (m + 2)] * Y[idx + 2]
                        
        elif (idx == 3):

            dYdX[idx] =  A[3, (m - 3)] * Y[idx - 3] + \
                         A[3, (m - 2)] * Y[idx - 2] + \
                         A[3, (m - 1)] * Y[idx - 1] + \
                         A[3,    m   ] * Y[idx    ] + \
                         A[3, (m + 1)] * Y[idx + 1] + \
                         A[3, (m + 2)] * Y[idx + 2] + \
                         A[3, (m + 3)] * Y[idx + 3]

        elif (idx == (N_pts - 4)):                       

            dYdX[idx] = A[5, (m - 3)] * Y[idx - 3] + \
                        A[5, (m - 2)] * Y[idx - 2] + \
                        A[5, (m - 1)] * Y[idx - 1] + \
                        A[5,    m   ] * Y[idx    ] + \
                        A[5, (m + 1)] * Y[idx + 1] + \
                        A[5, (m + 2)] * Y[idx + 2] + \
                        A[5, (m + 3)] * Y[idx + 3]
                         
        elif (idx == (N_pts - 3)):
            
            dYdX[idx] = A[6, (m - 2)] * Y[idx - 2] + \
                        A[6, (m - 1)] * Y[idx - 1] + \
                        A[6,    m   ] * Y[idx    ] + \
                        A[6, (m + 1)] * Y[idx + 1] + \
                        A[6, (m + 2)] * Y[idx + 2]
        
        elif (idx == (N_pts - 2)):
            
            dYdX[idx] = A[7, (m - 3)] * Y[idx - 3] + \
                        A[7, (m - 2)] * Y[idx - 2] + \
                        A[7, (m - 1)] * Y[idx - 1] + \
                        A[7,    m   ] * Y[idx    ] + \
                        A[7, (m + 1)] * Y[idx + 1] 
                          
        elif (idx == (N_pts - 1)): 
            
            dYdX[idx] = A[8, (m - 4)] * Y[idx - 4] + \
                        A[8, (m - 3)] * Y[idx - 3] + \
                        A[8, (m - 2)] * Y[idx - 2] + \
                        A[8, (m - 1)] * Y[idx - 1] + \
                        A[8,    m   ] * Y[idx    ]
                          
        else:
            
            dYdX[idx] = A[4, (m - 4)] * Y[idx - 4] + \
                        A[4, (m - 3)] * Y[idx - 3] + \
                        A[4, (m - 2)] * Y[idx - 2] + \
                        A[4, (m - 1)] * Y[idx - 1] + \
                        A[4,    m   ] * Y[idx    ] + \
                        A[4, (m + 1)] * Y[idx + 1] + \
                        A[4, (m + 2)] * Y[idx + 2] + \
                        A[4, (m + 3)] * Y[idx + 3] + \
                        A[4, (m + 4)] * Y[idx + 4]            
            
    return dYdX

def comp_CD2_deriv(Y):

    N_pts = len(Y);
    dYdX = np.zeros(N_pts);
  
    m = 1;
  
    A = np.array([ \
                  [   0,   -1,   1], \
                  [  -1,    1,   0], \
                  [  -1,    1,   0], \
    ])
  
    for idx in range(0, N_pts):

        
        if ( (idx > 0) and (idx < (N_pts - 1)) ): 

            dYdX[idx] = A[m, (m - 1)] * Y[idx - 1] + \
                        A[m,    m   ] * Y[idx    ] + \
                        A[m, (m + 1)] * Y[idx + 1]
        
        elif (idx == 0):
                  
            dYdX[idx] =  A[(m - 1),    m   ] * Y[idx    ] + \
                         A[(m - 1), (m + 1)] * Y[idx + 1]
            
        elif (idx == (N_pts - 1)):
             
            dYdX[idx] =  A[(m + 1), (m - 1) ] * Y[idx - 1] + \
                         A[(m + 1),    m    ] * Y[idx    ]            
  
        else:
            
            print(f'flow_solver_1D: All conditions have failed.')
            
    return dYdX

def comp_CD10_filter(U):
    
    N_pts = len(U);
    fil_U = np.zeros(N_pts);
  
    m = 5;
  
    A = np.array([ \
        [ 0,   0,   0,   0,    0,   1,   -5,  10, -10,  5, -1], \
        [ 0,   0,   0,   0,   -5,  26,  -55,  60, -35, 10, -1], \
        [ 0,   0,   0,  10,  -55, 126, -155, 110, -45, 10, -1], \
        [ 0,   0, -10,  60, -155, 226, -205, 120, -45, 10, -1], \
        [ 0,   5, -35, 110, -205, 251, -210, 120, -45, 10, -1], \
        [-1,  10, -45, 120, -210, 252, -210, 120, -45, 10, -1], \
        [-1,  10, -45, 120, -210, 251, -205, 110, -35,  5,  0], \
        [-1,  10, -45, 120, -205, 226, -155,  60, -10,  0,  0], \
        [-1,  10, -45, 110, -155, 126,  -55,  10,   0,  0,  0], \
        [-1,  10, -35,  60,  -55,  26,   -5,   0,   0,  0,  0], \
        [-1,   5, -10,  10,   -5,   1,    0,   0,   0,  0,  0]    
    ])
  
    for idx in range(0, N_pts):
        
        if ( (idx >= 5) and (idx <= (N_pts - 6)) ):
        
            fil_U[idx] = U[idx] - (1 / 1024) * sum(A[5, (m - 5) : (m + 5)] * U[idx - 5 : idx + 5])
        
        elif (idx == 0):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[0, (m    ) : (m + 5)] * U[idx     : idx + 5])
            
        elif (idx == 1):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[1, (m - 1) : (m + 5)] * U[idx - 1 : idx + 5])
            
        elif (idx == 2):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[2, (m - 2) : (m + 5)] * U[idx - 2 : idx + 5])            
            
        elif (idx == 3):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[3, (m - 3) : (m + 5)] * U[idx - 3 : idx + 5])            
            
        elif (idx == 4):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[4, (m - 4) : (m + 5)] * U[idx - 4 : idx + 5])            
            
        elif (idx == (N_pts - 5)):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[6, (m - 5) : (m + 4)] * U[idx - 5 : idx + 4])                        
            
        elif (idx == (N_pts - 4)):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[7, (m - 5) : (m + 3)] * U[idx - 5 : idx + 3])            
            
        elif (idx == (N_pts - 3)):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[8, (m - 5) : (m + 2)] * U[idx - 5 : idx + 2])                        
            
        elif (idx == (N_pts - 2)):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[9, (m - 5) : (m + 1)] * U[idx - 5 : idx + 1])                                    
            
        elif (idx == (N_pts - 1)):
            
            fil_U[idx] = U[idx]# - (1 / 1024) * sum(A[10, (m - 5) : (m    )] * U[idx - 5 : idx    ])            

        else: 
            
            print('fin_diff_lib: CD10_filter: Error! Input variable not entering any of the if..else conditions.')

    return fil_U



def comp_RK4_time_step(comp_fluxes, deriv_sten, flow_0, delta_t):

    flow_up = flow_0    
    
    #S1
    flow_1 = flow_0     
    #K1
    flow_1 = comp_fluxes(flow_1, deriv_sten)
    #RK_stage_1    
    flow_up.U_sol = list( map( add, \
                               flow_up.U_sol, \
                               [var_idx * (delta_t / 6) for var_idx in flow_1.F_sol]   ) )    
        
    #S2    
    flow_1.U_sol = list( map(add, flow_0.U_sol, [var_idx * (delta_t * 0.5) for var_idx in flow_1.F_sol] ) )
    #K2
    flow_1 = comp_fluxes(flow_1, deriv_sten)    
    #RK_stage_2    
    flow_up.U_sol = list( map( add, \
                               flow_up.U_sol, \
                               [var_idx * (delta_t / 3) for var_idx in flow_1.F_sol]   ) )        
      
    #S3    
    flow_1.U_sol = list( map(add, flow_0.U_sol, [var_idx * (delta_t * 0.5) for var_idx in flow_1.F_sol] ) )    
    #K3
    flow_1 = comp_fluxes(flow_1, deriv_sten)        
        
    #RK_stage_3    
    flow_up.U_sol = list( map( add, \
                               flow_up.U_sol, \
                               [var_idx * (delta_t / 3) for var_idx in flow_1.F_sol]   ) )        
 
    #S4    
    flow_1.U_sol = list( map(add, flow_0.U_sol, [var_idx * (delta_t) for var_idx in flow_1.F_sol] ) )    
    #K4
    flow_1 = comp_fluxes(flow_1, deriv_sten)            
        
    #RK_stage_4    
    flow_up.U_sol = list( map( add, \
                               flow_up.U_sol, \
                               [var_idx * (delta_t / 6) for var_idx in flow_1.F_sol]   ) )        

    return flow_up

def comp_euler_time_step(comp_fluxes, deriv_sten, flow_0, Delta_t):

    flow_up = flow_0    

    flow_0 = comp_fluxes(flow_0, deriv_sten)
        
    flow_up.U_sol = flow_0.U_sol + Delta_t * flow_0.F_sol        

    return flow_up
    