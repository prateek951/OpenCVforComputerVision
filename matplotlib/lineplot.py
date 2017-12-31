from matplotlib import pyplot as plt 

# Function to plot a line 

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y,label='First Line')
plt.plot(x2,y2,label='Second Line')
# Legends,titles and plots in matplotlib
# which is quite similiar to matlab
plt.xlabel('Plot number')
plt.ylabel('Important variable')
plt.title('Interesting Graph \n Check it out')

# Invoke the legend
plt.legend()

plt.show()