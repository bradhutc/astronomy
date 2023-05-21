import random as rn
import numpy as np

#Data pulled from NASA Exoplanet Archive.

#.csv file format is important. Data should go from line 1-end, and then an empty line after the end.
#Radii are in terms of Earth Radius.

def get_data(path,name):
    with open(f'{path}/{name}') as thefile:
        contents=thefile.read()
        IndividualPlanets=contents.split('\n')
        #This next line removes the titles of each section of data.
        IndividualPlanets=IndividualPlanets[1:]
        radius=[]
        for str in IndividualPlanets[0:-1]:
            str.split(',')
            if bool(str.split(',')[4]):
                radius.append(float(str.split(',')[4]))
        return radius
    
def distancefrommean(radius):
    avg=sum(radius)/len(radius)
    mylst=[]
    for i in radius:
        mylst.append(round(abs(i-avg),2))
    return mylst

#Function will pull random radii from all data (For Different Systems).
#This is to match a comparison for the n radii we pull from systems that have n exoplanets.
def SystemCreator(radiusofall,num_of_planets):
    difsysrn=[]
    lim=0
    #Choose how many systems you want to generate!
    while lim != 500000:
        difsysrn.append(rn.choices(radiusofall,k=num_of_planets))
        lim+=1
    return difsysrn

def proofrandplanets(distfrommean):
    means=[]
    variances=[]
    std_devs=[]
    for radii in distfrommean:
        means.append(round(np.mean(radii),2))
        variances.append(round(np.var(radii),2))
        std_devs.append(round(np.std(radii),2))
    avgmeans=round(sum(means)/len(means),4)
    avgvariances=round(sum(variances)/len(variances),4)
    avgstd_devs=round(sum(std_devs)/len(variances),4)
    return avgmeans, avgvariances, avgstd_devs

def finalresult(stats_chosen,stats_generated):
    return f"Mean, Variance, & Standard Deviation for Chosen Systems: {stats_chosen} VS Mean, Variance, & Standard Deviation for Generated Systems: {stats_generated}"

    
#---------------------------------------------------------------------
data=[['Kepler169.csv','Kepler-169'],['Kepler-114.csv','Kepler-114'],['Kepler-1031.csv','Kepler-1031'],['Kepler-313.csv','Kepler-313']]

myfilepath='/Users/bradhutc/Desktop/astronomy/A222HWK/exoplanetdata'
AllSystems='allsystems.csv'

samesystemradii80=get_data(myfilepath,'Kepler80.csv')
samesystemmean80=distancefrommean(samesystemradii80)
difsystemradii80=SystemCreator(get_data(myfilepath,'allsystems.csv'),5)

samesystemradii169=get_data(myfilepath,'Kepler169.csv')
samesystemmean169=distancefrommean(samesystemradii169)
difsystemradii169=SystemCreator(get_data(myfilepath,'allsystems.csv'),5)

samesystemradii114=get_data(myfilepath,'Kepler-114.csv')
samesystemmean114=distancefrommean(samesystemradii114)
difsystemradii114=SystemCreator(get_data(myfilepath,'allsystems.csv'),3)

samesystemradii1031=get_data(myfilepath,'Kepler-1031.csv')
samesystemmean1031=distancefrommean(samesystemradii1031)
difsystemradii1031=SystemCreator(get_data(myfilepath,'allsystems.csv'),2)

samesystemradii313=get_data(myfilepath,'Kepler-313.csv')
samesystemmean313=distancefrommean(samesystemradii313)
difsystemradii313=SystemCreator(get_data(myfilepath,'allsystems.csv'),3)

collectionofsamesystemmeans=[samesystemmean80,samesystemmean169,samesystemmean114,samesystemmean1031,samesystemmean313]
collectionofdifsystems=[difsystemradii1031,difsystemradii114,difsystemradii169,difsystemradii313,difsystemradii80]

print(finalresult(proofrandplanets(collectionofsamesystemmeans),proofrandplanets(collectionofdifsystems)))

samesystemradii1031=
