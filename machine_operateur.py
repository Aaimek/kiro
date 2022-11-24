import json
f = open('instances/tiny.json')
j = json.load(f)


def machine_operateur(dic):
    list_tasks = dic["tasks"]
    d = {}
    for tache in list_tasks:
        list_machines = tache["machines"]
        num_tache = tache["task"]
        for machine in list_machines:
            list_operateur = machine["operators"]
            num_machine = machine["machine"]
            d[(num_tache, num_machine)] = set(list_operateur)
    return (d)


print(machine_operateur(j))
