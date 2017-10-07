#Selected Characteristics of People at Specified Levels
#data received from 2016 American Community Survey 1-Year Estimates
#url: https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_16_1YR_S1703&prodType=table

#Number in array variable name indicates poverty level. Ex: age50 means the percent less than 50 percent of the poverty level.
#Ex: Below 200 percent of poverty level means if the poverty line is 20,000 then a person with 39,999 is below the
#200 percent poverty level because 2.00 * 20,000 = 40,000 and 39,999 < 40,000

#values inputed in these arrays are percent of that demographic that match the corresponding poverty level
#sex[0] = male, sex[1] = female
sex50 = [5.7, 6.8]
sex100 = [12.8, 15.2]
sex125 = [17.1, 20.0]
sex = [sex50,sex100,sex125]
#age[0] = under 18 yrs old, age[1] = 18-64, age[2] = 65 yrs and over
age50 = [8.6, 6.2, 2.9]
age100 = [19.5, 13.2, 9.2]
age125 = [25.5, 17.1, 13.8]
age = [age50,age100,age125]
#race[0] = white, race[1] = black/AfricanAmerican, race[2] = NativeAmerican/AlaskaNative, race[3] = Asian,
#race[4] = NativeHawaiian/otherPacificIslander, race[5] = Some other race, race[6] = two or more races
#race[7] = hispanic/latino origin, race[8] = white alone(not hispanic or latino)
race50 = [5.1, 11.0, 12.5, 5.8, 8.2, 8.7, 7.9, 8.3, 4.6]
race100 = [11.6, 23.9, 26.2, 11.8, 18.1, 22.7, 17.8, 21.0, 10.0]
race125 = [15.6, 30.3, 33.1, 15.3, 22.8, 30.6, 23.2, 28.4, 13.3]
race = [race50,race100,race125]
#living: living arrangement, living[0] = in married-couple family, living[1] = in female householder(no husband)
#living[2] = in other living arrangement
living50 = [2.0, 14.1, 12.2]
living100 = [6.4, 29.4, 23.9]
living125 = [9.5, 36.8, 29.9]
living = [living50,living100,living125]
#edu: educational attainment, edu[0] = less than high school grad, edu[1] = highschool grad
#edu[2] = some college/associate degree, edu[3] = bachelor's degree or higher
edu50 = [9.5, 5.8, 4.3, 2.2]
edu100 = [25.4, 13.9, 10.0, 4.4]
edu125 = [33.9, 18.9, 13.6, 5.9]
edu = [edu50,edu100,edu125]
#citizen: nativity and citizenship status, citizen[0] = native, citizen[1] = foreign born,
#citizen[3]= naturalized citizen
citizen50 = [6.1, 6.8, 3.6]
citizen100 = [13.7, 16.5, 10.8]
citizen125 = [18.0, 22.2, 15.0]
citizen = [citizen50,citizen100,citizen125]
#disability: disability status, disability[0] = with any disability, disability[1] = no disability
disability50 = [7.9, 6.0]
disability100 = [20.9, 13.1]
disability125 = [27.6, 17.3]
disability = [disability50,disability100,disability125]
#work: work status, work[0] = fulltime(year-round), work[1] = less than fulltime(year-round),
#work[2] = did not work
work50 = [0.5, 8.2, 16.8]
work100 = [2.9, 18.4, 30.7]
work125 = [5.2, 23.8, 36.9]
work = [work50,work100,work125]

#number of factors. Ex: SEX, AGE, RACE, EDU --> 4
numberOfFactors = 8

#totalData[DemographicFactor][povertyLevel][factorCategory] = percent below that poverty level
#Ex: totalData[2][0][3] --> totalData[race][below 50 percent of poverty level][Asian] = 5.8
totalData = [sex,age,race,living,edu,citizen,disability,work]
