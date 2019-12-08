import numpy as np
pp = input("Input a [n:2] matrix using np.array([[n,m],[n1,m1],[n2,m2],[n3,m3]]): ")

def polypit(e):
    x = e[:,0]
    y = e[:,1]
    for n in range(len(e)):
        a = np.polyfit(x, y, n)
        b = np.polyval(a, x)    
        c = np.linalg.norm(y - b)    
        d = [n,c]
        if n == 0:        
            m = d
        elif m[1] >= d[1]:        
            z = d[0]
            
    p = np.polyfit(x, y, z)
    
    print('The coefficients of the polynomial are: ',p)
    
polypit(eval(pp))

# To test, type np.array([[n,m],[n1,m1],[n2,m2],[n3,m3]])
# Example: np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])