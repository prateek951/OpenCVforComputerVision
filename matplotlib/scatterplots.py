# To show correlation between variables we use scatter plots
from matplotlib import pyplot as plt 
x = [1,2,3,4,5,6,7,8]
y = [5,6,7,8,9,4,4,2]
plt.scatter(x,y,label='skitscat',color='k',marker='x',s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph \n Check it out')
plt.legend()
plt.show()
