def start_tasks(tasks_to_start, tasks_en_cours, tasks):
    for task in tasks_to_start:
        index = task['task']
        real_task = tasks[index]
        task['temps-avant-fin'] = real_task['processing_time']
        tasks_en_cours.append(task)
    
    return tasks_en_cours