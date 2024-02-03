DUMMY = -100000

CD2 = 1
CD4 = 2
CD6 = 3
CD8 = 4

DRP4 = 5

EUL = 51
RK3 = 53
RK4 = 54

FIL_1 = 101

LCONV_1D = 201


class ip_params:
    
    
    def __init__(self):

        self.flow_model      = DUMMY
        self.deriv_sten      = DUMMY
        self.time_march      = DUMMY
        self.fil_sten        = DUMMY
        
        self.wkdir_grid_read = DUMMY
        self.ip_fname        = DUMMY    
        self.CFL             = DUMMY
        
        self.stop_iter       = DUMMY
        self.stop_time       = DUMMY
        
