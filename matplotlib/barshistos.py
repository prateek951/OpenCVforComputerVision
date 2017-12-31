from matplotlib import pyplot as plt 

population_ages = [22,55,62,21,45,34,44,22,5,67,99,110,10,127,111,65,43,43,56,99,111,123]
# ids = [x for x in range(len(population_ages))]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# plt.bar(ids,population_ages,label="Age Distribution for the population")

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
x = [1,2,3,4,5]
y = [2,3,5,6,9]

x2 = [12,32,33,22]
y2 = [23,33,11,22]

plt.bar(x,y,label="Bars1",color="r")
plt.bar(x2,y2,label="Bars2",color="c")

# Give an xlabel
plt.xlabel('Here are my x')
# Give a ylabel
plt.ylabel('Here are my y')
# Add a title
plt.title('Interesting Bar graph')
plt.legend()
plt.show()

