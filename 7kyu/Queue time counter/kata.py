def queue(queuers, pos):
    return sum(min(person, queuers[pos] - (place > pos)) for place, person in enumerate(queuers))
