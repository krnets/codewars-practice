def check_exam(arr1, arr2):
    score = 0

    for correct_answer, submitted_answer in zip(arr1, arr2):
        if submitted_answer == correct_answer:
            score += 4
        elif submitted_answer == "":
            continue
        else:
            score -= 1

    return max(0, score)