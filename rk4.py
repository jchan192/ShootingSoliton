import numpy as np
def a(n3,n2,n1,n,x):
    return 2*n**2-(4*n3/x
            - 10 * n1*n2/(n*x)
            + 6. * n1**3/(n**2*x)
            - 3  * n3*n1/n
            - 2  * n2**2/n
            + 7. * n1**2*n2/n**2
            - 3  * n1**4/n**3)


def rkshoot(N):
    N = np.int(N)
    x = np.linspace(0,30,N+1)
    x = x[1:]
    
    n = np.zeros(N)
    nn = np.zeros(N)
    nnn = np.zeros(N)
    nnnn = np.zeros(N)
    
    n[0] = 1
    nn[0] = 0
    nnn[0] = -0.612386937160
    nnnn[0] = 0
    dx = x[1]-x[0]
    
    for i in np.arange(N-1)+1:
        a0 = a(nnnn[i-1],nnn[i-1],nn[i-1],n[i-1],x[i-1])
        b0 = nnnn[i-1]
        c0 = nnn[i-1] 
        d0 = nn[i-1] 

        a1 = a(nnnn[i-1] + 0.5 * a0 * dx,
               nnn[i-1]  + 0.5 * b0 * dx,
               nn[i-1]   + 0.5 * c0 * dx,
               n[i-1]    + 0.5 * d0 * dx,
               x[i-1]    + 0.5 * dx)
        b1 = nnnn[i-1]   + 0.5 * a0 * dx
        c1 = nnn[i-1]    + 0.5 * b0 * dx
        d1 = nn[i-1]     + 0.5 * c0 * dx

        a2 = a(nnnn[i-1] + 0.5 * a1 * dx,
               nnn[i-1]  + 0.5 * b1 * dx,
               nn[i-1]   + 0.5 * c1 * dx,
               n[i-1]    + 0.5 * d1 * dx,
               x[i-1]    + 0.5 * dx)
        b2 = nnnn[i-1]   + 0.5 * a1 * dx
        c2 = nnn[i-1]    + 0.5 * b1 * dx
        d2 = nn[i-1]     + 0.5 * c1 * dx

        a3 = a(nnnn[i-1] + a2 * dx,
               nnn[i-1]  + b2 * dx,
               nn[i-1]   + c2 * dx,
               n[i-1]    + d2 * dx,
               x[i-1]    + dx)
        b3 = nnnn[i-1]   + a2 * dx
        c3 = nnn[i-1]    + b2 * dx
        d3 = nn[i-1]     + c2 * dx

        
        n[i] = n[i-1] + dx/6.0       *(d0 + 2*d1 + 2*d2 + d3)
        nn[i] = nn[i-1] + dx/6.0     *(c0 + 2*c1 + 2*c2 + c3)
        nnn[i] = nnn[i-1] + dx/6.0   *(b0 + 2*b1 + 2*b2 + b3)
        nnnn[i] = nnnn[i-1] + dx/6.0 *(a0 + 2*a1 + 2*a2 + a3)
    
    return x,n

