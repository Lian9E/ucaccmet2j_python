import json

with open('precipitation.json') as file:
    data = json.load(file)

#Seattle,WA,GHCND:US1WAKG0038

#list called seatle station containing measurements from seatle
    
    seatle_station = []
    for measurement in data:
        if measurement['station'] == 'GHCND:US1WAKG0038':
            seatle_station.append(measurement)
    

    # monthly_precipitation = []
    #     for item in seatle_station:
    #         if ['date'] == '2020-01-01'
    # seatle_station['date'].split('-')
    # # print(seatle_station['date']())
    # montly_precipitation = []
    # for dict in range(30):
    #     if ['date'] 


Month_values = []
#split dates 
for dict in seatle_station:
    split_dates = dict['date'].split('-')
    # makes new list with values and dates
    short_list = [split_dates[1], dict['value']]
    Month_values.append(short_list)

#create a empty list    
sum_Month =[0,0,0,0,0,0,0,0,0,0,0,0,]

#for each month add the sum to the list
for pair in Month_values:
    sum_Month[int(pair[0])-1] += pair[1]
   
print(sum_Month)

with open('monthly_precipitation.json', 'w') as monthly_precipitation:
    json.dump(sum_Month, monthly_precipitation)
    

  

