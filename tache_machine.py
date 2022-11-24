import json
f = open('instances/tiny.json')
j = json.load(f)


def nb_machines(dic):
    nb = 0
    list_tasks = dic["tasks"]
    for x in list_tasks:
        nb = max(nb, x["machines"]["machine"])
    return nb


def taches_machines(dic):
    nb = nb_machines(dic)
    list_tasks = dic["tasks"]
    d = {}
    for i in range(1, (nb+1)):
        d[i] = []
    for tache in list_tasks:
        num_tache = tache["task"]
        list_machines = tache["machines"]
        for x in list_machines:
            d[num_tache] += [x["machine"]]
    return (d)


def rarete_machine(taches_machines):
    d = {}
    for x in taches_machines:
        list_machines = taches_machines[x]
        for machine in list_machines:
            if machine in list(d.keys()):
                d[machine] += 1
            else:
                d[machine] = 0
    return (d)
