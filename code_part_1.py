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
sum_Month = [0,0,0,0,0,0,0,0,0,0,0,0]

#for each month add the sum to the list
for pair in Month_values:
    if pair[0] == '01':
        sum_Month[0] = sum_Month[0] + pair[1]    
    if pair[0] == '02':
        sum_Month[1] = sum_Month[1] + pair[1]
    if pair[0] == '03':
        sum_Month[2] = sum_Month[2] + pair[1]
    if pair[0] == '04':
        sum_Month[3] = sum_Month[3] + pair[1]
    if pair[0] == '05':
            sum_Month[4] = sum_Month[4] + pair[1]
    if pair[0] == '06':
        sum_Month[5] = sum_Month[5] + pair[1]
    if pair[0] == '07':
        sum_Month[6] = sum_Month[6] + pair[1]
    if pair[0] == '08':
        sum_Month[7] = sum_Month[7] + pair[1]
    if pair[0] == '09':
        sum_Month[8] = sum_Month[8] + pair[1]
    if pair[0] == '10':
        sum_Month[9] = sum_Month[9] + pair[1]
    if pair[0] == '11':
        sum_Month[10] = sum_Month[10] + pair[1]
    if pair[0] == '12':
        sum_Month[11] = sum_Month[11] + pair[1]
print(sum_Month)

with open('monthly_precipitation.json', 'w') as monthly_p_file:
    json.dump(sum_Month, monthly_p_file)
    

  

