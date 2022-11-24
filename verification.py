import json
import pandas as pd
from write_solution import write_solution
from update_tasks import update_tasks
f = open('instances/tiny.json')
data = json.load(f)


def sol_primaire(j):
    d = {}
    i = 0
    jobs = data["jobs"]
    task_en_cours = []
    task_finish = []
    tete = {}
    avancement_job = {}
    temps_restant = {}
    poids_tache_restante = {}
    operateur_pas_dispo = []
    task_finies = []
    task_en_cours = []
    for elem in jobs:
        avancement_job[elem["job"]] = 0
        tete[elem["job"]] = 0
        temps_restant[elem["job"]] = elem["due_date"]
    while i != 0:
        i += 1
        for elem in jobs:
            tete[elem["job"]] = elem["sequence"][avancement_job[elem["job"]]]
