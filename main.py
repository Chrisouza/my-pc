import platform
import psutil
import json

def hardware():
    info={}
    info['processor'] = platform.processor()
    info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))
    info['disk'] = str(round(psutil.disk_usage("/").total / 1024.0 ** 3))
    return info

def getSugestions(info):
    choises = []
    with open("sugestions.json", "r") as f:
        itens = json.load(f)
        for item in itens:
            if(item['arcteture'] == info['processor'] and item['ram'] <= info['ram']):
                choises.append({"system":item['system'], "interface":item['interface']})
    return choises


if(__name__ == "__main__"):
    info = hardware()
    sugestions = getSugestions(info)
    for s in sugestions:
        print(f"System: {s['system']} - Interface {s['interface']}")