import numpy as np

def shoot(N):
    N = np.int(N)
    x = np.linspace(0,30,N+1)
    x = x[1:]
    
    n =  np.zeros(N)
    n1 =  np.zeros(N)    
    n2 =  np.zeros(N)    
    n3 =  np.zeros(N)    

    # initial condition
    n[0] = 1
    n1[0] = 0
    n2[0] = -0.612386937160
    n3[0] = 0
    dx = x[1]-x[0]
    
    for i in np.arange(N-1)+1:
        n[i]  = n[i-1]  + n1[i-1]*dx 
        n1[i] = n1[i-1] + n2[i-1]*dx
        n2[i] = n2[i-1] + n3[i-1]*dx
        n3[i] = n3[i-1] + (2*n[i-1]**2  -(4  * n3[i-1]/x[i-1]
                                        - 10 * n1[i-1]*n2[i-1]/(n[i-1]*x[i-1])
                                        + 6. * n1[i-1]**3/(n[i-1]**2*x[i-1])
                                        - 3  * n3[i-1]*n1[i-1]/n[i-1]
                                        - 2  * n2[i-1]**2/n[i-1]
                                        + 7. * n1[i-1]**2*n2[i-1]/n[i-1]**2
                                        - 3  * n1[i-1]**4/n[i-1]**3)) * dx
    
    return x,n

