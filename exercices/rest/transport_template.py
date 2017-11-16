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

    print("Horaires pour {}:".format(dico_horaires["station"]["name"]))
    
    # A vous d'afficher les prochains départs
    # analysez les clés et les valeurs du dico_horairestionnaire

    # Vous pouvez analyser le résultat de la requête dans votre navigateur à l'adresse :
    # http://transport.opendata.ch/v1/stationboard?station=yverdon-les-bains,heig-vd&limit=10

    # Aidez vous également de la docutmentation de l'api libre des transports publics suisses :
    # http://transport.opendata.ch/docs.html#stationboard
    print(dico_horaires)


station_details("Yverdon-les-bains,HEIG-VD", 10)

