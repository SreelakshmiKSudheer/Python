from statistics import mean
from scipy import stats
# library for plotting
import matplotlib.pyplot as plt 

estimates = [100,1010,1786,200,1500,1500,100,120,120,150,150,175,210]

estimates.sort()

# stats.trim_mean(list_name,proportional cut)
m = stats.trim_mean(estimates, 0.1)
print(m)

'''
for i in range(len(estimates)):
    print(estimates[i])
'''
'''
tv = int(0.1 * len(estimates))      # get the index by the 10% value 

estimates = estimates[tv:]          # trims the list by removing first 10%  --- the list reduces to a list were first element org_list[tv] to the end
estimates = estimates[: len(estimates) - tv]

print(mean(estimates))
'''

# Plotting
plt.plot([1,2,3,4])             # both x and y value will be the ones given-----grapg
plt.plot([1,2,3,4],[1,4,9,16])  # x values then y values --- graph
plt.xlabel("x values")          # labeling x axis
plt.ylabel("y values")          # labeling y values
plt.plot([1,2,3,4],[1,4,9,16], 'ro')    # plots as points
plt.plot([1,2,3,4],[1,4,9,16], 'r--')   # plots as red dotted lines or red dashes
plt.plot([1,2,3,4],[1,4,9,16],'bs')     # plot as blue squares
plt.plot([1,2,3,4],[1,4,9,16], 'g^')    # plots as green triangles

plt.plot(estimates)             # plot a list

y = []
tv = int(0.1 * len(estimates))      # get the index by the 10% value 

estimates = estimates[tv:]          # trims the list by removing first 10%  --- the list reduces to a list were first element org_list[tv] to the end
estimates = estimates[: len(estimates) - tv]

for i in range(len(estimates)):
    y.append(5)
    
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'bs')
plt.plot([375],[5],'g^')