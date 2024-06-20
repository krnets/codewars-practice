# def distances_from_average(test_list):
#     avg = sum(test_list) / len(test_list)
#     return [round(avg - x, 2) for x in test_list]

import numpy as np


def distances_from_average(test_list):
    mean = np.mean(test_list)
    return np.around(mean - test_list, 2).tolist()

    # return np.around(np.mean(test_list) - test_list, 2).tolist()