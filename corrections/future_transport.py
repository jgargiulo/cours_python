#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
from concurrent.futures import *
from time import time
import urllib.request
import json

def dictionary_from_json_url(url):
    try:
        f = urllib.request.urlopen(url)
        return json.loads(f.read().decode('utf-8'))
    except HTTPError as e:
        time.sleep(1)
        return dictionary_from_json_url(url)


def station_details(station, limit=10):
    url = "http://transport.opendata.ch/v1/stationboard?station={}&limit={}".format(station, limit)
    dic = dictionary_from_json_url(url)

    res = "Horaires pour {}:".format(dic["station"]["name"])

    for i in dic["stationboard"]:
        stop = i["stop"]
        res += i["name"] 
        res += i["stop"]["departure"].split("T")[1].split('+')[0] 
        res += i["to"] 
        res += "\n"
    return res

with ProcessPoolExecutor(max_workers=4) as executor:

    start = time()


    resultat = []
    for i in executor.map(station_details, ["Yverdon", "Zurich", "Geneve", "Bern", "Geneve,poterie", "Cossonay-Penthalaz", "Penthaz", "Neuchatel"]):
        resultat.append(i)


    t = time()-start

    for r in resultat:
        print(r)

    print(t)
    
