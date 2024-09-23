import numpy as np
import matplotlib.pyplot as plt
import random

class genotype():

    def __init__(self, fFunc, gSize, mRate, pSize):
        self.mutationRate = mRate # probability in which a mutation should occur
        self.phenoSize = pSize # number of phenotypes per gene
        self.fitnessFunction = fFunc # The function for measuring the fitness of a genotype
        self.geneSize = gSize # amount of genes in each genotype
        self.geneology = np.zeros(self.geneSize) # Array of genes
        self.randomizeGeneology()
        self.fitnessScore = self.findFitness() # How fit the genotype is


    def randomizeGeneology(self):
        self.geneology = np.random.randint(self.phenoSize,size=(self.geneSize))
        return
    
    def reproduce(self, partner, numMutations=1):
        newGenotype = genotype(self.fitnessFunction, self.geneSize, self.mutationRate, self.phenoSize)
        for i in range(self.geneSize): # Generational (create new in probability to how much more successfull the original was)
            if(np.random.random() <= 0.5):#self.fitnessScore): # Totally randomly mix the two genotypes
                newGenotype.geneology[i] = self.geneology[i]
            else:
                newGenotype.geneology[i] = partner.geneology[i]
        newGenotype.chanceMutate()
        return newGenotype
    
    def chanceMutate(self):
        for geneMutated in range(self.geneSize):
            if(np.random.random() <= self.mutationRate):
                geneMutatedValue = np.random.randint(0, self.phenoSize) # in case non-binary phenotypes
                while(geneMutatedValue == self.geneology[geneMutated]): #ensure that the value is mutated to a different value
                    geneMutatedValue = np.random.randint(0, self.phenoSize)
                self.geneology[geneMutated] = geneMutatedValue
        return

    def numberMutate(self, numMutations):
        geneAlreadyMutated = np.full(self.geneSize, -1)
        geneMutated = np.random.randint(self.geneSize)
        for currentMutation in range(numMutations):
            while(geneMutated in geneAlreadyMutated):
                geneMutated = np.random.randint(self.geneSize) # ensures if mutating multiple phenotypes, it doesn't mutate the same one
            geneMutatedValue = np.random.randomint(self.phenoSize) # in case non-binary phenotypes
            while(geneMutatedValue == self.geneology[geneMutated]): #ensure that the value is mutated to a different value
                geneMutatedValue = np.random.randomint(self.phenoSize)
            self.geneology[geneMutated] = geneMutatedValue 
        return 

    def findFitness(self):
        return self.fitnessFunction(self.geneology)