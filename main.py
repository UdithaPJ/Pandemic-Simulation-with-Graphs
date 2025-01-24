import random
import math
import matplotlib.pyplot as plt

AGE_TYPE_CHILDREN = 1
AGE_TYPE_ADULT = 2
AGE_TYPE_SENIOR = 3

class Person:
    def __init__(self, ageType, wearingMask, familyID, count):
        self.isInfected = False
        self.suspiciousDays = 0
        self.infectedDays = 0 
        self.ageType = ageType
        self.wearingMask = wearingMask
        self.familyID = familyID
        self.id = count

        if ageType == 1:
            self.chanceByAge = random.randint(10, 20)
        elif ageType == 2:
            self.chanceByAge = random.randint(15, 40)
        elif ageType == 3:
            self.chanceByAge = random.randint(35, 60)

        if wearingMask == 1:
            self.reduceChance = random.randint(5, 10)
        else:
            self.reduceChance = 0

    def getInfect(self):
        self.isInfected = True

    def isFamilyMember(self, familyID):
        if familyID == self.familyID and self.familyID != 100001:
            self.chanceByFamily = random.randint(40, 80)
            return True

    def increaseHospitalizedDays(self):
        self.infectedDays += 1

    def increaseDay(self):
        self.suspiciousDays += 1

    def findInfected(self):
        totalChance = self.chanceByAge + self.chanceByFamily - self.reduceChance
        randomChance = random.randint(1, 100)
        return totalChance >= randomChance

class Family:
    def __init__(self, familyID):
        self.familyID = familyID
        self.members = []

    def addMember(self, person):
        self.members.append(person)

class Population:
    def __init__(self):
        self.population = []
        self.patients = []
        self.totalInfected = 0
        self.totalHospitalized = 0
        self.totalRecovered = 0
        self.totalDeaths = 0
        self.stillInHospital = 0
        self.day = 1
        self.dailyInfected = []
        self.dailyHospitalized = []
        self.dailyRecovered = []
        self.dailyDeaths = []
        self.contactOutsidePeopleUpperLimit = 20
        self.indices = []

    def simulate(self, patient):
        self.indices = []
        outsidePeople = random.randint(5, self.contactOutsidePeopleUpperLimit)
        familyID = patient.familyID
        personID = self.population.index(patient)

        for i in range(max(0, personID - 7), min(len(self.population), personID + 7)):
            family = self.population[i].isFamilyMember(familyID)
            if family:
                if i not in self.indices:
                    self.indices.append(i)

        randomOutsidePeople = random.sample(range(0, len(self.population)), outsidePeople)

        for person in randomOutsidePeople:
            personFamily = patient.familyID
            isAMember = patient.isFamilyMember(personFamily)
            if not isAMember and person not in self.indices:
                self.indices.append(person)

        totalHospitalizedAtDay = 0
        infectedAtDay = 0

        for check in self.indices:
            self.population[check].increaseDay()

            if len(self.indices) >= 1 and self.population[check].suspiciousDays > 10:
                self.indices.remove(check)

            isInfected = self.population[check].findInfected()
            if isInfected == 1 or self.population[check].isInfected:
                self.population[check].getInfect()
                infectedAtDay += 1
                totalHospitalizedAtDay += 1
                self.patients.append(self.population[check])

        return totalHospitalizedAtDay, infectedAtDay
    
    def runSimulation(self):
        count = 0
        for family in range(0, 100000):
            noOfFamilyMembers = random.randint(2, 7)
            for member in range(0, noOfFamilyMembers):
                ageType = random.randint(1, 3)
                wearingMask = random.randint(0, 1)
                self.population.append(Person(ageType, wearingMask, family, count))
                count += 1

        for alone in range(0, 1000000 - len(self.population)):
            ageType = random.randint(1, 3)
            wearingMask = random.randint(0, 1)
            self.population.append(Person(ageType, wearingMask, 100001, count))
            count += 1

        Id = 0
        self.patients.append(self.population[Id])

        for day in range(1, 51):
            list3 = list(dict.fromkeys(self.patients))
            totalDeathsAtDay = 0
            recoveredAtDay = 0
            print(f"Day {day}")

            isWearingMask = int(input(f"Are people enforced to wear masks in day {day}? (1 for yes, other for no): "))
            wearingMask = 1 if isWearingMask == 1 else 0

            isTravelling = int(input(f"Are there traveling restrictions in day {day}? (1 for yes, other for no): "))
            contactOutsidePeopleUpperLimit = 50 if isTravelling == 1 else 20

            count = 0 
            for person in list3:
                totalHospitalizedAtDay, infectedAtDay = self.simulate(person)
                self.totalInfected += infectedAtDay
                self.totalHospitalized += totalHospitalizedAtDay
                count += 1
                
                for patient in self.patients:
                    patient.increaseHospitalizedDays()
                    if patient.infectedDays >= 10:
                        recoveredAtDay += 1

                totalDeathsAtDay = math.floor((self.totalHospitalized - 1) * 0.001)
                self.totalDeaths += totalDeathsAtDay
                self.totalRecovered = self.totalHospitalized - self.totalDeaths

            dailyList = [infectedAtDay, totalHospitalizedAtDay, totalDeathsAtDay, recoveredAtDay]
            # Rest of your daily update logic or data handling...

            self.dailyInfected.append(infectedAtDay)
            self.dailyHospitalized.append(totalHospitalizedAtDay)
            self.dailyRecovered.append(recoveredAtDay)
            self.dailyDeaths.append(totalDeathsAtDay)

            print(f'Total Infected: {self.totalInfected}')
            print(f'Total hospitalized: {self.totalHospitalized}')
            print(f'Total recovered: {self.totalRecovered}')
            print(f'Total deaths: {self.totalDeaths}')
            print('#####################################################')

        print('=====================================================')
        print(f'Total Infected: {self.totalInfected}')
        print(f'Total hospitalized: {self.totalHospitalized}')
        print(f'Total recovered: {self.totalRecovered}')
        print(f'Total deaths: {self.totalDeaths}')
        print('=====================================================')

        

    def plotGraphs(self):
        days = list(range(1, 51))

        plt.figure(figsize=(10, 8))

        plt.subplot(2, 2, 1)
        plt.plot(days, self.dailyInfected)
        plt.title('Infected Per Day')
        plt.xlabel('Days')
        plt.ylabel('Infected Count')

        plt.subplot(2, 2, 2)
        plt.plot(days, self.dailyHospitalized)
        plt.title('Hospitalized Per Day')
        plt.xlabel('Days')
        plt.ylabel('Hospitalized Count')

        plt.subplot(2, 2, 3)
        plt.plot(days, self.dailyRecovered)
        plt.title('Recovered Per Day')
        plt.xlabel('Days')
        plt.ylabel('Recovered Count')

        plt.subplot(2, 2, 4)
        plt.plot(days, self.dailyDeaths)
        plt.title('Deaths Per Day')
        plt.xlabel('Days')
        plt.ylabel('Death Count')

        plt.tight_layout()
        plt.show()

population = Population()
population.runSimulation()
population.plotGraphs()
