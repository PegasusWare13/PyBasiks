import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([2,3,5,7])
y1 = np.array([3,2,6,8])
x2 = np.array([-2,-6,2,11])
y2 = np.array([-6,-7,-2,1])
plt.plot(x1,y1,x2,y2)
plt.show()

#keywords-->> color[c], linestyle[ls]
plt.plot(x1,y1, c='#1F8A3C', ls='dashdot')
plt.show()
# 'solid' (default)	'-'	
# 'dotted'	':'	
# 'dashed'	'--'	
# 'dashdot'	'-.'	
# 'None'	'' or ' '
