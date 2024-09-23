import numpy as np
import matplotlib.pyplot as plt
import genotype
# import random
import math

class geneticAlgorithm():

    def __init__(self, fFunc, gSize, mRate, pSize, pheSize):
        self.popSize = pSize
        genotypeList = [genotype.genotype(fFunc, gSize, mRate, pheSize) for i in range(self.popSize)]
        self.population = np.array(genotypeList)
        self.fitnessList = np.zeros(self.popSize)
        

    #Shuffling the population will not negatively impact the genotypes
    def shufflePopulation(self):
        np.random.shuffle(self.population)

    def duel(self):
        for i in range(math.floor(self.popSize/2)):
            #pick 2 to fight
            firstGene = self.population[i]
            secondGene = self.population[i+1]
            newGene = firstGene.reproduce(secondGene) #totally randomly mix two genotypes, winner lives
            if(firstGene.fitnessScore >= secondGene.fitnessScore): #pick winner for genotype
                self.population[i+1] = newGene #replace secondGene
            else:
                self.population[i] = newGene # check if this actually changes the gene or just changes a pointer?
        self.shufflePopulation()
        # print()

    def tournament(self, numTournament):
        gens = numTournament // self.popSize
        self.lineFits = np.zeros(shape=(gens))
        gen = 0    
        for tourny in range(numTournament):
            self.duel()
            if tourny % self.popSize == 0:
                for i in range(self.popSize):
                    self.fitnessList[i] = self.population[i].fitnessScore
                # self.lineFits[gen] = np.max(self.fitnessList)
                self.lineFits[gen] = np.mean(self.fitnessList)
                # self.lineFits[2][gen] = np.min(self.fitnessList)
                gen = gen + 1
                print(tourny,np.max(self.fitnessList),np.mean(self.fitnessList),np.min(self.fitnessList))#,np.argmax(self.fitnessList))