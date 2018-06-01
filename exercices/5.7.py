#prevision.meteo.ch/ser

import requests
import json

fcst3 = {}
day = ''
temp = ''
hour = ''
dayshort = ''

req = requests.get('https://www.prevision-meteo.ch/services/json/satigny')
rjson = req.json()

#get only 3 days
for x in range(1,4):
    k = 'fcst_day_'+str(x)
    v = rjson['fcst_day_'+str(x)]
    fcst3[k]=v

for d in fcst3.key():

    dayshort = d['day_short']
    day = d['date']
    hours = d['hourly_data']
        for h in hours.keys:
            hours = 'h'
            temp = hour['h']['TMP2m']



#get temperature by hour
for d in
hd = (fcst3['fcst_day_1']['hourly_data'])







# rjson['fcst_day_1']
