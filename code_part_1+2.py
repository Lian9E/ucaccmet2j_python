import json

with open('precipitation.json') as file:
    data = json.load(file)

#Seattle,WA,GHCND:US1WAKG0038

#list called seatle station containing measurements from seatle
    
    seatle_station = []
    for measurement in data:
        if measurement['station'] == 'GHCND:US1WAKG0038':
            seatle_station.append(measurement)

Month_values = []

for dict in seatle_station:
    #split dates
    split_dates = dict['date'].split('-')
    # makes new list with values and dates
    short_list = [split_dates[1], dict['value']]
    Month_values.append(short_list)

#create a empty list    
sum_Month =[0,0,0,0,0,0,0,0,0,0,0,0,]

# make a list with the sums of each month
for pair in Month_values:
    sum_Month[int(pair[0])-1] += pair[1]
   
print(f' the list of precipitation per month is: {sum_Month}')

#save the list to a json file
with open('results1.json', 'w') as monthly_precipitation:
    json.dump(sum_Month, monthly_precipitation)

#calculate total precipitation of the whole year
sum_year = sum(sum_Month)
print(f'The total amount of precipitation in seatle is {sum_year} in 2010')

#for each month calculate the percentage of the total precipitation
Monthly_percentage = []
for month in sum_Month:
    percentage = month/sum_year * 100
    Monthly_percentage.append(percentage)
print(f'The list of monthly percentages is: {Monthly_percentage}')

#make a dictionary containing all information for seatle
seatle_precipitation = {}
seatle_precipitation.update({'station': 'GHCND:US1WAKG0038'})
seatle_precipitation.update({'state': 'WA'})
seatle_precipitation.update({'totalMonthlyPrecipitation': sum_Month})
seatle_precipitation.update({'relativeMonthlyPrecipitation': Monthly_percentage})
seatle_precipitation.update({'totalYearlyPrecipitation': sum_year})

#save the dictionary to a json file
with open('result2.json', 'w') as seatle_file:
    json.dump({'Seattle':seatle_precipitation}, seatle_file)



    

  

