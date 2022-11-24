import pdb
import json
import pandas as pd
f = open('instances/tiny.json')
data = json.load(f)

L = [1, 2, 3]

def duree_liste_task(tasks):
    tasks_info = data['tasks']
    temps = 0

    for task in tasks:
        temps += tasks_info[task-1]['processing_time']
    
    return temps

def duree_reste_job(job, derniere_task = 0):
    dic_job = data['jobs'][job-1]
    liste = dic_job['sequence'][derniere_task:]

    temps = duree_liste_task(liste)
    return temps


print(duree_reste_job(1, 2))
