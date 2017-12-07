#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import json
import threading
import queue
import time

limit = 10


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

    res = "Horaires pour {}:".format(dic["station"]["name"]) + '\n'

    for i in dic["stationboard"]:
        stop = i["stop"]
        res += i["name"] + '\t'
        res += i["stop"]["departure"].split("T")[1].split('+')[0] + '\t'
        res += i["to"] + '\n'
    res += '\n'
    return res


class Departs(threading.Thread):
    def __init__(self, station, limit=10):
        super().__init__()
        self.station = station
        self.limit = limit

    def run(self):
        print(station_details(self.station, self.limit))


class DepartsQueue(threading.Thread):
    def __init__(self, queue, res_queue, limit=10):
        super().__init__()
        self.queue = queue
        self.res_queue = res_queue
        self.limit = limit

    def run(self):
        while True:
            station = self.queue.get()
            if station is None:
                break
            self.res_queue.put((station, station_details(station)))
            self.queue.task_done()


stations = ["Yverdon-les-bains", "Geneve", "Lucerne", "Vevey", "Brig",
          "Coppet", "Romont", "Bern", "Zurich", "Winterthur" ]

t0 = time.time()

# Not sync version: result can be interlaced
# for station in stations:
#     d = Departs(station)
#     d.start()


### Queue version
q = queue.Queue()
res = queue.Queue()

# Start the worker threads
worker_count = 5
workers = []
for i in range(worker_count):
    worker = DepartsQueue(q, res)
    worker.start()
    workers.append(worker)

# Enqueue the task
for station in stations:
    q.put(station)

# wait for all task to be done
q.join()

# stop the workers
for i in range(worker_count):
    q.put(None)
for worker in workers:
    worker.join()

# show result in stations order
dic_res = {}
while not res.empty():
    res_val = res.get()
    dic_res[res_val[0]] = res_val[1]

for station in stations:
    print(dic_res[station])

# show calculation time
print(time.time() - t0)
