import numpy as np

class MGA_disc():

    def __init__(self, fitnessfunction, genesize, popsize, recomprob, mutationprob, tournaments):
        self.genesize = genesize
        self.popsize = popsize
        self.recomprob = recomprob
        self.mutationprob = mutationprob
        self.tournaments = tournaments
        self.fitnessfunction = fitnessfunction
        self.pop = np.random.randint(2,size=(popsize,genesize))
        gens = tournaments//popsize      
        self.bestfit = np.zeros(gens)
        self.meanfit = np.zeros(gens)


    def run(self):
        # 1 loop for tour
        gen = 0
        for t in range(self.tournaments):
            # 2 pick two to fight (same could be picked -- fix)
            a = np.random.randint(self.popsize)
            b = np.random.randint(self.popsize)
            # 3 pick winner
            if self.fitnessfunction(self.pop[a]) > self.fitnessfunction(self.pop[b]):
                winner = a
                loser = b
            else:
                winner = b
                loser = a
            # 4 transfect winner to loser
            for g in range(self.genesize):
                if np.random.random() < self.recomprob: 
                    self.pop[loser][g] = self.pop[winner][g] 
            # 5 mutate loser
            for g in range(self.genesize):
                if np.random.random() < self.mutationprob: 
                    if self.pop[loser][g] == 1:
                        self.pop[loser][g] = 0
                    else:
                        self.pop[loser][g] = 1
            # 6 Stats 
            if t % self.popsize == 0:
                fits = np.zeros(self.popsize)
                for i in range(self.popsize):
                    fits[i] = self.fitnessfunction(self.pop[i])
                self.bestfit[gen] = np.max(fits)
                self.meanfit[gen] = np.mean(fits)
                gen +=1
                print(t,np.max(fits),np.mean(fits),np.min(fits),np.argmax(fits))

class MGA_real():

    def __init__(self, fitnessfunction, genesize, popsize, recomprob, mutationprob, tournaments):
        self.genesize = genesize
        self.popsize = popsize
        self.recomprob = recomprob
        self.mutationprob = mutationprob
        self.tournaments = tournaments
        self.fitnessfunction = fitnessfunction
        self.pop = np.random.random((popsize,genesize))
        self.fit = self.calculateFitness()
        # stats
        gens = tournaments//popsize      
        self.bestfit = np.zeros(gens)

    def calculateFitness(self):
        fits = np.zeros(self.popsize)
        for i in range(self.popsize):
            fits[i] = self.fitnessfunction(self.pop[i])
        return fits

    def run(self):
        # 1 loop for tour
        gen = 0
        for t in range(self.tournaments):
            # 2 pick two to fight (same could be picked -- fix)
            [a,b] = np.random.choice(np.arange(self.popsize),2,replace=False)
            # 3 pick winner
            if self.fit[a] > self.fit[b]:
                winner = a
                loser = b
            else:
                winner = b
                loser = a
            # 4 transfect winner to loser
            for g in range(self.genesize):
                if np.random.random() < self.recomprob: 
                    self.pop[loser][g] = self.pop[winner][g] 
            # 5 mutate loser
            self.pop[loser] += np.random.normal(0,self.mutationprob,self.genesize)
            self.pop[loser] = np.clip(self.pop[loser],0,1)
            # Update
            self.fit[loser] = self.fitnessfunction(self.pop[loser])
            # 6 Stats 
            if t % self.popsize == 0:
                self.bestfit[gen] = np.max(self.fit)
                gen += 1
                print(t,np.max(self.fit),round(np.mean(self.fit), 1),np.min(self.fit),np.argmax(self.fit))


            
