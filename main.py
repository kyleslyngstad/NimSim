import itertools
import os

#Person Class
class Person():
    idCount = itertools.count()
    personList = []
    def __init__(self):
        self.pId = next(Person.idCount)
        self.wealth = 0
        self.foodSupply = 0
        self.houseStatus = 0
        self.skills = {"farming":0, "building":0}
        #self.city = 'None'
        Person.personList.append(self)

    def hunger(self):
        return 50 - self.foodSupply*5

    def shelter(self):
        return 90 - self.houseStatus*30

#Create a function that modifies each birth with different stats.
def personRand():
    Person()

#Create a function that starts a city population
def startCity(popCount, cityName): #Later add stoneDensity and foodDensity to measure the abundance of those resources.
    #run the personRand
    for p in range(popCount):
        personRand()

    f = "./%s" % cityName
    try: os.mkdir(f)
    except: pass

    #write the people to a .csv
    #name the file the cityName+turn# so Seattle_0

#def turnCity(): #Reads in the city.csv and applies the logic for 1 turn then writes the results to a new.csv (Seattle_1.csv)

startCity(5,'Seattle')
