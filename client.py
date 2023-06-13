import requests, os, time
import psutil

configDict = {}
with open("config.txt") as config:
    for line in config:
        (key, value) = line.strip(' \n').split('=')
        configDict[key] = value

for i in range(10):
    data = {
    "CPU-usage": str(psutil.cpu_percent(2)), 
    "RAM-usage": str(psutil.virtual_memory()[2])
    }
    response = requests.post(f"{configDict['server-ip']}:{configDict['server-port']}", headers= data).text

    print(response)