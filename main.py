import os
import json
import requests
import matplotlib.pyplot as plt
from typing import Dict
from typing import Union

def process(data: Dict[str, int]):
    ...


def call_api(url, parameters):
    response = requests.get(url + parameters)
    return response

def temperature_analysis(temperatures):
    sorted_temperatures = sorted(temperatures)
    max_temperature = sorted_temperatures[len(sorted_temperatures) - 1]
    min_temperature = sorted_temperatures[0]

    return min_temperature, max_temperature, temperatures, sorted_temperatures


def temperature_analysis_storage(temperatures):
    json_content = {"min_temperature": temperatures[0], "max_temperature": temperatures[1], "initial_temperatures": temperatures[2], "sorted_temperatures": temperatures[3]}

    with open("meteo.json", 'w') as json_file:
        json.dumps(json_content, json_file, indent=4)

    if(os.path.exists("meteo.json")):
        return "Fichier d'analyse JSON sauvegardé avec succès sous le nom 'meteo.json' !"
    else:
        return "Il y a eu un problème de sauvegarde des résultats sous format JSON !"

def temperature_analysis_graph(json_file: Union[Dict[str, int], Dict[str, list]]):

    json_data = json_file.load(json_file)

    plt.figure(figsize=(8, 5))
    plt.plot(range(len(json_data["initial_temperatures"])), json_data["sorted_temperatures"], label='Temperature', marker='o', color='blue')

    # Highlight max and min points
    max_idx = json_data["initial_temperatures"].index(json_data["max_temperature"])
    min_idx = json_data["initial_temperatures"].index(json_data["min_temperature"])
    plt.scatter(max_idx, json["max_temperature"], color='red', label='Max', zorder=5)
    plt.scatter(min_idx, json["min_temperature"], color='green', label='Min', zorder=5)

    plt.xlabel('Jours')
    plt.ylabel('Temperature')
    plt.title('Temperature Analysis')
    plt.legend()
    plt.xticks(range(len(json_data["initial_temperatures"])))
    plt.tight_layout()
    plt.savefig("meteo.png")
    plt.close()
    
    if(os.path.exists("meteo.png")):
        return "Le graphique de température pour Paris est généré avec succès sous le nom 'meteo.png' !"
    else:
        return "Il y a eu un problème lors de la génération du graphique !"