from PovertyPredictor import *
import json
import sys

#script arguments is a javascript object (Ex: {"sexOptions": "male", "ageOptions": "empty", "raceOptions": "white", ...})
#converts that js object into a python dictionary
print(sys.argv[1])
options = json.load(open(sys.argv[1]))
#loop through the keys in options and then puts them into an array of different factor indices that represents which category the input user is in: [sexInd,ageInd,raceInd,livingInd,eduInd,citizenInd,disabilityInd,workInd]
userFactorCategories = [None] * 8 #8 corresponds to the number of keys in js object and also number of factors
for factorString in options:
    tempFactorIndex = factorToIndex[factorString] #Ex: "raceOptions" --> 2
    tempDict = factorIndexToDict[tempFactorIndex] #Ex: 2 --> raceDict
    tempCategoryIndex = tempDict[options[factorString]] #Ex: "black" --> 1
    userFactorCategories[tempFactorIndex] = tempCategoryIndex #Ex: "raceOptions":"black" --> [_,_,1, ...]
b50,b100,b125 = avgPercents(userFactorCategories) #assigns the variables that represent percent chance below 50/100/125 percent of poverty level

print(json.dumps({"riskBelow50": b50, "riskBelow100": b100, "riskBelow125": b125}, sort_keys = True))
