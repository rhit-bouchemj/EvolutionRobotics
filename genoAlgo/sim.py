import numpy as np
import ea 
import math
import matplotlib.pyplot as plt 

def fitnessfunction(genotype):
    # sumArr = []
    # prodArr = []
    # for i in range(len(genotype)):
    #     if genotype[i] == 0:
    #         sumArr.append(i+1)
    #     else:
    #         prodArr.append(i+1)
    # totalSum = np.sum(sumArr)
    # totalProd = np.prod(prodArr)
    # sumDiff = np.abs(totalSum - 36)
    # prodDiff = np.abs(totalProd - 360) / 10
    # if(-1 * (sumDiff + prodDiff) >= 0):
    #     print(totalSum, totalProd)
    #     print(sumArr, prodArr)
    # return -1 * (sumDiff + prodDiff)
    return np.sum(genotype)

# Global variables
genesize = 100
popsize = 1000
recomprob = 0.5
mutationprob = 0.05
tournaments = 10000

g = ea.MGA_disc(fitnessfunction, genesize, popsize, recomprob, mutationprob, tournaments)

print("\n Example evolutionary run using discrete genotype:")
g.run()

# g = ea.MGA_real(fitnessfunction, genesize, popsize, recomprob, mutationprob, tournaments)
# print("\n Example evolutionary run using real-valued genotype:")
# g.run()

plt.plot(g.bestfit)
plt.plot(g.meanfit)
plt.xlabel("Generation Number")
plt.ylabel("Fitness Score")
plt.legend(["Best Fit", "Mean Fit"])

plt.show()