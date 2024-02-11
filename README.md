PONNI PROJECT ARCHITECTURE



           ===========================         
           :                         :
           : user_module             :  
           :   => set_init_cond      : 
           :   => set_boundary_cond  :     
           :                         :  
           :                         :
           ===========================
                        |
                        |
                        V 
           ===========================          ==========================       
           :                         :          :                        :
           : Generic_2D_solver       :          :  fin_diff_lib          :
           :   => set_init_cond      :<=========:    => CD8 diff         :
           :   => set_boundary_cond  :          :    => RK4              :
           :   => compute_fluxes     :          :    => CD10 filter      :
           :                         :          :                        :
           ===========================          ==========================
                        |  
                        |               
                        V   
           =======================================
           :                                     :
           : Flow_solver_2D_lib                  :  
           :   => read_grid_file                 : 
           :   => compute_time_step              : 
           :   => Time loop for Rk4              :
           :   => Write output data as HDF5 file : 
           :                                     :
           =======================================


FLOW SOLVER STATUS

    1. The solver contains a 1D convection module with periodic boundary condition. The testcases appear to be satisfactory for now. More testing needed.

FUTURE UPDATES

    1. Next step is to clean up the solver + get the filtering stencil working.
    2. Implement the non-periodic boundary condition + schemes
    3. Add a sponge layer + PID type controller feature if possible.  
    4. Write a 1D acoustic solver + NRBC. 
    5. Write a 1D Euler equation solver + NSCBC. 
    6. 2D convection equation
    7. 2D NS equation
        i. Couette flow.
       ii. Flow over backward facing step. 
      iii. 2D plane jet. 
