import numpy as np
import geneticAlgorithm
import matplotlib.pyplot as plt

def fitnessFunction(genotype):
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
    # # if(-1 * (sumDiff + prodDiff) >= 0):
    #     # print(totalSum, totalProd)
    #     # print(sumArr, prodArr)
    # return -1 * (sumDiff + prodDiff)
    return np.sum(genotype)

genotypeSize = 15
phenotypeSize = 2
mutationRate = 0.01
populationSize = 10
numTournament = 1000

genesize = 15
popsize = 100
recomprob = 0.5
mutationprob = 0.01
tournaments = 10000

# g = ea.MGA_disc(fitnessfunction, genesize, popsize, recomprob, mutationprob, tournaments)

g = geneticAlgorithm.geneticAlgorithm(fitnessFunction,genotypeSize, mutationRate, populationSize, phenotypeSize)

g.tournament(numTournament)

plt.plot(g.lineFits)
plt.xlabel("Generation Number")
plt.ylabel("Sum of Arrays")
plt.show()