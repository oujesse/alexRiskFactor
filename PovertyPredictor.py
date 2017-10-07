from data import *

#calculates weight and percent to use for a factor based on the demographic and numberOfDemographics inside the factor the subject is in.
#(|percent - option1Percent| + |percent - option2Percent| + ...)/(numberOfDemographics - 1)
#Ex: for a 70 year old person below 50 percent povertyLevel (factorIndex, povertyLevelIndex, categoryIndex) = (1, 0, 2):
#percent = 2.9, numberOfDemographics = 3 because length[below 18, 18-64, 65 and above]-->3, weight for 70 year old person = (|2.9 - 6.2| + |2.9 - 8.6|)/2 = 4.5
def weightAndPercent(factorIndex, povertyLevelIndex, categoryIndex):
    #if there is no info on a factor, factorIndex = -1 and the function returns 0,0
    if categoryIndex == -1:
        return 0,0
    percent = totalData[factorIndex][povertyLevelIndex][categoryIndex]
    numberOfDemographics = len(totalData[factorIndex][povertyLevelIndex])
    totalPercentDifference = 0
    #adds together all the |percent - otherOptionPercent| magnitudes into totalPercentDifference
    for otherOptionPercent in totalData[factorIndex][povertyLevelIndex]:
        totalPercentDifference += abs(percent - otherOptionPercent)
    return totalPercentDifference/(numberOfDemographics - 1), percent

#takes in an array of different factor indices that represents which category the input user is in: [sexInd,ageInd,raceInd,livingInd,eduInd,citizenInd,disabilityInd,workInd]
#returns the 3 average percents of povertyLevel risk (percent chance you will be below 50/100/125 percent of poverty level)
#(weight1 * percent1 + weight2 * percent2 + ...)/(weight1 + weight2 + ...) = averaged percent at certain povertyLevel
#Ex: (male, 70yrsOld, white, other living arrangement, bachelors, native, no disability, did not work) --> avgPercents([0, 2, 0, 2, 3, 0, 1, 2]) = 350.32333/35.3333 = 9.914811321
def avgPercents(userFactorCategories):
    #the total percents of chance to be below a poverty level multiplied with corresponding weights
    #number at the end of variable name represents percent of povertyLevel
    #(weight1 * percent1 + weight2 * percent2 + ...)
    totalPercents50 = 0
    totalPercents100 = 0
    totalPercents125 = 0
    #sum of all weights
    #number at the end of variable name represents percent of povertyLevel
    #(weight1 + weight2 + ...)
    weightSum50 = 0
    weightSum100 = 0
    weightSum125 = 0
    #loops through different factor indices
    for factorInd in range(0, len(totalData)):
        weight50, percent50 = weightAndPercent(factorInd, 0, userFactorCategories[factorInd])
        weight100, percent100 = weightAndPercent(factorInd, 1, userFactorCategories[factorInd])
        weight125, percent125 = weightAndPercent(factorInd, 2, userFactorCategories[factorInd])
        totalPercents50 += weight50 * percent50
        totalPercents100 += weight100 * percent100
        totalPercents125 += weight125 * percent125
        weightSum50 += weight50
        weightSum100 += weight100
        weightSum125 += weight125
    print(totalPercents50)
    print(weightSum50)
    return totalPercents50/weightSum50, totalPercents100/weightSum100, totalPercents125/weightSum125
