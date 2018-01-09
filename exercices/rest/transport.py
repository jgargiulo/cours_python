#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import json

# Fonction permettant d'envoyer une requête, de récupérer des données
# au format json et de le convertir en un dictionnaire Python
def dictionary_from_json_url(url):
    f = urllib.request.urlopen(url)
    return json.loads(f.read().decode('utf-8'))


def station_details(station, limit):
    # Requête html permettant de récupérer les horaires de transport public à un arrêt (
    url = "http://transport.opendata.ch/v1/stationboard?station={}&limit={}".format(station, limit)
    dico_horaires = dictionary_from_json_url(url)

    for journey in dico_horaires["stationboard"]:
        print(journey["to"])


station_details("Yverdon-les-bains,HEIG-VD", 10)

