def golf_score_calculator(par_string, score_string):
    return sum(int(score) - int(par) for score, par in zip(score_string, par_string))
