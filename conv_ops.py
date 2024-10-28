# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#
# Written by Alwaleed Alrashidi 
# Other contributors: Prof Brad Denby (Boilerplate and lecture slide refernce code)
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math

if len(sys.argv)==9:

c_in = int(sys.argv[1])
h_in = int(sys.argv[2])
w_in = int(sys.argv[3])
n_filt = int(sys.argv[4])
h_filt = int(sys.argv[5])
w_filt = int(sys.argv[6])
s = int(sys.argv[7])
p = int(sys.argv[8])

else:
    print(\
     'Usage: '\
     'python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
    )
    exit()


h_out = (h_in-h_filt + 2*p)//s+1
w_out = (w_in-w_filt+2*p)//s+1
c_out = n_filt


adds = c_out*h_out*w_out*c_in*h_filt*w_filt
muls = adds 
divs = 0  


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed 
