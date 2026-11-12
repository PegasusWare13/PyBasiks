#Ts looks like CSS which I hate by heart ughh
import matplotlib.pyplot as plt
import numpy as np

bf = np.array([8,12,16,20,24,28])
psl = np.array([8,7.5,7,6,3,2])

#defining Fonts through dictionaries for fontdict
font1 = {'family' : 'Times New Roman', 'size' : 25, 'color' : 'r'}
font2 = {'family' : 'Arial', 'size' : 15, 'color' : 'b'}
#x,y labels
plt.xlabel("BodyFat%", fontdict=font1)
plt.ylabel("PSL Scale", fontdict= font2) 
#titleLabel
plt.title("PSL Scale vs BodyFat Correlation",fontdict={'family':'Montserrat', 'size' : 40, 'color' : 'g'})
plt.plot(bf, psl, marker = 'o')
#Grid
plt.grid(axis='x',color = 'purple', linestyle = 'dotted', linewidth = 0.3) #If Axis not mention, grid is drawn through both x and y axis
plt.show()